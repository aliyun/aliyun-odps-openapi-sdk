# Changelog

## 0.4.0 (2026-06-01)

### Breaking Changes (HTTP behavior)

- **GET/DELETE 请求不再携带多余的 request body 和 `content-type: application/json` 头。**
  - 此前所有请求（包括 GET、DELETE）均通过 `requestWithModel` 发送，会将一个空的 model 序列化为 JSON body（`{}`），不符合 HTTP 语义规范。
  - 现在 GET 和 body-less POST（如 `:getPolicy`、`:search`）使用 `request()` 函数，仅发送 query 参数，不发送 body。
  - DELETE 和 trigger 类操作使用 `requestVoid()` 函数，不发送 body 也不期望响应体。
  - 写操作（POST create、PUT/PATCH update、setPolicy）保持使用 `requestWithModel()` 不变。

### 影响范围

以下所有接口的 HTTP 请求行为已修正：

**GET 操作（不再发送 body）：**
- `listProjects` / `getProject`
- `listSchemas` / `getSchema`
- `listTables` / `getTable`
- `listPartitions`
- `listConnections` / `getConnection`
- `listRoles` / `getRole`
- `listTaxonomies` / `getTaxonomy`
- `listPolicyTags` / `getPolicyTag`
- `listDataPolicies` / `getDataPolicy`
- `listDataScans` / `getDataScan` / `listDataScanJobs`
- `listModels` / `getModel` / `listModelVersions`

**Body-less POST 操作（不再发送 body）：**
- `getTablePolicy` / `getSchemaPolicy`
- `getConnectionPolicy`
- `getRolePolicy` / `getTaxonomyPolicy` / `getPolicyTagPolicy` / `getDataPolicyPolicy`
- `search`
- `getDataToken`

**DELETE 操作（改用 `requestVoid`）：**
- `deleteTable` / `deleteSchema`
- `deleteConnection`
- `deleteRole`
- `deleteTaxonomy` / `deletePolicyTag` / `deleteDataPolicy`
- `deleteDataScan`
- `deleteModel` / `deleteModelVersion`

**trigger 操作（改用 `requestVoid`）：**
- `triggerDataScan`

### 依赖升级

- 升级 `common` (maxcompute:openapi) 至 v1.3.0，该版本新增了 `request()` 和 `requestVoid()` 函数。

### 备注

- SDK 公开 API 签名未变，客户端代码无需修改。
- 如果下游有基于 HTTP body 进行签名校验或日志解析的中间件/代理，请注意 GET/DELETE 请求的 body 已移除。

---

## 0.3.1 (2025-05-22)

- Initial stable release with full Catalog API coverage.
