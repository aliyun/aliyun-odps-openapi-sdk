# 发行记录（GitHub Releases）流程

> 本文只管一件事：**一个版本发布出去之后，GitHub Releases 页上要不要留一条记录、留成什么样、由谁来写。**
> 制品怎么发到 Maven Central / PyPI / Go module proxy 由 `.github/workflows/` 里已有的
> `catalog-api*.yml` / `common*.yml` 负责，本文不碰制品，也不创建 tag。
>
> 自动化实现拆在另一份改动里（见第 9 节）：本文描述规则，那份才是会写 release 对象的东西。

## 1. 一次发行其实是两个面

| 面 | 载体 | 谁来写 | 本仓现状（2026-11-21 现取，11-24 复核同值） |
| --- | --- | --- | --- |
| 制品 | Maven Central / PyPI / Go module proxy | 各语言线的 publish workflow，tag push 触发 | 0.4.0 三条线齐全（见第 2 节） |
| 记录 | GitHub Releases 页上的 release 对象 | 维护者决定，写入路径见第 5 节 | 只有 2 个对象：`v0.3.0-SNAPSHOT`（2026-02-04）与 `v0.1.1`（2025-04-09） |

记录面缺位的直接后果：`releases/latest` 返回 `v0.3.0-SNAPSHOT`。按 Releases 页判断版本的接入方，会把一个 SNAPSHOT 构建当成最新正式发行，而真正的 0.4.0 只体现在中央仓库里。

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

如果维护者更希望三条线各有记录，正文可以按线拆分，文件名沿用第 8 节的约定即可；但这种情况下必须显式把非主记录的 `--latest` 置为 false，否则 Latest 位取决于谁最后建。`common` 线的记录同样不占 Latest：`com.aliyun.odps:openapi` 的版本号（1.3.x）比 `catalog-api`（0.4.x）大，一旦让它占位，Releases 页的 Latest 就会长期停在公共组件上。

## 4. 写记录之前，先把"这个版本的制品能用"验一遍

**tag 存在不等于制品已发布。** `gh release create --verify-tag` 只核验 tag 在不在，不核验 Maven job 有没有成功；而记录 job 与各线 publish job 由同一次 tag push 并行启动，任何一条线失败时记录照样能写、还能抢占 Latest。

所以对主记录里声明的每个坐标，各取一次精确版本可用性，并且**同时留一条不受该次筛选约束的总结读数**（防止把"我没匹配到"写成"它不存在"）：

| 线 | 精确可用性 | 总结读数 |
| --- | --- | --- |
| Java | `https://repo1.maven.org/maven2/com/aliyun/odps/<artifact>/<ver>/<artifact>-<ver>.jar` 取 200 | 同目录 `maven-metadata.xml` 的 `<latest>` / `<release>` / `<version>` 全集 |
| Python | `https://pypi.org/pypi/<package>/<ver>/json` 取 200 | 同一 JSON 的 `info.version` 与 `releases` 键全集；还要看该版本文件的 `yanked` |
| Go | `https://proxy.golang.org/<module path>/@v/<ver>.info` 取 200 | 同模块 `@v/list` 全集与 `@latest` |

三条都对不上才允许写"这条线还没有制品"。任一声明的坐标取不到 ⇒ 该版本的记录不写，或者正文里把那条线写成"尚未发布"并从声明坐标里去掉。

## 5. 谁来写这条记录：现在只能是维护者授权的 workflow，不是网页

`catalog-api.yml` 与 `common.yml` 的 `on:` 里都挂着**未按 tag 过滤**的 `release: types: [ created ]`（11-24 从 develop 现取原文，两处都只订阅 `created`，没有订阅 `edited`）。后果：**任何人以人工身份新建一个 release 对象——网页点 New release 也好、用人用 token 调 API 也好——都会把这两条 Maven 发布 job 启动起来**，而发布路径本来只应由 tag push 触发。

- 由 GitHub Actions 用内置 `GITHUB_TOKEN` 写 release 对象不会递归触发这两条 job（workflow 之间的链式触发动作会被平台挡掉），所以自动化路径是安全的。
- 只订阅 `created` 也意味着**编辑已有对象不在危险范围内**：改标题、改正文、勾 Pre-release 都不会启动发布 job。危险只在新建那一下。
- 在这两个触发器被删掉或加上 tag 过滤之前，**不要用网页新建记录**。触发器怎么改属发布路径变更，归维护者定，本文不动它。

## 6. Latest 位与补录方向

Latest 只有一个位置，补录旧版本时它会变成方向问题：

- 新版本的记录：可以占 Latest，但要先确认当前 Latest 的稳定版本号确实比它旧。
- 补录旧版本：**默认不提升 Latest**。显式要求提升时，必须拿目标版本与当前 Latest 的版本做比较，更旧就拒绝，不能被一笔补录拨回去。
- 预发布形态（`-SNAPSHOT`、`-rc.1`）永远不占 Latest。判预发布要看版本部分，不是 tag 全名：`catalog-v0.4.0` 里的连字符是线名前缀的一部分，`0.4.0-SNAPSHOT` 里的才是预发布后缀。
- 读当前 Latest 再写 Latest 是"读后改"，两次补录并发就可能互相覆盖。串行化要以**解析后的目标 tag**为键，而"是否提升 Latest"这段还得有一把跨版本共用的锁；用 `github.ref` 做并发组是不够的——人工 dispatch 跑在默认分支 ref 上，和 tag push 的 ref 不是一个键。

## 7. `v0.3.0-SNAPSHOT` 这条现存记录怎么处置

它现在是 `draft=false`、`prerelease=false`，所以占了 Latest 位。两个候选动作：

- **A. 标成 pre-release**（Edit release → 勾 Pre-release）。成本最低，不删任何东西。
- **B. 撤下展示**（删除该 release 对象，tag 保留）。不可逆，且删完 Latest 位会落到 `v0.1.1`（2025-04-09），比现在还旧。

单独用哪个都不解决问题：A 之后 Latest 是 `v0.1.1`，B 之后也是 `v0.1.1`。处置建议是 **A + 补一条 0.4.0 主记录**。

两步的风险不一样，按第 5 节现取的触发器原文分开说：

- **A 是编辑现有对象**（`gh release edit v0.3.0-SNAPSHOT --prerelease=true`），`created` 事件不涉及，随时可做，网页上勾一下也一样安全。
- **补 0.4.0 主记录是新建对象**，会发 `release.created`，因此**在触发器修好之前只能走用内置 `GITHUB_TOKEN` 的 workflow**，不要在网页点 New release，也不要用个人 token 调创建接口。

## 8. 准备件的存放约定

`release-notes/<tag>.md`，tag 里的 `/` 写成 `-`。例如：

- `catalog-v0.4.0` → `release-notes/catalog-v0.4.0.md`
- `common/go/v1.3.2` → `release-notes/common-go-v1.3.2.md`

一份准备件对应一个 tag。正文本身就是 release 记录要用的 Markdown，改的时候顺手把 CHANGELOG 锚点一起对一遍。

放在仓库根目录而不是 `docs/`，是因为 `.gitignore` 最后有一条裸 `docs`（现取 `.gitignore:169`），任何 `docs/` 路径下的文件都不会被跟踪。要改成 `docs/release-notes/`，得先把那条 ignore 的来历查清楚——本稿不动 ignore 规则，以免影响 codegen 输出目录的既有语义。

## 9. 自动化建议稿的状态

第一轮把文档与 workflow 放在同一个 PR 里，评审（2026-11-21）指出自动化那版有三处要先修，本 PR 因此**只保留文档**，workflow 拆到后续 PR：

| 评审点 | 本文的落点 | 自动化侧要做的事 |
| --- | --- | --- |
| 1. 制品未发布也可能显示为正式发行 | 第 4 节 | 记录步骤前先跑逐坐标的制品门禁，取不到就不写；`--verify-tag` 只当 tag 存在性检查，不能替代它 |
| 2. 补录旧版会把 Latest 往回拨；`github.ref` 并发键不能串行化同一目标 | 第 6 节 | 补录默认不提升 Latest；显式提升先比当前 Latest 的稳定版本，更旧就拒绝；写入段用一把跨版本共用的锁（实现选了比"按目标 tag 串行"更粗但更稳的一档：同一时刻只允许一条记录在写） |
| 3. 网页手动新建记录会触发既有 Maven 发布 | 第 5、7 节 | 写入只走内置 `GITHUB_TOKEN` 的 workflow；在触发器修好前文档不推荐网页补录 |

评审还建议在**不写真实 release 对象**的测试里覆盖三种情形：tag 已存在但 Maven 发布失败、某条语言线制品缺失、新版已是 Latest 时重复补录旧版。这三格由后续 PR 的离线自测承担。

## 10. 现取读数（2026-11-21 首取，2026-11-24 复核）

| 项 | 读数 |
| --- | --- |
| Maven `com.aliyun.odps:catalog-api` | `latest=0.4.0`、`release=0.4.0`，`lastUpdated=20260601071716` |
| PyPI `pyodps_catalog` | `0.4.0` 未 yank，上传 2026-06-01T04:51:47Z；`1.0.0` yanked（理由 "Use 0.3.0 instead"） |
| Go module proxy `catalog-api/go` | `@v/list` 只有 `v0.4.0`，`@latest` 指向 `854219e` |
| Maven `com.aliyun.odps:openapi` | `latest=release=1.3.1`，`lastUpdated=20260601050939` |
| PyPI `maxcompute_tea_openapi` | `latest=1.3.1`（`1.3.1` 上传 2026-06-01T04:58:46Z） |
| Go module proxy `common/go` | `v1.3.0`、`v1.3.1`、`v1.3.2`（1.3.2 仅 Go：无 `common-v1.3.2` / `common-py-v1.3.2` tag，Maven/PyPI 最新仍 1.3.1） |
| GitHub tag 总数 | 31 |
| GitHub release 对象 | 2（`v0.3.0-SNAPSHOT` id 282814903、`v0.1.1` id 211200497），`releases/latest` = `v0.3.0-SNAPSHOT` |
| `catalog-api.yml` / `common.yml` 的 `on:` | 均含未按 tag 过滤的 `release: types: [ created ]`（11-24 从 develop 现取） |

一处需要在记录里点名的文档滞后：`catalog-api 0.4.0` 的产物实际依赖 `common 1.3.1`（`catalog-api/java/pom.xml` 与 `catalog-api/go/go.mod` 在 `catalog-v0.4.0` tag 上都是 1.3.1），而 `catalog-api/CHANGELOG.md` 的 0.4.0 小节写的是"升级 `common` 至 v1.3.0"。1.3.0 那次产物缺生成代码（见 `common/CHANGELOG.md` 的 1.3.1 小节），所以记录正文按 1.3.1 写。
