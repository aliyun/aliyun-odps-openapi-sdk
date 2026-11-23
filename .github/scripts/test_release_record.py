#!/usr/bin/env python3
"""Offline tests for release_record.py: no network, and no real release object is written.

Covers the cases the review asked for (a tag whose Maven publish failed, one language
line missing its artifact, and backfilling an older version while a newer one already
holds Latest), plus the guards those cases depend on.
"""
import json
import os
import tempfile
import unittest

import release_record as rr

MAVEN = rr.MAVEN_BASE
PYPI = rr.PYPI_BASE
GOPROXY = rr.GOPROXY_BASE
CAT = "com/aliyun/odps/catalog-api"
COM = "com/aliyun/odps/openapi"


def maven_metadata(versions, release, latest=None):
    body = "<metadata><versioning><latest>%s</latest><release>%s</release><versions>" % (
        latest or release, release)
    body += "".join(f"<version>{v}</version>" for v in versions)
    return body + "</versions></versioning></metadata>"


def pypi_package(info_version, releases):
    """releases: {version: [(yanked, reason), ...]}"""
    return json.dumps({
        "info": {"version": info_version},
        "releases": {v: [{"yanked": y, "yanked_reason": r} for y, r in files]
                     for v, files in releases.items()},
    })


def pypi_version(files):
    return json.dumps({"urls": [{"yanked": y, "yanked_reason": r} for y, r in files]})


def goproxy_list(*versions):
    return "\n".join(versions)


class Fetch:
    """Stubbed reader: unknown URL -> 404, so a missing fixture is a missing artifact."""

    def __init__(self, pages):
        self.pages = dict(pages)

    def __call__(self, url, timeout=30):
        if url not in self.pages:
            return 404, ""
        return 200, self.pages[url]


def all_catalog_040():
    return {
        f"{MAVEN}/{CAT}/0.4.0/catalog-api-0.4.0.jar": "",
        f"{MAVEN}/{CAT}/maven-metadata.xml": maven_metadata(["0.3.1", "0.4.0"], "0.4.0"),
        f"{PYPI}/pyodps_catalog/0.4.0/json": pypi_version([(False, None)]),
        f"{PYPI}/pyodps_catalog/json": pypi_package("0.4.0",
                                                    {"0.4.0": [(False, None)],
                                                     "1.0.0": [(True, "Use 0.3.0 instead")]}),
        f"{GOPROXY}/github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/@v/v0.4.0.info": "",
        f"{GOPROXY}/github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/@v/list": goproxy_list("v0.4.0"),
    }


class Classify(unittest.TestCase):
    def test_line_prefix_hyphen_is_not_a_prerelease(self):
        info = rr.classify("catalog-v0.4.0")
        self.assertEqual((info["module"], info["line"], info["version"]), ("catalog", "java", "0.4.0"))
        self.assertFalse(info["prerelease"])
        self.assertTrue(info["primary"])

    def test_snapshot_suffix_is_a_prerelease(self):
        info = rr.classify("catalog-v0.5.0-SNAPSHOT")
        self.assertTrue(info["prerelease"])
        self.assertEqual(info["version"], "0.5.0-SNAPSHOT")

    def test_submodule_tags_are_not_carriers(self):
        for tag in ("catalog-api/go/v0.4.0", "common-py-v1.3.1", "catalog-py-v0.4.0"):
            info = rr.classify(tag)
            self.assertFalse(info["primary"], tag)
            self.assertFalse(info["latest_owner"], tag)

    def test_common_java_tag_carries_its_module_but_not_latest(self):
        info = rr.classify("common-v1.3.1")
        self.assertTrue(info["primary"])
        self.assertFalse(info["latest_owner"])

    def test_legacy_unprefixed_tag_is_rejected(self):
        # The historical v0.3.0-SNAPSHOT record is handled by an explicit gh release edit,
        # not by this tooling; classifying it must fail loudly rather than guess a line.
        with self.assertRaises(ValueError):
            rr.classify("v0.3.0-SNAPSHOT")

    def test_version_of_reads_legacy_tags(self):
        self.assertEqual(rr.version_of("v0.3.0-SNAPSHOT"), "0.3.0-SNAPSHOT")
        self.assertEqual(rr.version_of("catalog-v0.4.0"), "0.4.0")


class BrokenFetch(Fetch):
    """Transport failure for a set of URLs: HTTP status 0, as release_record.http_get reports."""

    def __init__(self, pages, broken):
        super().__init__(pages)
        self.broken = set(broken)

    def __call__(self, url, timeout=30):
        if url in self.broken:
            return 0, "transport-error: Failed to connect to host"
        return super().__call__(url, timeout)


class Gate(unittest.TestCase):
    def test_all_three_lines_available(self):
        result = rr.gate(Fetch(all_catalog_040()), "catalog", "0.4.0", ["java", "python", "go"])
        self.assertTrue(result["ok"], result["blocking"])

    def test_tag_exists_but_maven_publish_failed(self):
        pages = all_catalog_040()
        pages.pop(f"{MAVEN}/{CAT}/0.4.0/catalog-api-0.4.0.jar")
        pages[f"{MAVEN}/{CAT}/maven-metadata.xml"] = maven_metadata(["0.3.1"], "0.3.1")
        result = rr.gate(Fetch(pages), "catalog", "0.4.0", ["java", "python", "go"])
        self.assertFalse(result["ok"])
        self.assertEqual(result["blocking"], ["java:unavailable"])
        java = [c for c in result["checks"] if c["line"] == "java"][0]
        # two independent readings are recorded before the negative verdict
        self.assertEqual(java["exact_status"], 404)
        self.assertIn("release=0.3.1", java["summary"])

    def test_one_language_line_missing(self):
        pages = all_catalog_040()
        pages.pop(f"{PYPI}/pyodps_catalog/0.4.0/json")
        pages[f"{PYPI}/pyodps_catalog/json"] = pypi_package("0.3.1", {"0.3.1": [(False, None)]})
        result = rr.gate(Fetch(pages), "catalog", "0.4.0", ["java", "python", "go"])
        self.assertFalse(result["ok"])
        self.assertEqual(result["blocking"], ["python:unavailable"])
        self.assertEqual([c["verdict"] for c in result["checks"]], ["available", "unavailable", "available"])

    def test_conflict_is_not_reported_as_missing(self):
        pages = all_catalog_040()
        pages.pop(f"{GOPROXY}/github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/@v/v0.4.0.info")
        result = rr.gate(Fetch(pages), "catalog", "0.4.0", ["java", "python", "go"])
        self.assertFalse(result["ok"])
        self.assertEqual(result["blocking"], ["go:conflict"])
        go = [c for c in result["checks"] if c["line"] == "go"][0]
        self.assertIn("unfiltered summary lists the version", go["reason"])

    def test_yanked_version_is_not_advertisable(self):
        pages = all_catalog_040()
        pages[f"{PYPI}/pyodps_catalog/0.4.0/json"] = pypi_version([(True, "Use 0.3.0 instead")])
        result = rr.gate(Fetch(pages), "catalog", "0.4.0", ["java", "python", "go"])
        self.assertFalse(result["ok"])
        self.assertEqual(result["blocking"], ["python:yanked"])

    def test_common_1_3_2_is_go_only(self):
        # Maven/PyPI never published 1.3.2, so a common-v1.3.2 record must be refused
        # while a Go-only probe would pass.
        pages = {
            f"{GOPROXY}/github.com/aliyun/aliyun-odps-openapi-sdk/common/go/@v/v1.3.2.info": "",
            f"{GOPROXY}/github.com/aliyun/aliyun-odps-openapi-sdk/common/go/@v/list": goproxy_list("v1.3.0", "v1.3.1", "v1.3.2"),
            f"{MAVEN}/{COM}/maven-metadata.xml": maven_metadata(["1.3.0", "1.3.1"], "1.3.1"),
            f"{PYPI}/maxcompute_tea_openapi/json": pypi_package("1.3.1", {"1.3.1": [(False, None)]}),
        }
        full = rr.gate(Fetch(pages), "common", "1.3.2", ["java", "python", "go"])
        self.assertEqual(full["blocking"], ["java:unavailable", "python:unavailable"])
        go_only = rr.gate(Fetch(pages), "common", "1.3.2", ["go"])
        self.assertTrue(go_only["ok"])


    def test_probe_failure_is_not_reported_as_missing(self):
        # The case this box actually hits today: proxy.golang.org is unreachable.
        broken = [f"{GOPROXY}/github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/@v/v0.4.0.info"]
        result = rr.gate(BrokenFetch(all_catalog_040(), broken), "catalog", "0.4.0",
                         ["java", "python", "go"])
        self.assertFalse(result["ok"])
        self.assertEqual(result["blocking"], ["go:unverifiable"])
        go = [c for c in result["checks"] if c["line"] == "go"][0]
        self.assertEqual(go["verdict"], "unverifiable")
        self.assertIn("probe could not be performed", go["reason"])
        self.assertNotIn("not published", go["reason"])
        self.assertIn("version_listed=True", go["summary"])   # the summary reading survives

    def test_summary_probe_failure_also_blocks(self):
        broken = [f"{MAVEN}/{CAT}/maven-metadata.xml"]
        result = rr.gate(BrokenFetch(all_catalog_040(), broken), "catalog", "0.4.0", ["java"])
        self.assertFalse(result["ok"])
        self.assertEqual(result["blocking"], ["java:unverifiable"])

    def test_unavailable_always_carries_both_readings(self):
        pages = all_catalog_040()
        pages.pop(f"{MAVEN}/{CAT}/0.4.0/catalog-api-0.4.0.jar")
        pages[f"{MAVEN}/{CAT}/maven-metadata.xml"] = maven_metadata(["0.3.1"], "0.3.1")
        java = rr.check_line(Fetch(pages), "java", "catalog", "0.4.0")
        self.assertEqual(java["verdict"], "unavailable")
        self.assertEqual(java["exact_status"], 404)          # a real HTTP answer
        self.assertIn("version_listed=False", java["summary"])  # plus the unfiltered list


class Plan(unittest.TestCase):
    def setUp(self):
        self.ok_gate = {"ok": True, "blocking": []}
        self.bad_gate = {"ok": False, "blocking": ["java:unavailable"]}

    def test_gate_failure_writes_nothing(self):
        result = rr.plan(rr.classify("catalog-v0.4.0"), self.bad_gate, "v0.3.0-SNAPSHOT", True, False)
        self.assertEqual(result["action"], "skip")
        self.assertEqual(result["gh_args"], [])
        self.assertIn("artifact gate failed", " ".join(result["reasons"]))

    def test_newer_version_may_take_latest(self):
        result = rr.plan(rr.classify("catalog-v0.4.0"), self.ok_gate, "v0.3.0-SNAPSHOT", True, False)
        self.assertTrue(result["latest"])
        self.assertIn("--latest=true", result["gh_args"])
        self.assertIn("--verify-tag", result["gh_args"])

    def test_backfill_does_not_move_latest_backwards(self):
        result = rr.plan(rr.classify("catalog-v0.3.1"), self.ok_gate, "catalog-v0.4.0", True, False)
        self.assertFalse(result["latest"])
        self.assertIn("--latest=false", result["gh_args"])
        self.assertTrue(any("backwards" in reason for reason in result["reasons"]))

    def test_backfill_default_never_promotes(self):
        result = rr.plan(rr.classify("catalog-v0.3.1"), self.ok_gate, "catalog-v0.4.0", False, True)
        self.assertFalse(result["latest"])
        self.assertEqual(result["action"], "edit")
        self.assertTrue(any("backfill default" in reason for reason in result["reasons"]))

    def test_prerelease_never_promotes(self):
        result = rr.plan(rr.classify("catalog-v0.5.0-SNAPSHOT"), self.ok_gate, "v0.3.0-SNAPSHOT", True, False)
        self.assertFalse(result["latest"])
        self.assertIn("--prerelease=true", result["gh_args"])

    def test_non_primary_tag_never_promotes(self):
        result = rr.plan(rr.classify("common-v1.3.1"), self.ok_gate, "catalog-v0.4.0", True, False)
        self.assertFalse(result["latest"])
        self.assertTrue(any("not the product line" in reason for reason in result["reasons"]))

    def test_existing_release_uses_edit(self):
        result = rr.plan(rr.classify("catalog-v0.4.0"), self.ok_gate, "v0.1.1", True, True)
        self.assertEqual(result["action"], "edit")
        self.assertNotIn("--verify-tag", result["gh_args"])
        self.assertIn("--prerelease=false", result["gh_args"])


    def test_stale_page_latest_still_blocks_backfill_via_registry(self):
        # The live case from 11-24: GitHub still calls v0.3.0-SNAPSHOT the Latest while
        # the registries report 0.4.0 as released. Backfilling 0.3.1 must not win.
        pages = all_catalog_040()
        pages[f"{MAVEN}/{CAT}/0.3.1/catalog-api-0.3.1.jar"] = ""
        pages[f"{PYPI}/pyodps_catalog/0.3.1/json"] = pypi_version([(False, None)])
        pages[f"{PYPI}/pyodps_catalog/json"] = pypi_package(
            "0.4.0", {"0.3.1": [(False, None)], "0.4.0": [(False, None)]})
        pages[f"{GOPROXY}/github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/@v/v0.3.1.info"] = ""
        pages[f"{GOPROXY}/github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/@v/list"] = goproxy_list("v0.3.1", "v0.4.0")
        gate_031 = rr.gate(Fetch(pages), "catalog", "0.3.1", ["java", "python", "go"])
        self.assertTrue(gate_031["ok"], gate_031["blocking"])
        self.assertEqual(gate_031["newest_stable"], "0.4.0")
        result = rr.plan(rr.classify("catalog-v0.3.1"), gate_031, "v0.3.0-SNAPSHOT", True, False)
        self.assertFalse(result["latest"])
        self.assertIn("--latest=false", result["gh_args"])
        self.assertTrue(any("registries already publish 0.4.0" in reason for reason in result["reasons"]))

    def test_recording_the_newest_published_version_promotes(self):
        # The 0.4.0 case itself: the target equals the registry's newest stable and is
        # newer than the stale SNAPSHOT holding the slot, so it must take Latest.
        gate_040 = {"ok": True, "blocking": [], "newest_stable": "0.4.0"}
        result = rr.plan(rr.classify("catalog-v0.4.0"), gate_040, "v0.3.0-SNAPSHOT", True, False)
        self.assertTrue(result["latest"])
        self.assertIn("--latest=true", result["gh_args"])
        self.assertTrue(any("promotion allowed" in reason for reason in result["reasons"]))

    def test_rerecording_the_version_that_holds_latest_is_allowed(self):
        gate_040 = {"ok": True, "blocking": [], "newest_stable": "0.4.0"}
        result = rr.plan(rr.classify("catalog-v0.4.0"), gate_040, "catalog-v0.4.0", True, True)
        self.assertTrue(result["latest"])
        self.assertEqual(result["action"], "edit")

    def test_unreadable_registry_field_does_not_set_a_floor(self):
        pages = all_catalog_040()
        gate_result = rr.gate(Fetch(pages), "catalog", "0.4.0", ["go"])
        # proxy @latest is absent from the fixture, so the go line reports NA
        self.assertEqual(gate_result["checks"][0]["registry_release"], "NA")
        self.assertEqual(gate_result["newest_stable"], "")


class Notes(unittest.TestCase):
    def test_prepared_file_is_used_and_header_stripped(self):
        with tempfile.TemporaryDirectory() as td:
            path = os.path.join(td, "catalog-v0.4.0.md")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("<!--\npreparation note\n-->\n\n# catalog-api 0.4.0\nbody\n")
            result = rr.notes_body(rr.classify("catalog-v0.4.0"), "catalog-v0.4.0", td)
            self.assertEqual(result["source"], "prepared")
            self.assertTrue(result["body"].startswith("# catalog-api 0.4.0"))
            self.assertNotIn("preparation note", result["body"])

    def test_placeholder_links_the_right_changelog(self):
        with tempfile.TemporaryDirectory() as td:
            catalog = rr.notes_body(rr.classify("catalog-v0.9.9"), "catalog-v0.9.9", td)
            common = rr.notes_body(rr.classify("common-v1.9.9"), "common-v1.9.9", td)
            self.assertEqual(catalog["source"], "generated")
            self.assertIn("catalog-api/CHANGELOG.md", catalog["body"])
            self.assertIn("common/CHANGELOG.md", common["body"])
            self.assertNotIn("release-notes/", common["body"] + catalog["body"])


if __name__ == "__main__":
    unittest.main()
