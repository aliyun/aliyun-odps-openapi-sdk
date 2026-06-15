# Changelog

## 1.3.2 (2026-06-15)

### Bug Fix

- **修复 Go SDK 分页签名错误导致的 401。**
  - `common/go` 依赖的 `tea/utils.buildCanonicalString` 在构造待签名串时对 query 值做了 `url.QueryEscape`，而 ODPS 服务端使用原始（解码后）的 query 值重建规范资源，二者不一致。
  - 当服务端返回的 opaque `pageToken` 含 `!` 等保留字符时（例如 `ListTables` 翻页），签名不匹配，第二页请求返回 `401 Unauthorized`。
  - 修复方式：签名串改用原始 query 值（与 Java、Python SDK 行为一致），实际请求 URL 的编码仍由请求层负责。
  - 对应上游修复：`aliyun/aliyun-odps-go-sdk#73`（`tea/v0.1.0`）。
  - 仅影响 Go；Java 与 Python 的签名实现本就使用原始值，不受影响。

---

## 1.3.1 (2026-06-01)

### Bug Fix

- **修复 1.3.0 发布产物缺少生成代码的问题。**
  - 1.3.0 的 tag 仅包含更新后的 `.dara` 源码，但 Java/Go 的生成代码未重新执行 codegen，导致发布到 Maven Central 和 Go module proxy 的产物缺少 `request()` 和 `requestVoid()` 方法。
  - 1.3.1 包含正确的全语言生成代码，功能与 1.3.0 设计一致。

---

## 1.3.0 (2026-06-01)

### New Features

- **新增 `request()` 函数**：无 body 请求，期望 JSON 响应。适用于 GET、list、以及无 body 的 POST（如 `:getPolicy`、`:search`）。
- **新增 `requestVoid()` 函数**：无 body 请求，不期望响应体。适用于 DELETE 和 trigger 类操作。

### 函数职责划分

| 函数 | 发送 body | 期望响应 | 适用场景 |
|------|----------|---------|---------|
| `request` | 否 | JSON | GET、list、body-less POST |
| `requestVoid` | 否 | 无 | DELETE、trigger |
| `requestWithModel` | 是 | JSON | POST create、PUT/PATCH update、setPolicy |

### 备注

- `requestWithModel` 和 `requestWithoutModel` 保留不变，向后兼容。
- 新函数不设置 `content-type` 头，也不序列化 body，符合 HTTP 语义规范。

---

## 1.2.0 (2025-05-29)

- Python 版本统一。

---

## 0.0.4

- Initial release with `requestWithModel` and `requestWithoutModel`.
