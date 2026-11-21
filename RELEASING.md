# 发行记录（GitHub Releases）流程

> 本文只管一件事：**一个版本发布出去之后，GitHub Releases 页上要不要留一条记录、留成什么样。**
> 制品怎么发到 Maven Central / PyPI / Go module proxy 由 `.github/workflows/` 里已有的
> `catalog-api*.yml` / `common*.yml` 负责，本文和随附的建议稿都不碰制品，也不创建 tag。

## 1. 一次发行其实是两个面

| 面 | 载体 | 谁来写 | 本仓现状（2026-11-21 现取） |
| --- | --- | --- | --- |
| 制品 | Maven Central / PyPI / Go module proxy | 各语言线的 publish workflow，tag push 触发 | 0.4.0 三条线齐全（见下表） |
| 记录 | GitHub Releases 页上的 release 对象 | 维护者手动建，或由本文附的建议稿自动补 | 只有 2 个对象：`v0.3.0-SNAPSHOT`（2026-02-04）与 `v0.1.1`（2025-04-09） |

记录面缺位的直接后果：`releases/latest` 现在返回 `v0.3.0-SNAPSHOT`。按 Releases 页判断版本的接入方，会把一个 SNAPSHOT 构建当成最新正式发行，而真正的 0.4.0 只体现在中央仓库里。

## 2. tag → 语言线 → 制品坐标

一个版本的三条线共用同一个 commit（0.4.0 是 `854219e`，2026-06-01T04:57:55Z），但各自有独立的 tag 名，因为 module 路径不同：

| tag 形态 | 语言线 | 制品坐标 | 触发的 publish workflow |
| --- | --- | --- | --- |
| `catalog-v*` | Java | Maven Central `com.aliyun.odps:catalog-api` | `catalog-api.yml` |
| `catalog-py-v*` | Python | PyPI `pyodps_catalog` | `catalog-api-python.yml` |
| `catalog-api/go/v*` | Go | `github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go` | `catalog-api-go.yml`（只校验构建，由 module proxy 索引） |
| `common-v*` | Java | Maven Central `com.aliyun.odps:openapi` | `common.yml` |
| `common-py-v*` | Python | PyPI `maxcompute_tea_openapi` | `common-python.yml` |
| `common/go/v*` | Go | `github.com/aliyun/aliyun-odps-openapi-sdk/common/go` | `common-go.yml`（同上） |

## 3. 一条主记录，而不是三条

一个 release 对象只能绑一个 tag。同一个版本的三条线如果各建一条记录，Latest 位会在三条线之间反复跳，正文也得维护三份。

**建议形态：以 Java 线的 tag（`catalog-v<ver>` / `common-v<ver>`）作为该版本的主记录**，正文里逐线列出引入方式与制品状态（见 `release-notes/catalog-v0.4.0.md` 这份准备件）。其余两条线只保留 tag，不建记录。

如果维护者更希望三条线各有记录，正文可以按线拆分，文件名沿用第 6 节的约定即可；但这种情况下必须显式把非主记录的 `--latest` 置为 false，否则 Latest 位取决于谁最后建。`common` 线的记录同样不占 Latest：`com.aliyun.odps:openapi` 的版本号（1.3.x）比 `catalog-api`（0.4.x）大，一旦让它占位，Releases 页的 Latest 就会长期停在公共组件上。

## 4. 建记录时带上这些（给维护者的清单）

1. 标题 = tag 名；正文取 `release-notes/<tag>.md`，没有准备件就手写并指向 CHANGELOG 锚点：
   - `catalog-api/CHANGELOG.md` 的 `0.4.0 (2026-06-01)` 小节
   - `common/CHANGELOG.md` 的 `1.3.1` / `1.3.2` 小节
2. 逐线写清"已发布 / 未发布"，不要假定三条线总是一起发。现取的例子：`common` 的 1.3.2 只在 Go module proxy 上（`common/go/v1.3.2`），Maven `com.aliyun.odps:openapi` 与 PyPI `maxcompute_tea_openapi` 最新仍是 1.3.1，仓库里也没有 `common-v1.3.2` / `common-py-v1.3.2` 这两个 tag。
3. 预发布形态的 tag（带 `-SNAPSHOT`、`-rc.1` 这一类后缀）建记录时勾 pre-release，并且不要占 Latest 位。
4. 已被 yank 的制品不要建记录。PyPI 上的 `pyodps_catalog 1.0.0`（2025-09-17 上传）现在是 yanked 状态，理由是 "Use 0.3.0 instead"；给它建一条 release 只会多一个误导入口。
5. 记录只追加，不改历史：本流程和随附 workflow 都不创建 tag、不重发制品。

## 5. `v0.3.0-SNAPSHOT` 这条现存记录怎么处置

它现在是 `draft=false`、`prerelease=false`，所以占了 Releases 页的 Latest 位。两个候选动作，都由维护者执行：

- **A. 标成 pre-release**（Edit release → 勾 Pre-release）。成本最低，不删任何东西。
- **B. 撤下展示**（删除该 release 对象，tag 保留）。不可逆，且删完 Latest 位会落到 `v0.1.1`（2025-04-09），比现在还旧。

单独用哪个都不解决问题：A 之后 Latest 是 `v0.1.1`，B 之后也是 `v0.1.1`。所以处置建议是 **A + 补一条 0.4.0 主记录**，让 Latest 落到真正的最新版本上。

## 6. 准备件的存放约定

`release-notes/<tag>.md`，tag 里的 `/` 写成 `-`。例如：

- `catalog-v0.4.0` → `release-notes/catalog-v0.4.0.md`
- `common/go/v1.3.2` → `release-notes/common-go-v1.3.2.md`

一份准备件对应一个 tag。正文本身就是 release 记录要用的 Markdown，改的时候顺手把 CHANGELOG 锚点一起对一遍。

放在仓库根目录而不是 `docs/`，是因为 `.gitignore` 最后有一条裸 `docs`（现取 `.gitignore:169`），任何 `docs/` 路径下的文件都不会被跟踪。要改成 `docs/release-notes/`，得先把那条 ignore 的来历查清楚——本稿不动 ignore 规则，以免影响 codegen 输出目录的既有语义。

## 7. 自动化建议稿

`.github/workflows/release-record.yml` 是本仓的**建议稿**，行为边界：

- 触发面收窄到两条主记录 tag：push `catalog-v*` / `common-v*`。同版本的 Python / Go tag 不会重复建记录（第 3 节）；真要三条线各一条，把 pattern 加回去并保持非主记录 `--latest=false`。
- 已经发出去的版本不会被 push 事件追认，所以另开了 `workflow_dispatch` 入口：填一个已存在的 tag 就能补记录，第 4 节的清单和 `release-notes/` 的准备件就是为这条路径准备的。
- 预发布判定看版本部分而不是 tag 全名：`catalog-v0.4.0` 里的连字符是线名前缀的一部分，`0.4.0-SNAPSHOT` 里的才是预发布后缀；workflow 先剥线名再判。
- 只做"建/更新 release 记录"这一件事，正文优先取第 6 节约定的准备件（准备件开头那段 `<!-- -->` 说明会被剥掉再上传），取不到就退化成一段带 CHANGELOG 链接的占位说明。
- 预发布 tag 自动 `prerelease=true` 且不占 Latest；只有 `catalog-v*` 的非预发布 tag 占 Latest，`common-v*` 不抢，避免 Latest 位在主产品线和公共组件线之间来回跳。
- 重复运行走 `gh release edit` 而不是报错，因此可以安全重跑；`--verify-tag` 保证 tag 不存在时不会凭空建记录。
- 只需要内置的 `GITHUB_TOKEN`（`contents: write`），不需要新增任何 secret，也不会触发制品发布。

合入即生效。如果希望先试运行，可以把 workflow 文件留在分支上，维护者用 `gh release create` 按第 4 节手工补历史版本的记录。

## 8. 现取读数（2026-11-21，全部来自公开接口）

| 项 | 读数 |
| --- | --- |
| Maven `com.aliyun.odps:catalog-api` | `latest=0.4.0`、`release=0.4.0`，`lastUpdated=20260601071716` |
| PyPI `pyodps_catalog` | `0.4.0` 未 yank，上传 2026-06-01T04:51:47Z；`1.0.0` yanked |
| Go module proxy `catalog-api/go` | `@v/list` 只有 `v0.4.0`，`@latest` 指向 `854219e` |
| Maven `com.aliyun.odps:openapi` | `latest=release=1.3.1`，`lastUpdated=20260601050939` |
| PyPI `maxcompute_tea_openapi` | `latest=1.3.1`（`1.3.1` 上传 2026-06-01T04:58:46Z） |
| Go module proxy `common/go` | `v1.3.0`、`v1.3.1`、`v1.3.2` |
| GitHub tag 总数 | 31 |
| GitHub release 对象 | 2（`v0.3.0-SNAPSHOT`、`v0.1.1`），`releases/latest` = `v0.3.0-SNAPSHOT` |

一处需要在记录里点名的文档滞后：`catalog-api 0.4.0` 的产物实际依赖 `common 1.3.1`（`catalog-api/java/pom.xml` 与 `catalog-api/go/go.mod` 在 `catalog-v0.4.0` tag 上都是 1.3.1），而 `catalog-api/CHANGELOG.md` 的 0.4.0 小节写的是"升级 `common` 至 v1.3.0"。1.3.0 那次产物缺生成代码（见 `common/CHANGELOG.md` 的 1.3.1 小节），所以记录正文按 1.3.1 写。
