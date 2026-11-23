#!/usr/bin/env python3
"""Decision logic for the release-record workflow. Nothing here writes to GitHub.

Three questions, kept out of the YAML so they can be tested offline:

1. classify(tag) - which module, which language line, which version, and whether the
   version is a pre-release (the hyphen inside a tag like ``catalog-v0.4.0`` is part of
   the line name, not a pre-release marker).
2. gate(module, version, lines) - are the artifacts this record would advertise actually
   resolvable? A tag existing does not mean Maven, PyPI and the Go proxy served it, and
   the publish jobs run in parallel with any recording job. Every verdict needs two
   independent readings: the exact-version URL *and* an unfiltered summary (Maven
   ``maven-metadata.xml``, the PyPI package JSON, the Go proxy ``@v/list``). Verdicts:

     available     both readings agree that the version is there
     unavailable   both agree it is not: the exact URL answered a real HTTP error code
                   (not a failed connection) and the unfiltered summary omits the version
     conflict      the two readings disagree
     unverifiable  a probe could not be performed (DNS/connect/TLS failure, HTTP 0)
     yanked        the version is there but withdrawn

   Anything but ``available`` blocks the record. A failed probe is reported as
   unverifiable, never as "not published".
3. plan(...) - create or edit the release object, whether it may hold the "Latest" slot,
   and why. Backfilling never promotes Latest; an explicit promotion is refused when the
   current Latest is a newer stable version.

Usage:
  release_record.py classify --tag catalog-v0.4.0
  release_record.py gate --module catalog --version 0.4.0 --lines java,python,go
  release_record.py plan --tag catalog-v0.4.0 --current-latest v0.3.0-SNAPSHOT --promote-latest
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

MAVEN_BASE = "https://repo1.maven.org/maven2"
PYPI_BASE = "https://pypi.org/pypi"
GOPROXY_BASE = "https://proxy.golang.org"
GO_MODULE_ROOT = "github.com/aliyun/aliyun-odps-openapi-sdk"

LINES = {
    "catalog": {
        "java": {
            "coordinate": "com.aliyun.odps:catalog-api",
            "artifact_id": "catalog-api",
            "group_path": "com/aliyun/odps",
        },
        "python": {"coordinate": "pyodps_catalog", "package": "pyodps_catalog"},
        "go": {"coordinate": GO_MODULE_ROOT + "/catalog-api/go", "suffix": "catalog-api/go"},
    },
    "common": {
        "java": {
            "coordinate": "com.aliyun.odps:openapi",
            "artifact_id": "openapi",
            "group_path": "com/aliyun/odps",
        },
        "python": {"coordinate": "maxcompute_tea_openapi", "package": "maxcompute_tea_openapi"},
        "go": {"coordinate": GO_MODULE_ROOT + "/common/go", "suffix": "common/go"},
    },
}

# Longest line prefixes first: "catalog-py-v" must be tested before "catalog-v".
TAG_PREFIXES = [
    ("catalog-api/go/v", "catalog", "go"),
    ("common/go/v", "common", "go"),
    ("catalog-py-v", "catalog", "python"),
    ("common-py-v", "common", "python"),
    ("catalog-v", "catalog", "java"),
    ("common-v", "common", "java"),
]


def classify(tag: str) -> dict:
    """Return module/line/version/prerelease/primary for a release tag."""
    for prefix, module, line in TAG_PREFIXES:
        if tag.startswith(prefix):
            version = tag[len(prefix):]
            if not version:
                raise ValueError(f"tag {tag!r} has no version after the line prefix")
            prerelease = "-" in version
            return {
                "tag": tag,
                "module": module,
                "line": line,
                "version": version,
                "prerelease": prerelease,
                # The Java-line tag carries the record for its module's version (RELEASING.md 3).
                "primary": line == "java",
                # Only the product line may own the repository-wide Latest slot: the
                # common line's versions (1.3.x) are numerically higher than catalog's
                # (0.4.x), so letting it promote would pin Latest to the shared runtime.
                "latest_owner": module == "catalog" and line == "java",
                "flat": tag.replace("/", "-"),
            }
    raise ValueError(f"unsupported tag {tag!r}: expected one of {[p for p, _, _ in TAG_PREFIXES]}")


def version_of(tag: str) -> str:
    """Strip the line prefix from a known tag; fall back to a leading "v"."""
    for prefix, _, _ in TAG_PREFIXES:
        if tag.startswith(prefix):
            return tag[len(prefix):]
    return tag[1:] if tag[:1] in ("v", "V") else tag


def semver_key(version: str) -> tuple:
    """Sortable key for a version. Release > any pre-release of the same core."""
    core, _, pre = version.partition("-")
    parts = []
    for chunk in core.split("."):
        parts.append(int(chunk) if chunk.isdigit() else 0)
    while len(parts) < 3:
        parts.append(0)
    return (tuple(parts[:3]), 0 if pre else 1, pre)


def http_get(url: str, timeout: int = 30):
    """Return (status, body). Network only; tests inject their own fetcher."""
    request = urllib.request.Request(url, headers={"User-Agent": "release-record-gate/1"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except OSError as exc:
        return 0, f"transport-error: {exc}"


def _maven_urls(module: str, version: str) -> dict:
    spec = LINES[module]["java"]
    group, artifact = spec["group_path"], spec["artifact_id"]
    exact = f"{MAVEN_BASE}/{group}/{artifact}/{version}/{artifact}-{version}.jar"
    metadata = f"{MAVEN_BASE}/{group}/{artifact}/maven-metadata.xml"
    return {"exact": exact, "summary": metadata, "coordinate": spec["coordinate"]}


def _pypi_urls(module: str, version: str) -> dict:
    spec = LINES[module]["python"]
    package = spec["package"]
    return {
        "exact": f"{PYPI_BASE}/{package}/{version}/json",
        "summary": f"{PYPI_BASE}/{package}/json",
        "coordinate": package,
    }


def _goproxy_urls(module: str, version: str) -> dict:
    spec = LINES[module]["go"]
    path = f"{GO_MODULE_ROOT}/{spec['suffix']}"
    return {
        "exact": f"{GOPROXY_BASE}/{path}/@v/v{version}.info",
        "summary": f"{GOPROXY_BASE}/{path}/@v/list",
        "coordinate": path,
    }


def urls_for(line: str, module: str, version: str) -> dict:
    if line == "java":
        return _maven_urls(module, version)
    if line == "python":
        return _pypi_urls(module, version)
    if line == "go":
        return _goproxy_urls(module, version)
    raise ValueError(f"unknown line {line!r}")


def _maven_verdict(fetch, urls, version):
    exact_status, exact_body = fetch(urls["exact"])
    summary_status, summary_body = fetch(urls["summary"])
    listed = bool(re.search(rf"<version>{re.escape(version)}</version>", summary_body or ""))
    release = (re.search(r"<release>([^<]*)</release>", summary_body or "") or [None, "NA"])[1]
    latest = (re.search(r"<latest>([^<]*)</latest>", summary_body or "") or [None, "NA"])[1]
    summary = f"release={release} latest={latest} version_listed={listed}"
    errors = _probe_errors((urls["exact"], exact_status, exact_body),
                           (urls["summary"], summary_status, summary_body))
    extra = {"probe_errors": errors, "registry_release": release}
    return exact_status, listed, summary, extra, summary_status


def _pypi_verdict(fetch, urls, version):
    exact_status, exact_body = fetch(urls["exact"])
    summary_status, summary_body = fetch(urls["summary"])  # noqa: F841
    try:
        data = json.loads(summary_body or "{}")
    except json.JSONDecodeError:
        data = {}
    releases = data.get("releases") or {}
    listed = version in releases
    info_version = (data.get("info") or {}).get("version", "NA")
    yanked_reasons = sorted({f.get("yanked_reason") or "yanked"
                             for f in (releases.get(version) or []) if f.get("yanked")})
    if exact_body:
        try:
            per_version = json.loads(exact_body)
        except json.JSONDecodeError:
            per_version = {}
        files = per_version.get("urls") or []
        if files and all(f.get("yanked") for f in files):
            yanked_reasons = sorted({f.get("yanked_reason") or "yanked" for f in files})
    summary = f"info.version={info_version} version_listed={listed}"
    errors = _probe_errors((urls["exact"], exact_status, exact_body),
                           (urls["summary"], summary_status, summary_body))
    extra = {"yanked": bool(yanked_reasons), "yanked_reason": ";".join(yanked_reasons),
             "probe_errors": errors, "registry_release": info_version}
    return exact_status, listed, summary, extra, summary_status


def _goproxy_verdict(fetch, urls, version):
    exact_status, exact_body = fetch(urls["exact"])
    summary_status, summary_body = fetch(urls["summary"])
    entries = [x for x in re.split(r"\s+", (summary_body or "").strip()) if x]
    listed = version in entries or f"v{version}" in entries
    summary_status_l, summary_body_l = fetch(urls["summary"].replace("@v/list", "@latest"))
    latest = "NA"
    try:
        latest = json.loads(summary_body_l or "{}").get("Version", "NA")
    except json.JSONDecodeError:
        pass
    summary = f"@latest={latest} version_listed={listed}"
    errors = _probe_errors((urls["exact"], exact_status, exact_body),
                           (urls["summary"], summary_status, summary_body))
    extra = {"probe_errors": errors, "registry_release": latest}
    return exact_status, listed, summary, extra, summary_status


VERDICT_READERS = {"java": _maven_verdict, "python": _pypi_verdict, "go": _goproxy_verdict}


def _probe_errors(*probes) -> str:
    """Transport failures are HTTP status 0 in this module; keep their text for the log."""
    parts = []
    for url, status, body in probes:
        if status == 0:
            detail = (body or "").strip()[:120] or "no response"
            parts.append(f"{url} -> {detail}")
    return "; ".join(parts)


def check_line(fetch, line: str, module: str, version: str) -> dict:
    """One advertised line, judged from two independent readings."""
    urls = urls_for(line, module, version)
    exact_status, listed, summary, extra, summary_status = VERDICT_READERS[line](fetch, urls, version)
    resolvable = exact_status == 200
    probe_errors = extra.get("probe_errors", "")
    if extra.get("yanked"):
        verdict = "yanked"
        reason = f"all files for this version are yanked ({extra['yanked_reason']})"
    elif exact_status == 0 or summary_status == 0:
        verdict = "unverifiable"
        reason = f"a probe could not be performed, so absence is not claimed: {probe_errors}"
    elif resolvable and not listed:
        verdict = "conflict"          # served, but the unfiltered list does not know it
        reason = "exact URL is 200 but the unfiltered summary does not list the version"
    elif (not resolvable) and listed:
        verdict = "conflict"          # listed, but the exact URL does not resolve
        reason = "the unfiltered summary lists the version but the exact URL is not 200"
    elif resolvable:
        verdict = "available"
        reason = "exact artifact resolves and the summary lists the version"
    else:
        verdict = "unavailable"
        reason = (f"exact artifact is HTTP {exact_status} and the summary does not list "
                  f"the version ({summary})")
    return {
        "line": line,
        "module": module,
        "version": version,
        "coordinate": urls["coordinate"],
        "exact_url": urls["exact"],
        "exact_status": exact_status,
        "summary_status": summary_status,
        "probe_errors": probe_errors,
        "summary_url": urls["summary"],
        "summary": summary,
        "registry_release": extra.get("registry_release", ""),
        "verdict": verdict,
        "reason": reason,
    }


def gate(fetch, module: str, version: str, lines) -> dict:
    """Advertised lines must be available; anything else fails closed.

    Also reports newest_stable: the highest stable version the registries themselves
    name as released for this module. Backfilling an older tag must not take Latest
    while a newer version is already out - the GitHub page can be behind the
    registries by exactly the gap this tool exists to close.
    """
    checks = [check_line(fetch, line, module, version) for line in lines]
    blocking = [c for c in checks if c["verdict"] != "available"]
    reported = []
    for check in checks:
        name = (check.get("registry_release") or "").strip()
        # Only real version strings count: "NA" from an unreadable field must not join
        # the comparison, and a pre-release never sets the floor for a stable slot.
        if re.match(r"^\d+\.\d+", name) and "-" not in name:
            reported.append(name)
    newest = max(reported, key=semver_key) if reported else ""
    return {
        "module": module,
        "version": version,
        "lines": list(lines),
        "ok": not blocking,
        "checks": checks,
        "blocking": [f"{c['line']}:{c['verdict']}" for c in blocking],
        "newest_stable": newest,
        "newest_stable_sources": [f"{c['line']}={c.get('registry_release', '')}" for c in checks],
    }


def plan(info: dict, gate_result: dict, current_latest: str,
         promote_latest: bool, release_exists: bool) -> dict:
    """Decide the gh release invocation. Never writes anything itself."""
    reasons = []
    tag, version, prerelease = info["tag"], info["version"], info["prerelease"]
    if not gate_result["ok"]:
        reasons.append("artifact gate failed for: " + ", ".join(gate_result["blocking"]))
        return {"action": "skip", "prerelease": prerelease, "latest": False,
                "reasons": reasons, "gh_args": []}
    if not info["latest_owner"]:
        reasons.append("not the product line tag: never promoted to Latest (RELEASING.md 3 and 6)")
        latest = False
    elif prerelease:
        reasons.append("pre-release version: never promoted to Latest (RELEASING.md 6)")
        latest = False
    elif not promote_latest:
        reasons.append("backfill default: Latest is left where it is (RELEASING.md 6)")
        latest = False
    else:
        target_key = semver_key(version)
        current = (current_latest or "").strip()
        current_version = version_of(current) if current else ""
        current_key = semver_key(current_version) if current_version else None
        newest = (gate_result.get("newest_stable") or "").strip()
        newest_key = semver_key(newest) if re.match(r"^\d+\.\d+", newest) else None
        # Two floors, two directions:
        #   * the page's current Latest must not be overtaken by an *older* tag;
        #     re-recording the version that already holds the slot is fine.
        #   * the registries' newest stable version blocks anything strictly older,
        #     even when the page has not caught up yet (that gap is the whole point).
        if current_key is not None and target_key < current_key:
            reasons.append(f"refused to move Latest backwards: target {version} is older than "
                           f"the current Latest {current}")
            latest = False
        elif newest_key is not None and target_key < newest_key:
            reasons.append(f"refused to promote an older version: the registries already publish "
                           f"{newest} as their newest stable release")
            latest = False
        else:
            floors = []
            if current:
                floors.append(f"current Latest {current}")
            if newest:
                floors.append(f"registry newest {newest}")
            reasons.append("promotion allowed (" + (", ".join(floors) if floors
                                                    else "no readable Latest or registry version")
                           + ")")
            latest = True
    action = "edit" if release_exists else "create"
    gh_args = ["release", action, tag, "--title", tag]
    if release_exists:
        gh_args += ["--prerelease=" + ("true" if prerelease else "false")]
        if latest:
            gh_args += ["--latest=true"]
        else:
            gh_args += ["--latest=false"]
    else:
        gh_args += ["--verify-tag"]
        if prerelease:
            gh_args += ["--prerelease=true"]
        gh_args += ["--latest=" + ("true" if latest else "false")]
    if not latest and action == "create" and not prerelease:
        reasons.append("Latest stays with the current release")
    return {"action": action, "prerelease": prerelease, "latest": latest,
            "reasons": reasons, "gh_args": gh_args}


def notes_body(info: dict, tag: str, notes_dir: str = "release-notes",
               repo: str = "aliyun/aliyun-odps-openapi-sdk",
               branch: str = "develop") -> dict:
    """Prepared file when present (leading note stripped), placeholder otherwise."""
    path = f"{notes_dir}/{info['flat']}.md"
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        if text.startswith("<!--"):
            _, _, rest = text.partition("-->")
            text = rest.lstrip("\n")
        return {"source": "prepared", "path": path, "body": text}
    log = "catalog-api/CHANGELOG.md" if info["module"] == "catalog" else "common/CHANGELOG.md"
    body = (
        f"## {tag}\n\n"
        "Recorded after the artifact gate confirmed the advertised coordinates resolve.\n\n"
        f"No prepared notes file was found at {path}. Changes are listed in "
        f"[{log}](https://github.com/{repo}/blob/{branch}/{log}).\n"
    )
    return {"source": "generated", "path": "", "body": body}


def _emit(pairs) -> None:
    """Append key=value to GITHUB_OUTPUT when the workflow set one."""
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in pairs:
            handle.write(f"{key}={value}\n")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    p_classify = commands.add_parser("classify")
    p_classify.add_argument("--tag", required=True)

    p_gate = commands.add_parser("gate")
    p_gate.add_argument("--module", required=True, choices=sorted(LINES))
    p_gate.add_argument("--version", required=True)
    p_gate.add_argument("--lines", default="java,python,go")
    p_gate.add_argument("--report-only", action="store_true")

    p_notes = commands.add_parser("notes")
    p_notes.add_argument("--tag", required=True)
    p_notes.add_argument("--notes-dir", default="release-notes")
    p_notes.add_argument("--repo", default="aliyun/aliyun-odps-openapi-sdk")
    p_notes.add_argument("--branch", default="develop")
    p_notes.add_argument("--out", default="")

    p_plan = commands.add_parser("plan")
    p_plan.add_argument("--tag", required=True)
    p_plan.add_argument("--current-latest", default="")
    p_plan.add_argument("--promote-latest", action="store_true")
    p_plan.add_argument("--exists", action="store_true")
    p_plan.add_argument("--gate-json", default="")
    args = parser.parse_args(argv)

    if args.command == "classify":
        info = classify(args.tag)
        print(json.dumps(info))
        _emit([(k, ("true" if isinstance(v, bool) else v)) for k, v in info.items()])
        return 0

    if args.command == "gate":
        lines = [x.strip() for x in args.lines.split(",") if x.strip()]
        result = gate(http_get, args.module, args.version, lines)
        print(json.dumps(result, indent=1))
        for check in result["checks"]:
            print(f"[gate] {check['line']:6s} {check['verdict']:11s} {check['coordinate']} "
                  f"exact={check['exact_status']} {check['summary']} :: {check['reason']}",
                  file=sys.stderr)
        _emit([("gate", "ok" if result["ok"] else "fail"),
               ("blocking", ",".join(result["blocking"]))])
        if args.report_only:
            return 0
        return 0 if result["ok"] else 2

    if args.command == "notes":
        info = classify(args.tag)
        result = notes_body(info, args.tag, args.notes_dir, args.repo, args.branch)
        if args.out:
            with open(args.out, "w", encoding="utf-8") as handle:
                handle.write(result["body"])
        print(json.dumps({"source": result["source"], "path": result["path"],
                          "body_bytes": len(result["body"])}))
        _emit([("notes_source", result["source"])])
        return 0

    if args.command == "plan":
        info = classify(args.tag)
        if args.gate_json:
            with open(args.gate_json, encoding="utf-8") as handle:
                gate_result = json.load(handle)
        else:
            gate_result = {"ok": True, "blocking": []}
        result = plan(info, gate_result, args.current_latest, args.promote_latest, args.exists)
        print(json.dumps(result, indent=1))
        for reason in result["reasons"]:
            print(f"[plan] {reason}", file=sys.stderr)
        _emit([("action", result["action"]),
               ("latest", "true" if result["latest"] else "false"),
               ("gh_args", " ".join(result["gh_args"]))])
        return 0 if result["action"] != "skip" else 3

    return 2


if __name__ == "__main__":
    sys.exit(main())
