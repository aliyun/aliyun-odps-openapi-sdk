# MaxCompute CatalogAPI → darabonba 代码生成与命名规范

本项目用于将 **可读的 OpenAPI 风格接口描述文本** 自动转换为 **darabonba 代码**（实体 + 方法），生成规则如下。

---

## 1. 模型（model）生成规则

### 1.1 字段定义
- 所有字段都必须定义为**可选**（`?:`）
- `name='xxx'` 属性与原字段名保持一致
- 保留中文 `description` 注释
- 如果示例值为字符串，设置 `example='xxx'`
- 如果示例值为空字符串，可设置 `example=''`
- 如果示例值为空数组或空 map，不写 `example`
- 不单独为 enum 创建类型，用 `string` 代替
- 类型映射：
  - `string` → `string`
  - `int32` → `int32`
  - `int64` → `string` 并加注释（毫秒时间戳等）
  - `boolean` → `boolean`
  - `array` → `[Type]`
  - `map<string,string>` → `map[string]string`
  - `object(Type)` → `Type`

### 1.2 示例

可读文本：
```
etag	string
用于 read-modify-write 一致性校验
name	string
projects/{projectId}/schemas/{schemaName}/tables/{tableName}
仅输出。
projectId	string
必须：表所属的 project ID。
```

生成：
```ts
model Table {
  etag?: string(name='etag', description='用于 read-modify-write 一致性校验。', example=''),
  name?: string(name='name', description='表的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/tables/{tableName}', example=''),
  projectId?: string(name='projectId', description='表所属的 project ID。', example='')
}
```

---

## 2. 方法（function）生成规则

### 2.1 基本原则
- 方法名遵循**命名规范**（见第 4 节）
- 路径前缀固定为：
  ```
  /api/catalog/v1alpha/
  ```
- 统一使用已有工具方法：
  - **request**：无 body 请求，期望 JSON 响应。用于 `GET`、`list`、以及无 body 的 `POST`（如 `:getPolicy`、`:search`）
  - **requestVoid**：无 body 请求，不期望响应体。用于 `DELETE`、trigger 类操作
  - **requestWithModel**：有 body 请求（model 序列化为 JSON），期望 JSON 响应。用于 `POST` 创建、`PUT`/`PATCH` 更新、`setPolicy`
- 可复用已有 `<resource>Path` 辅助函数生成路径

### 2.2 query 参数处理
- 判断非空使用：
  ```ts
  if (!Util.isUnset(param)) { ... }
  ```
- 将数字、布尔转换为字符串时，使用：
  ```ts
  McUtil.toString(value)
  ```

### 2.3 参数传递
- Path 参数显式列在方法签名中
- 查询参数统一使用：
  ```ts
  var query: map[string]string = {};
  ```
- 可选参数仅在不为空时添加到 `query`

### 2.4 示例

#### 示例 A: GET 方法
可读文本：
```
projects.schemas.tables.get
HTTP request
GET {name=projects/*/schemas/*/tables/*}
Path parameters
name	string
projects/{PROJECT_ID}/schemas/{SCHEMA_NAME}/tables/{TABLE_NAME}
Response body: Table
```

生成：
```ts
async function getTable(table: Table): Table {
  var runtime = new Util.RuntimeOptions{};
  return request('GET', getTablePath(table), null, runtime);
}

function getTablePath(table: Table): string {
  if(Util.isUnset(table.schemaName)) {
    return `/api/catalog/v1alpha/projects/${table.projectId}/schemas/default/tables/${table.tableName}`;
  } else {
    return `/api/catalog/v1alpha/projects/${table.projectId}/schemas/${table.schemaName}/tables/${table.tableName}`;
  }
}
```

#### 示例 B: POST 动作方法（无 body 的读操作）
可读文本：
```
projects.schemas.tables.getPolicy
HTTP request
POST {name=projects/*/schemas/*/tables/*}:getPolicy
Response: Policy
```

生成：
```ts
async function getTablePolicy(table: Table): Policy {
  var runtime = new Util.RuntimeOptions{};
  var path = `${getTablePath(table)}:getPolicy`;
  var query : map[string]string = {};
  return request('POST', path, query, runtime);
}
```

#### 示例 C: DELETE
```ts
async function deleteDataPolicy(namespace: string, dataPolicyName: string): HttpResponse {
  var runtime = new Util.RuntimeOptions{};
  var path = getDataPolicyPath(namespace, dataPolicyName);
  return requestVoid('DELETE', path, null, runtime);
}
```

---

## 3. 路径辅助函数规则

- 命名格式：
  ```
  get<Resource>Path
  get<ResourcePlural>Path
  ```
- Path 中的参数保持与真实路径大小写一致
- 示例：
```ts
function getConnectionPath(namespace: string, connectionName: string): string {
  return `/api/catalog/v1alpha/namespaces/${namespace}/connections/${connectionName}`;
}
```

---

## 4. 函数命名规范

### 4.1 CRUD 资源
- 创建：`createX`
- 获取单个：`getX`
- 获取列表：`listXs`（必须复数）
- 更新：`updateX`（统一用 update，不混用 patch）
- 删除：`deleteX`

### 4.2 子资源
- 获取：`getX<SubResource>`
- 更新：`updateX<SubResource>`
- 设置（替换）：`setX<SubResource>`（仅当明确是替换）
- 列表：`listX<SubResources>`
- 创建：`createX<SubResource>`
- 删除：`deleteX<SubResource>`

### 4.3 任务/动作
- 触发一次性任务：`triggerX`
- 启动长任务：`startX`
- 停止长任务：`stopX`

### 4.4 路径构造函数
- `get<Resource>Path`
- `get<ResourcePlural>Path`
- 避免 `getParentPath` 这种模糊命名

---

## 5. 其他注意事项
1. `enum` 类型直接用 `string` 表示，不用单独定义类型
2. Model 中的所有参数**都是可选**（使用 `?:`）
3. 时间戳字段使用 `string` 类型，并在 `description` 中标明毫秒或秒
4. 分页参数命名统一为：`pageSize` / `pageToken`
5. 所有 query 参数检查 `!Util.isUnset(param)` 后再加入
6. 所有需要转换为字符串的值通过 `McUtil.toString` 完成
7. DELETE 请求使用 `requestVoid`，不传 model

---

**该规范文件需被 claude-code 严格遵循，在从可读接口描述文本生成 darabonba 代码时，保证模型、方法、路径和命名规则的统一性。**
