<!--
准备件：给 tag `catalog-v0.4.0` 建 GitHub Release 主记录时直接用作正文。
对应发行流程见 RELEASING.md。本文件只是文本准备件，不创建 tag、不发布制品。
-->

# catalog-api 0.4.0

发布日期：2026-06-01（三条语言线同日，同一个 commit `854219e`）

这一版修的是请求语义：GET / DELETE 与不带 body 的 POST 不再携带一个空 JSON body 和多余的 `content-type: application/json`。SDK 对外的方法签名没变，接入方代码不用改。

## 逐线状态（2026-11-21 现取）

| 语言 | 引入方式 | 状态 |
| --- | --- | --- |
| Java | Maven Central `com.aliyun.odps:catalog-api:0.4.0` | 已发布，`maven-metadata.xml` 的 `latest` / `release` 均为 0.4.0 |
| Python | `pip install pyodps_catalog==0.4.0` | 已发布（2026-06-01T04:51:47Z，未 yank） |
| Go | `go get github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go@v0.4.0` | 已索引，module proxy 当前 `@latest` 即 v0.4.0（tag `catalog-api/go/v0.4.0`） |

```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>catalog-api</artifactId>
    <version>0.4.0</version>
</dependency>
```

## 变更内容

- **GET / list 操作不再发送 body**：`listProjects` / `getProject`、`listSchemas` / `getSchema`、`listTables` / `getTable`、`listPartitions`、`listConnections` / `getConnection`、`listRoles` / `getRole`、`listTaxonomies` / `getTaxonomy`、`listPolicyTags` / `getPolicyTag`、`listDataPolicies` / `getDataPolicy`、`listDataScans` / `getDataScan` / `listDataScanJobs`、`listModels` / `getModel` / `listModelVersions`。
- **body-less POST 不再发送 body**：`getTablePolicy` / `getSchemaPolicy`、`getConnectionPolicy`、`getRolePolicy` / `getTaxonomyPolicy` / `getPolicyTagPolicy` / `getDataPolicyPolicy`、`search`、`getDataToken`。
- **DELETE 与 trigger 改用 `requestVoid`**（不发 body，也不期望响应体）：`deleteTable` / `deleteSchema`、`deleteConnection`、`deleteRole`、`deleteTaxonomy` / `deletePolicyTag` / `deleteDataPolicy`、`deleteDataScan`、`deleteModel` / `deleteModelVersion`、`triggerDataScan`。
- **写操作不变**：POST create、PUT/PATCH update、`setPolicy` 仍走 `requestWithModel`。

完整清单与动机见 [catalog-api/CHANGELOG.md 的 0.4.0 小节](https://github.com/aliyun/aliyun-odps-openapi-sdk/blob/catalog-v0.4.0/catalog-api/CHANGELOG.md#040-2026-06-01)。

## 依赖基线

这一版依赖 `common 1.3.1`（`catalog-api/java/pom.xml` 声明 `com.aliyun.odps:openapi:1.3.1`，`catalog-api/go/go.mod` 声明 `common/go v1.3.1`）。1.3.1 补的是 1.3.0 产物缺 `request()` / `requestVoid()` 生成代码的问题，功能与 1.3.0 的设计一致：见 [common/CHANGELOG.md 的 1.3.1 小节](https://github.com/aliyun/aliyun-odps-openapi-sdk/blob/develop/common/CHANGELOG.md#131-2026-06-01)。

> 说明：`catalog-api/CHANGELOG.md` 的 0.4.0 小节把依赖升级写成了 v1.3.0，实际发布产物是 1.3.1，以本条为准。

`common` 侧另有一条：1.3.2 只发到了 Go module proxy（`common/go/v1.3.2`，修复 Go 分页签名导致的 401），Java / Python 线没有 1.3.2。用 catalog-api 0.4.0 的 Go 接入方如果想拿这个分页修复，需要单独把 `common/go` 升到 v1.3.2。

## 升级影响

- 公开 API 签名未变，客户端代码无需修改。
- 如果链路上有按 GET / DELETE 请求 body 做签名校验或日志解析的中间件、代理，需要知会：这些请求现在没有 body 了。
- Go 线需要 Go 1.23 及以上（`go.mod` 声明 `go 1.23.2`）。
- 版本仍在 `0.x`，接口与请求行为可能在次要版本之间调整，生产使用请锁定具体版本。

## 建议的记录设置

- tag：`catalog-v0.4.0`（主记录；`catalog-py-v0.4.0`、`catalog-api/go/v0.4.0` 只留 tag）
- Pre-release：否
- 标记为 Latest：是
