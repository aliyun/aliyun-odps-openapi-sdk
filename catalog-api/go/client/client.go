// This file is auto-generated, don't edit it. Thanks.
package client

import (
  openapi  "github.com/aliyun/aliyun-odps-openapi-sdk/common/go/client"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  mcutil  "github.com/aliyun/aliyun-odps-go-sdk/tea/utils"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// ==================================== Common ====================================
type HttpResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *string `json:"body,omitempty" xml:"body,omitempty"`
}

func (s HttpResponse) String() string {
  return tea.Prettify(s)
}

func (s HttpResponse) GoString() string {
  return s.String()
}

func (s *HttpResponse) SetHeaders(v map[string]*string) *HttpResponse {
  s.Headers = v
  return s
}

func (s *HttpResponse) SetStatusCode(v int32) *HttpResponse {
  s.StatusCode = &v
  return s
}

func (s *HttpResponse) SetBody(v string) *HttpResponse {
  s.Body = &v
  return s
}

type Policy struct {
  Etag *string `json:"etag,omitempty" xml:"etag,omitempty"`
  Bindings []*Binding `json:"bindings,omitempty" xml:"bindings,omitempty" type:"Repeated"`
}

func (s Policy) String() string {
  return tea.Prettify(s)
}

func (s Policy) GoString() string {
  return s.String()
}

func (s *Policy) SetEtag(v string) *Policy {
  s.Etag = &v
  return s
}

func (s *Policy) SetBindings(v []*Binding) *Policy {
  s.Bindings = v
  return s
}

type Binding struct {
  Role *string `json:"role,omitempty" xml:"role,omitempty"`
  Members []*string `json:"members,omitempty" xml:"members,omitempty" type:"Repeated"`
}

func (s Binding) String() string {
  return tea.Prettify(s)
}

func (s Binding) GoString() string {
  return s.String()
}

func (s *Binding) SetRole(v string) *Binding {
  s.Role = &v
  return s
}

func (s *Binding) SetMembers(v []*string) *Binding {
  s.Members = v
  return s
}

type SetPolicyRequest struct {
  // 设置的 Policy。
  Policy *Policy `json:"policy,omitempty" xml:"policy,omitempty"`
}

func (s SetPolicyRequest) String() string {
  return tea.Prettify(s)
}

func (s SetPolicyRequest) GoString() string {
  return s.String()
}

func (s *SetPolicyRequest) SetPolicy(v *Policy) *SetPolicyRequest {
  s.Policy = v
  return s
}

// Description:
// 
// ==================================== Table ====================================
type TableFieldSchema struct {
  // 列名（如果是顶层列），或者 struct 字段名。
  FieldName *string `json:"fieldName,omitempty" xml:"fieldName,omitempty"`
  // 在 SQL DDL 语句中填写的表示列类型的字符串定义。
  SqlTypeDefinition *string `json:"sqlTypeDefinition,omitempty" xml:"sqlTypeDefinition,omitempty"`
  // 字段类型。
  TypeCategory *string `json:"typeCategory,omitempty" xml:"typeCategory,omitempty"`
  // REQUIRED 或 NULLABLE。
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  // 如果是 STRUCT 类型，表示 STRUCT 的子字段。
  Fields []*TableFieldSchema `json:"fields,omitempty" xml:"fields,omitempty" type:"Repeated"`
  // 列的评论。
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 可选。列绑定的 policy tag。
  PolicyTags *PolicyTags `json:"policyTags,omitempty" xml:"policyTags,omitempty"`
  // 如果是 CHAR/VARCHAR 类型，表示字段的最大长度。
  MaxLength *string `json:"maxLength,omitempty" xml:"maxLength,omitempty"`
  // 如果 DECIMAL 类型，表示精度。
  Precision *string `json:"precision,omitempty" xml:"precision,omitempty"`
  // 如果 DECIMAL 类型，表示 scale。
  Scale *string `json:"scale,omitempty" xml:"scale,omitempty"`
  // 可选。默认值的表达式字符串。
  DefaultValueExpression *string `json:"defaultValueExpression,omitempty" xml:"defaultValueExpression,omitempty"`
}

func (s TableFieldSchema) String() string {
  return tea.Prettify(s)
}

func (s TableFieldSchema) GoString() string {
  return s.String()
}

func (s *TableFieldSchema) SetFieldName(v string) *TableFieldSchema {
  s.FieldName = &v
  return s
}

func (s *TableFieldSchema) SetSqlTypeDefinition(v string) *TableFieldSchema {
  s.SqlTypeDefinition = &v
  return s
}

func (s *TableFieldSchema) SetTypeCategory(v string) *TableFieldSchema {
  s.TypeCategory = &v
  return s
}

func (s *TableFieldSchema) SetMode(v string) *TableFieldSchema {
  s.Mode = &v
  return s
}

func (s *TableFieldSchema) SetFields(v []*TableFieldSchema) *TableFieldSchema {
  s.Fields = v
  return s
}

func (s *TableFieldSchema) SetDescription(v string) *TableFieldSchema {
  s.Description = &v
  return s
}

func (s *TableFieldSchema) SetPolicyTags(v *PolicyTags) *TableFieldSchema {
  s.PolicyTags = v
  return s
}

func (s *TableFieldSchema) SetMaxLength(v string) *TableFieldSchema {
  s.MaxLength = &v
  return s
}

func (s *TableFieldSchema) SetPrecision(v string) *TableFieldSchema {
  s.Precision = &v
  return s
}

func (s *TableFieldSchema) SetScale(v string) *TableFieldSchema {
  s.Scale = &v
  return s
}

func (s *TableFieldSchema) SetDefaultValueExpression(v string) *TableFieldSchema {
  s.DefaultValueExpression = &v
  return s
}

type PolicyTags struct {
  Names []*string `json:"names,omitempty" xml:"names,omitempty" type:"Repeated"`
}

func (s PolicyTags) String() string {
  return tea.Prettify(s)
}

func (s PolicyTags) GoString() string {
  return s.String()
}

func (s *PolicyTags) SetNames(v []*string) *PolicyTags {
  s.Names = v
  return s
}

type Field struct {
  // 列名（如果是顶层列），或者 struct 字段名。
  FieldName *string `json:"fieldName,omitempty" xml:"fieldName,omitempty"`
}

func (s Field) String() string {
  return tea.Prettify(s)
}

func (s Field) GoString() string {
  return s.String()
}

func (s *Field) SetFieldName(v string) *Field {
  s.FieldName = &v
  return s
}

type SortingField struct {
  // 列名（如果是顶层列），或者 struct 字段名。
  FieldName *string `json:"fieldName,omitempty" xml:"fieldName,omitempty"`
  // 排序顺序
  // 
  // example:
  // 
  // DESC
  Order *string `json:"order,omitempty" xml:"order,omitempty"`
}

func (s SortingField) String() string {
  return tea.Prettify(s)
}

func (s SortingField) GoString() string {
  return s.String()
}

func (s *SortingField) SetFieldName(v string) *SortingField {
  s.FieldName = &v
  return s
}

func (s *SortingField) SetOrder(v string) *SortingField {
  s.Order = &v
  return s
}

type Clustering struct {
  // 表的聚簇类型，目前支持 hash/range。
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // 聚簇列定义。
  Fields []*string `json:"fields,omitempty" xml:"fields,omitempty" type:"Repeated"`
  // 聚簇桶的个数。只有 hash clustering 才有此属性。创建 hash clustering 表时，如不指定桶个数，默认为 16。
  NumBuckets *string `json:"numBuckets,omitempty" xml:"numBuckets,omitempty"`
}

func (s Clustering) String() string {
  return tea.Prettify(s)
}

func (s Clustering) GoString() string {
  return s.String()
}

func (s *Clustering) SetType(v string) *Clustering {
  s.Type = &v
  return s
}

func (s *Clustering) SetFields(v []*string) *Clustering {
  s.Fields = v
  return s
}

func (s *Clustering) SetNumBuckets(v string) *Clustering {
  s.NumBuckets = &v
  return s
}

type Fields struct {
  // 主键列名列表。
  Fields []*string `json:"fields,omitempty" xml:"fields,omitempty" type:"Repeated"`
}

func (s Fields) String() string {
  return tea.Prettify(s)
}

func (s Fields) GoString() string {
  return s.String()
}

func (s *Fields) SetFields(v []*string) *Fields {
  s.Fields = v
  return s
}

type TableConstraints struct {
  // 表的主键。系统不为主键自动去重。
  PrimaryKey *Fields `json:"primaryKey,omitempty" xml:"primaryKey,omitempty"`
}

func (s TableConstraints) String() string {
  return tea.Prettify(s)
}

func (s TableConstraints) GoString() string {
  return s.String()
}

func (s *TableConstraints) SetPrimaryKey(v *Fields) *TableConstraints {
  s.PrimaryKey = v
  return s
}

type PartitionDefinition struct {
  PartitionedColumns []*PartitionedColumn `json:"partitionedColumns,omitempty" xml:"partitionedColumns,omitempty" type:"Repeated"`
}

func (s PartitionDefinition) String() string {
  return tea.Prettify(s)
}

func (s PartitionDefinition) GoString() string {
  return s.String()
}

func (s *PartitionDefinition) SetPartitionedColumns(v []*PartitionedColumn) *PartitionDefinition {
  s.PartitionedColumns = v
  return s
}

type PartitionedColumn struct {
  Field *string `json:"field,omitempty" xml:"field,omitempty"`
}

func (s PartitionedColumn) String() string {
  return tea.Prettify(s)
}

func (s PartitionedColumn) GoString() string {
  return s.String()
}

func (s *PartitionedColumn) SetField(v string) *PartitionedColumn {
  s.Field = &v
  return s
}

type TableFormatDefinition struct {
  Transactional *bool `json:"transactional,omitempty" xml:"transactional,omitempty"`
  Version *string `json:"version,omitempty" xml:"version,omitempty"`
}

func (s TableFormatDefinition) String() string {
  return tea.Prettify(s)
}

func (s TableFormatDefinition) GoString() string {
  return s.String()
}

func (s *TableFormatDefinition) SetTransactional(v bool) *TableFormatDefinition {
  s.Transactional = &v
  return s
}

func (s *TableFormatDefinition) SetVersion(v string) *TableFormatDefinition {
  s.Version = &v
  return s
}

type ExpirationOptions struct {
  ExpirationDays *int32 `json:"expirationDays,omitempty" xml:"expirationDays,omitempty"`
  PartitionExpirationDays *int32 `json:"partitionExpirationDays,omitempty" xml:"partitionExpirationDays,omitempty"`
}

func (s ExpirationOptions) String() string {
  return tea.Prettify(s)
}

func (s ExpirationOptions) GoString() string {
  return s.String()
}

func (s *ExpirationOptions) SetExpirationDays(v int32) *ExpirationOptions {
  s.ExpirationDays = &v
  return s
}

func (s *ExpirationOptions) SetPartitionExpirationDays(v int32) *ExpirationOptions {
  s.PartitionExpirationDays = &v
  return s
}

type ExternalDataConfiguration struct {
  // 表数据所在的 URI
  SourceUris []*string `json:"sourceUris,omitempty" xml:"sourceUris,omitempty" type:"Repeated"`
  // 支持格式：PAIMON/ICEBERG/ORC/PARQUET/CSV 等
  SourceFormat *string `json:"sourceFormat,omitempty" xml:"sourceFormat,omitempty"`
  // 关联的 Connection ID
  Connection *string `json:"connection,omitempty" xml:"connection,omitempty"`
}

func (s ExternalDataConfiguration) String() string {
  return tea.Prettify(s)
}

func (s ExternalDataConfiguration) GoString() string {
  return s.String()
}

func (s *ExternalDataConfiguration) SetSourceUris(v []*string) *ExternalDataConfiguration {
  s.SourceUris = v
  return s
}

func (s *ExternalDataConfiguration) SetSourceFormat(v string) *ExternalDataConfiguration {
  s.SourceFormat = &v
  return s
}

func (s *ExternalDataConfiguration) SetConnection(v string) *ExternalDataConfiguration {
  s.Connection = &v
  return s
}

type Table struct {
  // 用于 read-modify-write 一致性校验。
  Etag *string `json:"etag,omitempty" xml:"etag,omitempty"`
  // 表的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/tables/{tableName}
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // 表所属的 project ID。
  ProjectId *string `json:"projectId,omitempty" xml:"projectId,omitempty"`
  // 表所属的 schema 名。
  SchemaName *string `json:"schemaName,omitempty" xml:"schemaName,omitempty"`
  // 表名。
  TableName *string `json:"tableName,omitempty" xml:"tableName,omitempty"`
  // 表的类型。
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // 表的描述。等价于 SQL DDL 中表的 comment。
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 表列的 schema 定义。
  TableSchema *TableFieldSchema `json:"tableSchema,omitempty" xml:"tableSchema,omitempty"`
  // 表的 cluster 属性定义，只有 cluster 表才有。
  Clustering *Clustering `json:"clustering,omitempty" xml:"clustering,omitempty"`
  // 表的主键约束定义，只有 delta 表才有。
  TableConstraints *TableConstraints `json:"tableConstraints,omitempty" xml:"tableConstraints,omitempty"`
  // 表的分区列定义，只有分区表才有。
  PartitionDefinition *PartitionDefinition `json:"partitionDefinition,omitempty" xml:"partitionDefinition,omitempty"`
  // 可选。仅内表有此字段。默认为普通表格式。
  TableFormatDefinition *TableFormatDefinition `json:"tableFormatDefinition,omitempty" xml:"tableFormatDefinition,omitempty"`
  // 表的创建时间（毫秒）。仅输出。
  CreateTime *string `json:"createTime,omitempty" xml:"createTime,omitempty"`
  // 表的修改时间（毫秒）。仅输出。
  LastModifiedTime *string `json:"lastModifiedTime,omitempty" xml:"lastModifiedTime,omitempty"`
  // 可选。表的过期时间配置。
  ExpirationOptions *ExpirationOptions `json:"expirationOptions,omitempty" xml:"expirationOptions,omitempty"`
  // 可选。表上的标签。
  Labels map[string]*string `json:"labels,omitempty" xml:"labels,omitempty"`
  // 外部表配置
  ExternalDataConfiguration *ExternalDataConfiguration `json:"externalDataConfiguration,omitempty" xml:"externalDataConfiguration,omitempty"`
  // 新增字段
}

func (s Table) String() string {
  return tea.Prettify(s)
}

func (s Table) GoString() string {
  return s.String()
}

func (s *Table) SetEtag(v string) *Table {
  s.Etag = &v
  return s
}

func (s *Table) SetName(v string) *Table {
  s.Name = &v
  return s
}

func (s *Table) SetProjectId(v string) *Table {
  s.ProjectId = &v
  return s
}

func (s *Table) SetSchemaName(v string) *Table {
  s.SchemaName = &v
  return s
}

func (s *Table) SetTableName(v string) *Table {
  s.TableName = &v
  return s
}

func (s *Table) SetType(v string) *Table {
  s.Type = &v
  return s
}

func (s *Table) SetDescription(v string) *Table {
  s.Description = &v
  return s
}

func (s *Table) SetTableSchema(v *TableFieldSchema) *Table {
  s.TableSchema = v
  return s
}

func (s *Table) SetClustering(v *Clustering) *Table {
  s.Clustering = v
  return s
}

func (s *Table) SetTableConstraints(v *TableConstraints) *Table {
  s.TableConstraints = v
  return s
}

func (s *Table) SetPartitionDefinition(v *PartitionDefinition) *Table {
  s.PartitionDefinition = v
  return s
}

func (s *Table) SetTableFormatDefinition(v *TableFormatDefinition) *Table {
  s.TableFormatDefinition = v
  return s
}

func (s *Table) SetCreateTime(v string) *Table {
  s.CreateTime = &v
  return s
}

func (s *Table) SetLastModifiedTime(v string) *Table {
  s.LastModifiedTime = &v
  return s
}

func (s *Table) SetExpirationOptions(v *ExpirationOptions) *Table {
  s.ExpirationOptions = v
  return s
}

func (s *Table) SetLabels(v map[string]*string) *Table {
  s.Labels = v
  return s
}

func (s *Table) SetExternalDataConfiguration(v *ExternalDataConfiguration) *Table {
  s.ExternalDataConfiguration = v
  return s
}

type ListTablesResponse struct {
  Tables []*Table `json:"tables,omitempty" xml:"tables,omitempty" type:"Repeated"`
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListTablesResponse) String() string {
  return tea.Prettify(s)
}

func (s ListTablesResponse) GoString() string {
  return s.String()
}

func (s *ListTablesResponse) SetTables(v []*Table) *ListTablesResponse {
  s.Tables = v
  return s
}

func (s *ListTablesResponse) SetNextPageToken(v string) *ListTablesResponse {
  s.NextPageToken = &v
  return s
}

// Description:
// 
// ==================================== Connection ====================================
type Connection struct {
  // 资源全局唯一名：namespaces/{namespace_ID}/connections/{connectionName}
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 32]。
  ConnectionName *string `json:"connectionName,omitempty" xml:"connectionName,omitempty"`
  // 可选。最多 1KB。
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Connection 的创建时间（毫秒）
  CreationTime *string `json:"creationTime,omitempty" xml:"creationTime,omitempty"`
  // 最后修改时间（毫秒）
  LastModifiedTime *string `json:"lastModifiedTime,omitempty" xml:"lastModifiedTime,omitempty"`
  // Connection 的类型。必需项。
  ConnectionType *string `json:"connectionType,omitempty" xml:"connectionType,omitempty"`
  // 云上资源类型的 connection 对应的选项配置。仅当 connectionType 为 CLOUD_RESOURCE 时才设置。
  CloudResource *CloudResourceOptions `json:"cloudResource,omitempty" xml:"cloudResource,omitempty"`
  // 此 connection 所属的 region。
  Region *string `json:"region,omitempty" xml:"region,omitempty"`
}

func (s Connection) String() string {
  return tea.Prettify(s)
}

func (s Connection) GoString() string {
  return s.String()
}

func (s *Connection) SetName(v string) *Connection {
  s.Name = &v
  return s
}

func (s *Connection) SetConnectionName(v string) *Connection {
  s.ConnectionName = &v
  return s
}

func (s *Connection) SetDescription(v string) *Connection {
  s.Description = &v
  return s
}

func (s *Connection) SetCreationTime(v string) *Connection {
  s.CreationTime = &v
  return s
}

func (s *Connection) SetLastModifiedTime(v string) *Connection {
  s.LastModifiedTime = &v
  return s
}

func (s *Connection) SetConnectionType(v string) *Connection {
  s.ConnectionType = &v
  return s
}

func (s *Connection) SetCloudResource(v *CloudResourceOptions) *Connection {
  s.CloudResource = v
  return s
}

func (s *Connection) SetRegion(v string) *Connection {
  s.Region = &v
  return s
}

type CloudResourceOptions struct {
  // 被委托的账号名。在创建 connection 时自动保存为创建者的账号。
  DelegatedAccount *string `json:"delegatedAccount,omitempty" xml:"delegatedAccount,omitempty"`
  // 授权给 MaxCompute 服务扮演的 RAM 角色 ARN。
  RamRoleArn *string `json:"ramRoleArn,omitempty" xml:"ramRoleArn,omitempty"`
}

func (s CloudResourceOptions) String() string {
  return tea.Prettify(s)
}

func (s CloudResourceOptions) GoString() string {
  return s.String()
}

func (s *CloudResourceOptions) SetDelegatedAccount(v string) *CloudResourceOptions {
  s.DelegatedAccount = &v
  return s
}

func (s *CloudResourceOptions) SetRamRoleArn(v string) *CloudResourceOptions {
  s.RamRoleArn = &v
  return s
}

type ListConnectionsResponse struct {
  Connections []*Connection `json:"connections,omitempty" xml:"connections,omitempty" type:"Repeated"`
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListConnectionsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListConnectionsResponse) GoString() string {
  return s.String()
}

func (s *ListConnectionsResponse) SetConnections(v []*Connection) *ListConnectionsResponse {
  s.Connections = v
  return s
}

func (s *ListConnectionsResponse) SetNextPageToken(v string) *ListConnectionsResponse {
  s.NextPageToken = &v
  return s
}

// Description:
// 
// ==================================== Role ====================================
// Role model
type Role struct {
  // 资源全局唯一名。e.g., namespaces/{namespace_ID}/roles/{roleName}
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。
  RoleName *string `json:"roleName,omitempty" xml:"roleName,omitempty"`
  // 可选。最多 1KB。
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Role 包含的权限。
  IncludedPermissions []*string `json:"includedPermissions,omitempty" xml:"includedPermissions,omitempty" type:"Repeated"`
  // 用于一致性校验。
  Etag *string `json:"etag,omitempty" xml:"etag,omitempty"`
  // 表示是否被删除。
  // 
  // example:
  // 
  // false
  Deleted *bool `json:"deleted,omitempty" xml:"deleted,omitempty"`
}

func (s Role) String() string {
  return tea.Prettify(s)
}

func (s Role) GoString() string {
  return s.String()
}

func (s *Role) SetName(v string) *Role {
  s.Name = &v
  return s
}

func (s *Role) SetRoleName(v string) *Role {
  s.RoleName = &v
  return s
}

func (s *Role) SetDescription(v string) *Role {
  s.Description = &v
  return s
}

func (s *Role) SetIncludedPermissions(v []*string) *Role {
  s.IncludedPermissions = v
  return s
}

func (s *Role) SetEtag(v string) *Role {
  s.Etag = &v
  return s
}

func (s *Role) SetDeleted(v bool) *Role {
  s.Deleted = &v
  return s
}

// ListRolesResponse model
type ListRolesResponse struct {
  // 角色列表。
  Roles []*Role `json:"roles,omitempty" xml:"roles,omitempty" type:"Repeated"`
  // 下一页的token。
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListRolesResponse) String() string {
  return tea.Prettify(s)
}

func (s ListRolesResponse) GoString() string {
  return s.String()
}

func (s *ListRolesResponse) SetRoles(v []*Role) *ListRolesResponse {
  s.Roles = v
  return s
}

func (s *ListRolesResponse) SetNextPageToken(v string) *ListRolesResponse {
  s.NextPageToken = &v
  return s
}

// Description:
// 
// ==================================== Taxonomy ====================================
// Taxonomy model
type Taxonomy struct {
  // 资源全局唯一名。e.g., namespaces/{namespace_ID}/taxonomies/{ID}
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。
  TaxonomyName *string `json:"taxonomyName,omitempty" xml:"taxonomyName,omitempty"`
  // 可选。最多 1KB。
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Taxonomy 下开启的 policy 类型列表，默认为 POLICY_TYPE_UNSPECIFIED
  ActivatedPolicyTypes []*string `json:"activatedPolicyTypes,omitempty" xml:"activatedPolicyTypes,omitempty" type:"Repeated"`
  // 此 Taxonomy 内 policy tag 的个数。
  PolicyTagCount *int `json:"policyTagCount,omitempty" xml:"policyTagCount,omitempty"`
  // Taxonomy 的创建时间戳（毫秒）。仅输出。
  CreateTime *string `json:"createTime,omitempty" xml:"createTime,omitempty"`
  // Taxonomy 的最后修改时间戳（毫秒）。仅输出。
  LastModifiedTime *string `json:"lastModifiedTime,omitempty" xml:"lastModifiedTime,omitempty"`
}

func (s Taxonomy) String() string {
  return tea.Prettify(s)
}

func (s Taxonomy) GoString() string {
  return s.String()
}

func (s *Taxonomy) SetName(v string) *Taxonomy {
  s.Name = &v
  return s
}

func (s *Taxonomy) SetTaxonomyName(v string) *Taxonomy {
  s.TaxonomyName = &v
  return s
}

func (s *Taxonomy) SetDescription(v string) *Taxonomy {
  s.Description = &v
  return s
}

func (s *Taxonomy) SetActivatedPolicyTypes(v []*string) *Taxonomy {
  s.ActivatedPolicyTypes = v
  return s
}

func (s *Taxonomy) SetPolicyTagCount(v int) *Taxonomy {
  s.PolicyTagCount = &v
  return s
}

func (s *Taxonomy) SetCreateTime(v string) *Taxonomy {
  s.CreateTime = &v
  return s
}

func (s *Taxonomy) SetLastModifiedTime(v string) *Taxonomy {
  s.LastModifiedTime = &v
  return s
}

// PolicyTag model
type PolicyTag struct {
  // PolicyTag的完整路径。e.g., namespaces/{namespace_ID}/taxonomies/{TID}/policyTags/{ID}
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // 父 Taxonomy 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。
  PolicyTagName *string `json:"policyTagName,omitempty" xml:"policyTagName,omitempty"`
  // 可选。最多 1KB。
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 父节点的name。空代表根节点。
  ParentPolicyTag *string `json:"parentPolicyTag,omitempty" xml:"parentPolicyTag,omitempty"`
  // 子节点的name列表。仅输出。
  ChildPolicyTags []*string `json:"childPolicyTags,omitempty" xml:"childPolicyTags,omitempty" type:"Repeated"`
}

func (s PolicyTag) String() string {
  return tea.Prettify(s)
}

func (s PolicyTag) GoString() string {
  return s.String()
}

func (s *PolicyTag) SetName(v string) *PolicyTag {
  s.Name = &v
  return s
}

func (s *PolicyTag) SetPolicyTagName(v string) *PolicyTag {
  s.PolicyTagName = &v
  return s
}

func (s *PolicyTag) SetDescription(v string) *PolicyTag {
  s.Description = &v
  return s
}

func (s *PolicyTag) SetParentPolicyTag(v string) *PolicyTag {
  s.ParentPolicyTag = &v
  return s
}

func (s *PolicyTag) SetChildPolicyTags(v []*string) *PolicyTag {
  s.ChildPolicyTags = v
  return s
}

// List responses
type ListTaxonomiesResponse struct {
  // Taxonomy列表。
  Taxonomies []*Taxonomy `json:"taxonomies,omitempty" xml:"taxonomies,omitempty" type:"Repeated"`
  // 下一页的token。
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListTaxonomiesResponse) String() string {
  return tea.Prettify(s)
}

func (s ListTaxonomiesResponse) GoString() string {
  return s.String()
}

func (s *ListTaxonomiesResponse) SetTaxonomies(v []*Taxonomy) *ListTaxonomiesResponse {
  s.Taxonomies = v
  return s
}

func (s *ListTaxonomiesResponse) SetNextPageToken(v string) *ListTaxonomiesResponse {
  s.NextPageToken = &v
  return s
}

type ListPolicyTagsResponse struct {
  // PolicyTag列表。
  PolicyTags []*PolicyTag `json:"policyTags,omitempty" xml:"policyTags,omitempty" type:"Repeated"`
  // 下一页的token。
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListPolicyTagsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListPolicyTagsResponse) GoString() string {
  return s.String()
}

func (s *ListPolicyTagsResponse) SetPolicyTags(v []*PolicyTag) *ListPolicyTagsResponse {
  s.PolicyTags = v
  return s
}

func (s *ListPolicyTagsResponse) SetNextPageToken(v string) *ListPolicyTagsResponse {
  s.NextPageToken = &v
  return s
}

// Description:
// 
// ==================================== DataPolicy ====================================
type DataPolicy struct {
  // namespaces/{namespace_ID}/dataPolicies/{dataPolicyName}。仅输出。
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // 用户指定的 data policy 名，在账号级唯一。
  DataPolicyName *string `json:"dataPolicyName,omitempty" xml:"dataPolicyName,omitempty"`
  // Data policy 绑定的 policy tag 资源全名。
  PolicyTag *string `json:"policyTag,omitempty" xml:"policyTag,omitempty"`
  // data policy 的类型，目前仅支持 DATA_MASKING_POLICY 类型。
  DataPolicyType *string `json:"dataPolicyType,omitempty" xml:"dataPolicyType,omitempty"`
  // Data policy 上定义的脱敏规则。
  DataMaskingPolicy *DataMaskingPolicy `json:"dataMaskingPolicy,omitempty" xml:"dataMaskingPolicy,omitempty"`
}

func (s DataPolicy) String() string {
  return tea.Prettify(s)
}

func (s DataPolicy) GoString() string {
  return s.String()
}

func (s *DataPolicy) SetName(v string) *DataPolicy {
  s.Name = &v
  return s
}

func (s *DataPolicy) SetDataPolicyName(v string) *DataPolicy {
  s.DataPolicyName = &v
  return s
}

func (s *DataPolicy) SetPolicyTag(v string) *DataPolicy {
  s.PolicyTag = &v
  return s
}

func (s *DataPolicy) SetDataPolicyType(v string) *DataPolicy {
  s.DataPolicyType = &v
  return s
}

func (s *DataPolicy) SetDataMaskingPolicy(v *DataMaskingPolicy) *DataPolicy {
  s.DataMaskingPolicy = v
  return s
}

type DataMaskingPolicy struct {
  // 预定义脱敏策略的类型。
  PredefinedExpression *string `json:"predefinedExpression,omitempty" xml:"predefinedExpression,omitempty"`
  // 预定义脱敏策略的参数。
  Parameters []*string `json:"parameters,omitempty" xml:"parameters,omitempty" type:"Repeated"`
}

func (s DataMaskingPolicy) String() string {
  return tea.Prettify(s)
}

func (s DataMaskingPolicy) GoString() string {
  return s.String()
}

func (s *DataMaskingPolicy) SetPredefinedExpression(v string) *DataMaskingPolicy {
  s.PredefinedExpression = &v
  return s
}

func (s *DataMaskingPolicy) SetParameters(v []*string) *DataMaskingPolicy {
  s.Parameters = v
  return s
}

type ListDataPoliciesResponse struct {
  DataPolicies []*DataPolicy `json:"dataPolicies,omitempty" xml:"dataPolicies,omitempty" type:"Repeated"`
  // 分页标记。
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListDataPoliciesResponse) String() string {
  return tea.Prettify(s)
}

func (s ListDataPoliciesResponse) GoString() string {
  return s.String()
}

func (s *ListDataPoliciesResponse) SetDataPolicies(v []*DataPolicy) *ListDataPoliciesResponse {
  s.DataPolicies = v
  return s
}

func (s *ListDataPoliciesResponse) SetNextPageToken(v string) *ListDataPoliciesResponse {
  s.NextPageToken = &v
  return s
}

// Description:
// 
// ==================================== Project/Schema ====================================
// Models
type Project struct {
  // Project的资源全名：projects/{projectId}。仅输出。
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // Project唯一ID
  ProjectId *string `json:"projectId,omitempty" xml:"projectId,omitempty"`
  // Project的拥有者
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // Project描述
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 创建时间戳（UTC毫秒）
  CreateTime *string `json:"createTime,omitempty" xml:"createTime,omitempty"`
  // 最后修改时间戳（UTC毫秒）
  LastModifiedTime *string `json:"lastModifiedTime,omitempty" xml:"lastModifiedTime,omitempty"`
  // 是否开启三层模型
  SchemaEnabled *bool `json:"schemaEnabled,omitempty" xml:"schemaEnabled,omitempty"`
  // 所属region
  Region *string `json:"region,omitempty" xml:"region,omitempty"`
}

func (s Project) String() string {
  return tea.Prettify(s)
}

func (s Project) GoString() string {
  return s.String()
}

func (s *Project) SetName(v string) *Project {
  s.Name = &v
  return s
}

func (s *Project) SetProjectId(v string) *Project {
  s.ProjectId = &v
  return s
}

func (s *Project) SetOwner(v string) *Project {
  s.Owner = &v
  return s
}

func (s *Project) SetDescription(v string) *Project {
  s.Description = &v
  return s
}

func (s *Project) SetCreateTime(v string) *Project {
  s.CreateTime = &v
  return s
}

func (s *Project) SetLastModifiedTime(v string) *Project {
  s.LastModifiedTime = &v
  return s
}

func (s *Project) SetSchemaEnabled(v bool) *Project {
  s.SchemaEnabled = &v
  return s
}

func (s *Project) SetRegion(v string) *Project {
  s.Region = &v
  return s
}

type Schema struct {
  // Schema的资源全名：projects/{projectId}/schemas/{schemaName}。仅输出。
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // Project下唯一名称
  SchemaName *string `json:"schemaName,omitempty" xml:"schemaName,omitempty" maxLength:"128"`
  // 可选描述，不超过xxKB
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Schema类型：DEFAULT/EXTERNAL
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // Schema拥有者
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // 外部schema配置
  ExternalSchemaConfiguration *ExternalSchemaConfiguration `json:"externalSchemaConfiguration,omitempty" xml:"externalSchemaConfiguration,omitempty"`
}

func (s Schema) String() string {
  return tea.Prettify(s)
}

func (s Schema) GoString() string {
  return s.String()
}

func (s *Schema) SetName(v string) *Schema {
  s.Name = &v
  return s
}

func (s *Schema) SetSchemaName(v string) *Schema {
  s.SchemaName = &v
  return s
}

func (s *Schema) SetDescription(v string) *Schema {
  s.Description = &v
  return s
}

func (s *Schema) SetType(v string) *Schema {
  s.Type = &v
  return s
}

func (s *Schema) SetOwner(v string) *Schema {
  s.Owner = &v
  return s
}

func (s *Schema) SetExternalSchemaConfiguration(v *ExternalSchemaConfiguration) *Schema {
  s.ExternalSchemaConfiguration = v
  return s
}

type ExternalSchemaConfiguration struct {
  // 关联的connection ID
  Connection *string `json:"connection,omitempty" xml:"connection,omitempty"`
  // 外部catalog schema配置
  ExternalCatalogSchemaOptions *ExternalCatalogSchemaOptions `json:"externalCatalogSchemaOptions,omitempty" xml:"externalCatalogSchemaOptions,omitempty"`
}

func (s ExternalSchemaConfiguration) String() string {
  return tea.Prettify(s)
}

func (s ExternalSchemaConfiguration) GoString() string {
  return s.String()
}

func (s *ExternalSchemaConfiguration) SetConnection(v string) *ExternalSchemaConfiguration {
  s.Connection = &v
  return s
}

func (s *ExternalSchemaConfiguration) SetExternalCatalogSchemaOptions(v *ExternalCatalogSchemaOptions) *ExternalSchemaConfiguration {
  s.ExternalCatalogSchemaOptions = v
  return s
}

type ExternalCatalogSchemaOptions struct {
  // 外部schema属性配置
  Parameters map[string]*string `json:"parameters,omitempty" xml:"parameters,omitempty"`
}

func (s ExternalCatalogSchemaOptions) String() string {
  return tea.Prettify(s)
}

func (s ExternalCatalogSchemaOptions) GoString() string {
  return s.String()
}

func (s *ExternalCatalogSchemaOptions) SetParameters(v map[string]*string) *ExternalCatalogSchemaOptions {
  s.Parameters = v
  return s
}

type ListProjectsResponse struct {
  Projects []*Project `json:"projects,omitempty" xml:"projects,omitempty" type:"Repeated"`
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListProjectsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListProjectsResponse) GoString() string {
  return s.String()
}

func (s *ListProjectsResponse) SetProjects(v []*Project) *ListProjectsResponse {
  s.Projects = v
  return s
}

func (s *ListProjectsResponse) SetNextPageToken(v string) *ListProjectsResponse {
  s.NextPageToken = &v
  return s
}

type ListSchemasResponse struct {
  Schemas []*Schema `json:"schemas,omitempty" xml:"schemas,omitempty" type:"Repeated"`
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListSchemasResponse) String() string {
  return tea.Prettify(s)
}

func (s ListSchemasResponse) GoString() string {
  return s.String()
}

func (s *ListSchemasResponse) SetSchemas(v []*Schema) *ListSchemasResponse {
  s.Schemas = v
  return s
}

func (s *ListSchemasResponse) SetNextPageToken(v string) *ListSchemasResponse {
  s.NextPageToken = &v
  return s
}

// Description:
// 
// ==================================== Partition ====================================
// Models
type Partition struct {
  // 分区spec，格式样例为 bu=tt/ds=20250515
  Spec *string `json:"spec,omitempty" xml:"spec,omitempty"`
}

func (s Partition) String() string {
  return tea.Prettify(s)
}

func (s Partition) GoString() string {
  return s.String()
}

func (s *Partition) SetSpec(v string) *Partition {
  s.Spec = &v
  return s
}

type ListPartitionsResponse struct {
  Partitions []*Partition `json:"partitions,omitempty" xml:"partitions,omitempty" type:"Repeated"`
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListPartitionsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListPartitionsResponse) GoString() string {
  return s.String()
}

func (s *ListPartitionsResponse) SetPartitions(v []*Partition) *ListPartitionsResponse {
  s.Partitions = v
  return s
}

func (s *ListPartitionsResponse) SetNextPageToken(v string) *ListPartitionsResponse {
  s.NextPageToken = &v
  return s
}

// Description:
// 
// ==================================== DataScans ====================================
// Models
type DataScanSource struct {
  // location地址。支持oss、dlf 和 holo
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // connection name。提供访问source需要的身份与网络信息。需要鉴权
  Connection *string `json:"connection,omitempty" xml:"connection,omitempty"`
  // 忽略访问的路径。支持正则表达式
  Ignores []*string `json:"ignores,omitempty" xml:"ignores,omitempty" type:"Repeated"`
}

func (s DataScanSource) String() string {
  return tea.Prettify(s)
}

func (s DataScanSource) GoString() string {
  return s.String()
}

func (s *DataScanSource) SetLocation(v string) *DataScanSource {
  s.Location = &v
  return s
}

func (s *DataScanSource) SetConnection(v string) *DataScanSource {
  s.Connection = &v
  return s
}

func (s *DataScanSource) SetIgnores(v []*string) *DataScanSource {
  s.Ignores = v
  return s
}

type DataScanTarget struct {
  // 结果写入的project name。
  Project *string `json:"project,omitempty" xml:"project,omitempty"`
  // 当dataScan.type为table时，table写入的schema
  Schema *string `json:"schema,omitempty" xml:"schema,omitempty"`
  // 爬取任务自动生成的table/schema名称的前缀，防止命名冲突。
  NamePrefix *string `json:"namePrefix,omitempty" xml:"namePrefix,omitempty"`
  // 用户可指定的最终表 / schema 的属性
  Properties *string `json:"properties,omitempty" xml:"properties,omitempty"`
}

func (s DataScanTarget) String() string {
  return tea.Prettify(s)
}

func (s DataScanTarget) GoString() string {
  return s.String()
}

func (s *DataScanTarget) SetProject(v string) *DataScanTarget {
  s.Project = &v
  return s
}

func (s *DataScanTarget) SetSchema(v string) *DataScanTarget {
  s.Schema = &v
  return s
}

func (s *DataScanTarget) SetNamePrefix(v string) *DataScanTarget {
  s.NamePrefix = &v
  return s
}

func (s *DataScanTarget) SetProperties(v string) *DataScanTarget {
  s.Properties = &v
  return s
}

type DataScanProperties struct {
  // AUTO/PARQUET/ORC/JSON/CSV。只爬取对应属性的数据。若指定，则忽略其他类型的文件。auto为不指定属性自动探测。
  FormatFilter *string `json:"formatFilter,omitempty" xml:"formatFilter,omitempty"`
  // enum	SAMPLE/TOTAL。 默认为SAMPLE。扫描时抽样扫描或者完整扫描
  ScanMode *string `json:"scanMode,omitempty" xml:"scanMode,omitempty"`
  // 是否统计信息用于查询优化
  EnableStats *bool `json:"enableStats,omitempty" xml:"enableStats,omitempty"`
  // 其余的配置可选项，如csv格式下的一些额外选项
  Options *string `json:"options,omitempty" xml:"options,omitempty"`
  // 分区路径识别的pattern, 例如{table}/{part1}={value1}/{part2}={value2}
  Pattern *string `json:"options,omitempty" xml:"options,omitempty"`
  // 发现表元数据发生变化时的处理策略。APPEND_ONLY/OVERWRITE/IGNORE
  UpdatePolicy *string `json:"updatePolicy,omitempty" xml:"updatePolicy,omitempty"`
  // 发现表删除时是否自动删除
  SyncRemove *bool `json:"syncRemove,omitempty" xml:"syncRemove,omitempty"`
  // false代表爬取任务只输出结果，不提交ddl
  AutoCommit *bool `json:"autoCommit,omitempty" xml:"autoCommit,omitempty"`
}

func (s DataScanProperties) String() string {
  return tea.Prettify(s)
}

func (s DataScanProperties) GoString() string {
  return s.String()
}

func (s *DataScanProperties) SetFormatFilter(v string) *DataScanProperties {
  s.FormatFilter = &v
  return s
}

func (s *DataScanProperties) SetScanMode(v string) *DataScanProperties {
  s.ScanMode = &v
  return s
}

func (s *DataScanProperties) SetEnableStats(v bool) *DataScanProperties {
  s.EnableStats = &v
  return s
}

func (s *DataScanProperties) SetOptions(v string) *DataScanProperties {
  s.Options = &v
  return s
}

func (s *DataScanProperties) SetPattern(v string) *DataScanProperties {
  s.Pattern = &v
  return s
}

func (s *DataScanProperties) SetUpdatePolicy(v string) *DataScanProperties {
  s.UpdatePolicy = &v
  return s
}

func (s *DataScanProperties) SetSyncRemove(v bool) *DataScanProperties {
  s.SyncRemove = &v
  return s
}

func (s *DataScanProperties) SetAutoCommit(v bool) *DataScanProperties {
  s.AutoCommit = &v
  return s
}

type DataScan struct {
  // 资源全局唯一名。e.g., namespaces/{namespaceID}/dataScans/{dataScanName}
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // 用户指定的爬取任务名称
  ScanName *string `json:"scanName,omitempty" xml:"scanName,omitempty"`
  // 取值范围为：TABLE_DISCOVERY, SCHEMA_DISCOVERY
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // dataScan 的创建者
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // 客户 ID
  CustomerId *string `json:"customerId,omitempty" xml:"customerId,omitempty"`
  // dataScan 所属的 namespace
  NamespaceId *string `json:"namespaceId,omitempty" xml:"namespaceId,omitempty"`
  // 用户自定义的描述
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 系统自动生成的 scan ID，只读字段。展示项
  ScanId *string `json:"scanId,omitempty" xml:"scanId,omitempty"`
  // 创建的时间，UTC timestamp
  CreationTime *int64 `json:"creationTime,omitempty" xml:"creationTime,omitempty"`
  // 上次修改的时间，UTC timestamp
  LastModifiedTime *int64 `json:"lastModifiedTime,omitempty" xml:"lastModifiedTime,omitempty"`
  // 爬取任务上次触发的时间（开始调度时间），UTC timestamp。未触发过默认值为 0
  LastTriggeredTime *int64 `json:"lastTriggeredTime,omitempty" xml:"lastTriggeredTime,omitempty"`
  // 触发当前调度的来源；具体用户或调度器
  LastTriggeredBy *string `json:"lastTriggeredBy,omitempty" xml:"lastTriggeredBy,omitempty"`
  // dataScan 对象的调度状态。包含 IDLE/IMMEDIATE/PENDING/SCHEDULING 四种状态。dataScan 初始化状态为 IDLE，如果创建后立刻执行，设置为 IMMEDIATE
  SchedulingStatus *string `json:"schedulingStatus,omitempty" xml:"schedulingStatus,omitempty"`
  // 元数据爬取和发现来源，包括 location、connection 等信息
  Source *DataScanSource `json:"source,omitempty" xml:"source,omitempty"`
  // 控制 dataScan 发现结果写入的参数，包含 project、namePrefix、以及透传的 Tbl Properties 等
  Target *DataScanTarget `json:"target,omitempty" xml:"target,omitempty"`
  // 爬取任务的可选参数，包含更新策略、分类器等
  Properties *DataScanProperties `json:"properties,omitempty" xml:"properties,omitempty"`
  // manual/periodic，手动触发或者周期性自动触发
  SchedulerMode *string `json:"schedulerMode,omitempty" xml:"schedulerMode,omitempty"`
  // 当 schedulerMode 为 periodic 时，两次爬取任务之间间隔的最大间隔，取值为 [1h-7d]
  SchedulerInterval *string `json:"schedulerInterval,omitempty" xml:"schedulerInterval,omitempty"`
}

func (s DataScan) String() string {
  return tea.Prettify(s)
}

func (s DataScan) GoString() string {
  return s.String()
}

func (s *DataScan) SetName(v string) *DataScan {
  s.Name = &v
  return s
}

func (s *DataScan) SetScanName(v string) *DataScan {
  s.ScanName = &v
  return s
}

func (s *DataScan) SetType(v string) *DataScan {
  s.Type = &v
  return s
}

func (s *DataScan) SetCreator(v string) *DataScan {
  s.Creator = &v
  return s
}

func (s *DataScan) SetCustomerId(v string) *DataScan {
  s.CustomerId = &v
  return s
}

func (s *DataScan) SetNamespaceId(v string) *DataScan {
  s.NamespaceId = &v
  return s
}

func (s *DataScan) SetDescription(v string) *DataScan {
  s.Description = &v
  return s
}

func (s *DataScan) SetScanId(v string) *DataScan {
  s.ScanId = &v
  return s
}

func (s *DataScan) SetCreationTime(v int64) *DataScan {
  s.CreationTime = &v
  return s
}

func (s *DataScan) SetLastModifiedTime(v int64) *DataScan {
  s.LastModifiedTime = &v
  return s
}

func (s *DataScan) SetLastTriggeredTime(v int64) *DataScan {
  s.LastTriggeredTime = &v
  return s
}

func (s *DataScan) SetLastTriggeredBy(v string) *DataScan {
  s.LastTriggeredBy = &v
  return s
}

func (s *DataScan) SetSchedulingStatus(v string) *DataScan {
  s.SchedulingStatus = &v
  return s
}

func (s *DataScan) SetSource(v *DataScanSource) *DataScan {
  s.Source = v
  return s
}

func (s *DataScan) SetTarget(v *DataScanTarget) *DataScan {
  s.Target = v
  return s
}

func (s *DataScan) SetProperties(v *DataScanProperties) *DataScan {
  s.Properties = v
  return s
}

func (s *DataScan) SetSchedulerMode(v string) *DataScan {
  s.SchedulerMode = &v
  return s
}

func (s *DataScan) SetSchedulerInterval(v string) *DataScan {
  s.SchedulerInterval = &v
  return s
}

type ScanJob struct {
  // Job ID
  JobId *string `json:"jobId,omitempty" xml:"jobId,omitempty"`
  // 作业所属的 namespace
  NamespaceId *string `json:"namespaceId,omitempty" xml:"namespaceId,omitempty"`
  // 系统自动生成的 dataScan ID
  DataScanId *string `json:"dataScanId,omitempty" xml:"dataScanId,omitempty"`
  // 所属爬取任务名称。此处为全称 namespace/$nsId/dataScan/$scanName
  DataScanName *string `json:"dataScanName,omitempty" xml:"dataScanName,omitempty"`
  // 触发此次爬取作业的人，定时触发则为 scheduler
  TriggeredBy *string `json:"triggeredBy,omitempty" xml:"triggeredBy,omitempty"`
  // 爬取作业开始时间，UTC timestamp
  StartTime *int64 `json:"startTime,omitempty" xml:"startTime,omitempty"`
  // 爬取作业结束时间，UTC timestamp
  EndTime *int64 `json:"endTime,omitempty" xml:"endTime,omitempty"`
  // 爬取作业状态，取值范围：Created/Running/Terminated/Failed
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // 爬取作业状态详细信息，如报错信息
  StatusDetail *string `json:"statusDetail,omitempty" xml:"statusDetail,omitempty"`
  // 爬取作业返回的需要提交的 DDL 信息
  Ddl *string `json:"ddl,omitempty" xml:"ddl,omitempty"`
  // 爬取作业返回的 stats 信息，JSON 格式
  Stats *string `json:"stats,omitempty" xml:"stats,omitempty"`
}

func (s ScanJob) String() string {
  return tea.Prettify(s)
}

func (s ScanJob) GoString() string {
  return s.String()
}

func (s *ScanJob) SetJobId(v string) *ScanJob {
  s.JobId = &v
  return s
}

func (s *ScanJob) SetNamespaceId(v string) *ScanJob {
  s.NamespaceId = &v
  return s
}

func (s *ScanJob) SetDataScanId(v string) *ScanJob {
  s.DataScanId = &v
  return s
}

func (s *ScanJob) SetDataScanName(v string) *ScanJob {
  s.DataScanName = &v
  return s
}

func (s *ScanJob) SetTriggeredBy(v string) *ScanJob {
  s.TriggeredBy = &v
  return s
}

func (s *ScanJob) SetStartTime(v int64) *ScanJob {
  s.StartTime = &v
  return s
}

func (s *ScanJob) SetEndTime(v int64) *ScanJob {
  s.EndTime = &v
  return s
}

func (s *ScanJob) SetStatus(v string) *ScanJob {
  s.Status = &v
  return s
}

func (s *ScanJob) SetStatusDetail(v string) *ScanJob {
  s.StatusDetail = &v
  return s
}

func (s *ScanJob) SetDdl(v string) *ScanJob {
  s.Ddl = &v
  return s
}

func (s *ScanJob) SetStats(v string) *ScanJob {
  s.Stats = &v
  return s
}

type ListDataScansResponse struct {
  // 分页 token
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
  // 返回所有的 dataScans 列表。
  DataScans []*DataScan `json:"dataScans,omitempty" xml:"dataScans,omitempty" type:"Repeated"`
}

func (s ListDataScansResponse) String() string {
  return tea.Prettify(s)
}

func (s ListDataScansResponse) GoString() string {
  return s.String()
}

func (s *ListDataScansResponse) SetNextPageToken(v string) *ListDataScansResponse {
  s.NextPageToken = &v
  return s
}

func (s *ListDataScansResponse) SetDataScans(v []*DataScan) *ListDataScansResponse {
  s.DataScans = v
  return s
}

// DataScanJob
type ListDataScanJobsResponse struct {
  // 返回所有的 dataScan jobs 列表
  ScanJobs []*ScanJob `json:"scanJobs,omitempty" xml:"scanJobs,omitempty" type:"Repeated"`
  // 分页 token
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListDataScanJobsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListDataScanJobsResponse) GoString() string {
  return s.String()
}

func (s *ListDataScanJobsResponse) SetScanJobs(v []*ScanJob) *ListDataScanJobsResponse {
  s.ScanJobs = v
  return s
}

func (s *ListDataScanJobsResponse) SetNextPageToken(v string) *ListDataScanJobsResponse {
  s.NextPageToken = &v
  return s
}

// Description:
// 
// ==================================== Models ====================================
// Model 实体定义
type Model struct {
  // 模型的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/models/{modelName}
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // 模型名。上级 Schema 内唯一。大小写不敏感。包含字符：[a-z][A-Z][0-9]_，字节个数范围 [3, 255]
  ModelName *string `json:"modelName,omitempty" xml:"modelName,omitempty"`
  // 版本名。同一 model 范围内唯一。大小写不敏感。包含字符：[a-z][A-Z][0-9]_，字节个数范围 [3, 255]
  VersionName *string `json:"versionName,omitempty" xml:"versionName,omitempty"`
  // 模型的默认版本名
  DefaultVersion *string `json:"defaultVersion,omitempty" xml:"defaultVersion,omitempty"`
  // 模型的创建时间（毫秒）
  CreateTime *string `json:"createTime,omitempty" xml:"createTime,omitempty"`
  // 模型的修改时间（毫秒）
  UpdateTime *string `json:"updateTime,omitempty" xml:"updateTime,omitempty"`
  // 版本的创建时间（毫秒）
  VersionCreateTime *string `json:"versionCreateTime,omitempty" xml:"versionCreateTime,omitempty"`
  // 版本的修改时间（毫秒）
  VersionUpdateTime *string `json:"versionUpdateTime,omitempty" xml:"versionUpdateTime,omitempty"`
  // 模型的描述，最长 1KB
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 版本的描述，最长 1KB
  VersionDescription *string `json:"versionDescription,omitempty" xml:"versionDescription,omitempty"`
  // 模型基于最近更新时间的生命周期（天）
  ExpirationDays *int `json:"expirationDays,omitempty" xml:"expirationDays,omitempty"`
  // 版本基于最近更新时间的生命周期（天）
  VersionExpirationDays *int `json:"versionExpirationDays,omitempty" xml:"versionExpirationDays,omitempty"`
  // 模型的来源类型，创建后不支持修改
  SourceType *string `json:"sourceType,omitempty" xml:"sourceType,omitempty"`
  // 模型的类型，创建后不支持修改
  ModelType *string `json:"modelType,omitempty" xml:"modelType,omitempty"`
  // 模型的标签
  Labels map[string]*string `json:"labels,omitempty" xml:"labels,omitempty"`
  // 版本的预处理信息
  Transform map[string]*string `json:"transform,omitempty" xml:"transform,omitempty"`
  // 版本对应模型文件的路径
  Path *string `json:"path,omitempty" xml:"path,omitempty"`
  // 版本的参数
  Options map[string]*string `json:"options,omitempty" xml:"options,omitempty"`
  // 模型的额外信息
  ExtraInfo map[string]*string `json:"extraInfo,omitempty" xml:"extraInfo,omitempty"`
  // 版本的额外信息
  VersionExtraInfo map[string]*string `json:"versionExtraInfo,omitempty" xml:"versionExtraInfo,omitempty"`
  // 版本的训练信息
  TrainingInfo map[string]*string `json:"trainingInfo,omitempty" xml:"trainingInfo,omitempty"`
  // 版本的推理参数
  InferenceParameters map[string]*string `json:"inferenceParameters,omitempty" xml:"inferenceParameters,omitempty"`
  // 版本的列 schema 定义
  FeatureColumns *ModelFieldSchema `json:"featureColumns,omitempty" xml:"featureColumns,omitempty"`
  // version 支持的所有 task 类型。要求：对于 LLM/MLLM 类型模型，可取值 text-generation，chat，sentence-embedding 中的一个或多个. 对于 BOOSTED_TREE_CLASSIFIER 类型模型，只能取值为 [predict, predict-proba, feature-importance]（顺序任意）. 对于 BOOSTED_TREE_REGRESSOR 类型模型，只能取值为 [predict, feature-importance]（顺序任意）
  Tasks []*string `json:"tasks,omitempty" xml:"tasks,omitempty" type:"Repeated"`
}

func (s Model) String() string {
  return tea.Prettify(s)
}

func (s Model) GoString() string {
  return s.String()
}

func (s *Model) SetName(v string) *Model {
  s.Name = &v
  return s
}

func (s *Model) SetModelName(v string) *Model {
  s.ModelName = &v
  return s
}

func (s *Model) SetVersionName(v string) *Model {
  s.VersionName = &v
  return s
}

func (s *Model) SetDefaultVersion(v string) *Model {
  s.DefaultVersion = &v
  return s
}

func (s *Model) SetCreateTime(v string) *Model {
  s.CreateTime = &v
  return s
}

func (s *Model) SetUpdateTime(v string) *Model {
  s.UpdateTime = &v
  return s
}

func (s *Model) SetVersionCreateTime(v string) *Model {
  s.VersionCreateTime = &v
  return s
}

func (s *Model) SetVersionUpdateTime(v string) *Model {
  s.VersionUpdateTime = &v
  return s
}

func (s *Model) SetDescription(v string) *Model {
  s.Description = &v
  return s
}

func (s *Model) SetVersionDescription(v string) *Model {
  s.VersionDescription = &v
  return s
}

func (s *Model) SetExpirationDays(v int) *Model {
  s.ExpirationDays = &v
  return s
}

func (s *Model) SetVersionExpirationDays(v int) *Model {
  s.VersionExpirationDays = &v
  return s
}

func (s *Model) SetSourceType(v string) *Model {
  s.SourceType = &v
  return s
}

func (s *Model) SetModelType(v string) *Model {
  s.ModelType = &v
  return s
}

func (s *Model) SetLabels(v map[string]*string) *Model {
  s.Labels = v
  return s
}

func (s *Model) SetTransform(v map[string]*string) *Model {
  s.Transform = v
  return s
}

func (s *Model) SetPath(v string) *Model {
  s.Path = &v
  return s
}

func (s *Model) SetOptions(v map[string]*string) *Model {
  s.Options = v
  return s
}

func (s *Model) SetExtraInfo(v map[string]*string) *Model {
  s.ExtraInfo = v
  return s
}

func (s *Model) SetVersionExtraInfo(v map[string]*string) *Model {
  s.VersionExtraInfo = v
  return s
}

func (s *Model) SetTrainingInfo(v map[string]*string) *Model {
  s.TrainingInfo = v
  return s
}

func (s *Model) SetInferenceParameters(v map[string]*string) *Model {
  s.InferenceParameters = v
  return s
}

func (s *Model) SetFeatureColumns(v *ModelFieldSchema) *Model {
  s.FeatureColumns = v
  return s
}

func (s *Model) SetTasks(v []*string) *Model {
  s.Tasks = v
  return s
}

// ModelFieldSchema 定义
type ModelFieldSchema struct {
  // 列名或 struct 字段名
  FieldName *string `json:"fieldName,omitempty" xml:"fieldName,omitempty"`
  // SQL DDL 中的列类型定义
  SqlTypeDefinition *string `json:"sqlTypeDefinition,omitempty" xml:"sqlTypeDefinition,omitempty"`
  // 字段类型
  TypeCategory *string `json:"typeCategory,omitempty" xml:"typeCategory,omitempty"`
  // 字段模式：REQUIRED 或 NULLABLE
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  // STRUCT 类型的子字段
  Fields []*ModelFieldSchema `json:"fields,omitempty" xml:"fields,omitempty" type:"Repeated"`
  // 列的 comment
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // CHAR/VARCHAR 类型的最大长度
  MaxLength *string `json:"maxLength,omitempty" xml:"maxLength,omitempty"`
  // DECIMAL 类型的精度
  Precision *string `json:"precision,omitempty" xml:"precision,omitempty"`
  // DECIMAL 类型的 scale
  Scale *string `json:"scale,omitempty" xml:"scale,omitempty"`
  // 默认值的表达式字符串
  DefaultValueExpression *string `json:"defaultValueExpression,omitempty" xml:"defaultValueExpression,omitempty"`
}

func (s ModelFieldSchema) String() string {
  return tea.Prettify(s)
}

func (s ModelFieldSchema) GoString() string {
  return s.String()
}

func (s *ModelFieldSchema) SetFieldName(v string) *ModelFieldSchema {
  s.FieldName = &v
  return s
}

func (s *ModelFieldSchema) SetSqlTypeDefinition(v string) *ModelFieldSchema {
  s.SqlTypeDefinition = &v
  return s
}

func (s *ModelFieldSchema) SetTypeCategory(v string) *ModelFieldSchema {
  s.TypeCategory = &v
  return s
}

func (s *ModelFieldSchema) SetMode(v string) *ModelFieldSchema {
  s.Mode = &v
  return s
}

func (s *ModelFieldSchema) SetFields(v []*ModelFieldSchema) *ModelFieldSchema {
  s.Fields = v
  return s
}

func (s *ModelFieldSchema) SetDescription(v string) *ModelFieldSchema {
  s.Description = &v
  return s
}

func (s *ModelFieldSchema) SetMaxLength(v string) *ModelFieldSchema {
  s.MaxLength = &v
  return s
}

func (s *ModelFieldSchema) SetPrecision(v string) *ModelFieldSchema {
  s.Precision = &v
  return s
}

func (s *ModelFieldSchema) SetScale(v string) *ModelFieldSchema {
  s.Scale = &v
  return s
}

func (s *ModelFieldSchema) SetDefaultValueExpression(v string) *ModelFieldSchema {
  s.DefaultValueExpression = &v
  return s
}

type ListModelsResponse struct {
  Models []*Model `json:"models,omitempty" xml:"models,omitempty" type:"Repeated"`
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListModelsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListModelsResponse) GoString() string {
  return s.String()
}

func (s *ListModelsResponse) SetModels(v []*Model) *ListModelsResponse {
  s.Models = v
  return s
}

func (s *ListModelsResponse) SetNextPageToken(v string) *ListModelsResponse {
  s.NextPageToken = &v
  return s
}

type ListModelVersionsResponse struct {
  Models []*Model `json:"models,omitempty" xml:"models,omitempty" type:"Repeated"`
  NextPageToken *string `json:"nextPageToken,omitempty" xml:"nextPageToken,omitempty"`
}

func (s ListModelVersionsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListModelVersionsResponse) GoString() string {
  return s.String()
}

func (s *ListModelVersionsResponse) SetModels(v []*Model) *ListModelVersionsResponse {
  s.Models = v
  return s
}

func (s *ListModelVersionsResponse) SetNextPageToken(v string) *ListModelVersionsResponse {
  s.NextPageToken = &v
  return s
}

type Client struct {
  openapi.Client
}

func NewClient(config *openapi.Config)(*Client, error) {
  client := new(Client)
  err := client.Init(config)
  return client, err
}

func (client *Client)Init(config *openapi.Config)(_err error) {
  _err = client.Client.Init(config  )
  if _err != nil {
    return _err
  }
  return nil
}



func (client *Client) UpdateTable (table *Table) (_result *Table, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &Table{}
  _body, _err := client.RequestWithModel(table, tea.String("PUT"), client.GetTablePath(table), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) DeleteTable (table *Table) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(table, tea.String("DELETE"), client.GetTablePath(table), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) CreateTable (table *Table) (_result *Table, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &Table{}
  _body, _err := client.RequestWithModel(table, tea.String("POST"), client.GetTablesPath(table), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetTable (table *Table) (_result *Table, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &Table{}
  _body, _err := client.RequestWithModel(table, tea.String("GET"), client.GetTablePath(table), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) ListTables (projectId *string, schemaName *string, pageSize *int32, pageToken *string) (_result *ListTablesResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/tables")
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListTablesResponse{}
  _body, _err := client.RequestWithModel(&ListTablesResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) SetTablePolicy (table *Table, policy *Policy) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetTablePath(table)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(policy, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetTablePolicy (table *Table) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetTablePath(table)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(&Policy{}, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetTablePath (table *Table) (_result *string) {
  if tea.BoolValue(util.IsUnset(table.SchemaName)) {
    _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(table.ProjectId) + "/schemas/default/tables/" + tea.StringValue(table.TableName))
    return _result
  } else {
    _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(table.ProjectId) + "/schemas/" + tea.StringValue(table.SchemaName) + "/tables/" + tea.StringValue(table.TableName))
    return _result
  }

}

func (client *Client) GetTablesPath (table *Table) (_result *string) {
  if tea.BoolValue(util.IsUnset(table.SchemaName)) {
    _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(table.ProjectId) + "/schemas/default/tables")
    return _result
  } else {
    _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(table.ProjectId) + "/schemas/" + tea.StringValue(table.SchemaName) + "/tables")
    return _result
  }

}

func (client *Client) CreateConnection (namespace *string, connection *Connection) (_result *Connection, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/connections")
  _result = &Connection{}
  _body, _err := client.RequestWithModel(connection, tea.String("POST"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) ListConnections (namespace *string, pageSize *int, pageToken *string) (_result *ListConnectionsResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/connections")
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListConnectionsResponse{}
  _body, _err := client.RequestWithModel(&ListConnectionsResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetConnection (namespace *string, connectionName *string) (_result *Connection, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetConnectionPath(namespace, connectionName)
  _result = &Connection{}
  _body, _err := client.RequestWithModel(&Connection{}, tea.String("GET"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) UpdateConnection (namespace *string, connectionName *string, connection *Connection, updateMask *string) (_result *Connection, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetConnectionPath(namespace, connectionName)
  query := make(map[string]*string)
  query["updateMask"] = updateMask
  _result = &Connection{}
  _body, _err := client.RequestWithModel(connection, tea.String("PATCH"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) DeleteConnection (namespace *string, connectionName *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetConnectionPath(namespace, connectionName)
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(&Connection{}, tea.String("DELETE"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) SetConnectionPolicy (namespace *string, connectionName *string, request *SetPolicyRequest) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetConnectionPath(namespace, connectionName)
  query := make(map[string]*string)
  query["method"] = tea.String("setPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(request, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetConnectionPolicy (namespace *string, connectionName *string) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetConnectionPath(namespace, connectionName)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(&Policy{}, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetConnectionPath (namespace *string, connectionName *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/connections/" + tea.StringValue(connectionName))
  return _result
}

// Path generation helper
func (client *Client) GetRolePath (namespace *string, roleName *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/roles/" + tea.StringValue(roleName))
  return _result
}

// Create role
func (client *Client) CreateRole (namespace *string, role *Role) (_result *Role, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/roles")
  _result = &Role{}
  _body, _err := client.RequestWithModel(role, tea.String("POST"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Delete role
func (client *Client) DeleteRole (namespace *string, roleName *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetRolePath(namespace, roleName)
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(&Role{}, tea.String("DELETE"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Get role
func (client *Client) GetRole (namespace *string, roleName *string, view *string) (_result *Role, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetRolePath(namespace, roleName)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(view)) {
    query["view"] = view
  }

  _result = &Role{}
  _body, _err := client.RequestWithModel(&Role{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// List roles
func (client *Client) ListRoles (namespace *string, pageSize *int, pageToken *string, view *string, showDeleted *bool) (_result *ListRolesResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/roles")
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  if !tea.BoolValue(util.IsUnset(view)) {
    query["view"] = view
  }

  if !tea.BoolValue(util.IsUnset(showDeleted)) {
    query["showDeleted"] = mcutil.ToString(showDeleted)
  }

  _result = &ListRolesResponse{}
  _body, _err := client.RequestWithModel(&ListRolesResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Update role
func (client *Client) UpdateRole (namespace *string, roleName *string, role *Role, updateMask *string) (_result *Role, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetRolePath(namespace, roleName)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(updateMask)) {
    query["updateMask"] = updateMask
  }

  _result = &Role{}
  _body, _err := client.RequestWithModel(role, tea.String("PATCH"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Set role policy
func (client *Client) SetRolePolicy (namespace *string, roleName *string, policy *Policy) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetRolePath(namespace, roleName)
  query := make(map[string]*string)
  query["method"] = tea.String("setPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(policy, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Get role policy
func (client *Client) GetRolePolicy (namespace *string, roleName *string) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetRolePath(namespace, roleName)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(&Policy{}, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Path generation helpers
func (client *Client) GetTaxonomyPath (namespace *string, taxonomyId *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/taxonomies/" + tea.StringValue(taxonomyId))
  return _result
}

func (client *Client) GetPolicyTagPath (namespace *string, taxonomyId *string, policyTagId *string) (_result *string) {
  _result = tea.String(tea.StringValue(client.GetTaxonomyPath(namespace, taxonomyId)) + "/policyTags/" + tea.StringValue(policyTagId))
  return _result
}

// Taxonomy operations
func (client *Client) CreateTaxonomy (namespace *string, taxonomy *Taxonomy) (_result *Taxonomy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/taxonomies")
  _result = &Taxonomy{}
  _body, _err := client.RequestWithModel(taxonomy, tea.String("POST"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) DeleteTaxonomy (namespace *string, taxonomyId *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetTaxonomyPath(namespace, taxonomyId)
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(&Taxonomy{}, tea.String("DELETE"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetTaxonomy (namespace *string, taxonomyId *string) (_result *Taxonomy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetTaxonomyPath(namespace, taxonomyId)
  _result = &Taxonomy{}
  _body, _err := client.RequestWithModel(&Taxonomy{}, tea.String("GET"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) ListTaxonomies (namespace *string, pageSize *int, pageToken *string) (_result *ListTaxonomiesResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/taxonomies")
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListTaxonomiesResponse{}
  _body, _err := client.RequestWithModel(&ListTaxonomiesResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) UpdateTaxonomy (namespace *string, taxonomyId *string, taxonomy *Taxonomy, updateMask *string) (_result *Taxonomy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetTaxonomyPath(namespace, taxonomyId)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(updateMask)) {
    query["updateMask"] = updateMask
  }

  _result = &Taxonomy{}
  _body, _err := client.RequestWithModel(taxonomy, tea.String("PATCH"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) SetTaxonomyPolicy (namespace *string, taxonomyId *string, policy *Policy) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetTaxonomyPath(namespace, taxonomyId)
  query := make(map[string]*string)
  query["method"] = tea.String("setPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(policy, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetTaxonomyPolicy (namespace *string, taxonomyId *string) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetTaxonomyPath(namespace, taxonomyId)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(&Policy{}, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// PolicyTag operations
func (client *Client) CreatePolicyTag (namespace *string, taxonomyId *string, policyTag *PolicyTag) (_result *PolicyTag, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String(tea.StringValue(client.GetTaxonomyPath(namespace, taxonomyId)) + "/policyTags")
  _result = &PolicyTag{}
  _body, _err := client.RequestWithModel(policyTag, tea.String("POST"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) DeletePolicyTag (namespace *string, taxonomyId *string, policyTagId *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetPolicyTagPath(namespace, taxonomyId, policyTagId)
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(&PolicyTag{}, tea.String("DELETE"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetPolicyTag (namespace *string, taxonomyId *string, policyTagId *string) (_result *PolicyTag, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetPolicyTagPath(namespace, taxonomyId, policyTagId)
  _result = &PolicyTag{}
  _body, _err := client.RequestWithModel(&PolicyTag{}, tea.String("GET"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) ListPolicyTags (namespace *string, taxonomyId *string, pageSize *int, pageToken *string) (_result *ListPolicyTagsResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String(tea.StringValue(client.GetTaxonomyPath(namespace, taxonomyId)) + "/policyTags")
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListPolicyTagsResponse{}
  _body, _err := client.RequestWithModel(&ListPolicyTagsResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) UpdatePolicyTag (namespace *string, taxonomyId *string, policyTagId *string, policyTag *PolicyTag, updateMask *string) (_result *PolicyTag, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetPolicyTagPath(namespace, taxonomyId, policyTagId)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(updateMask)) {
    query["updateMask"] = updateMask
  }

  _result = &PolicyTag{}
  _body, _err := client.RequestWithModel(policyTag, tea.String("PATCH"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) SetPolicyTagPolicy (namespace *string, taxonomyId *string, policyTagId *string, policy *Policy) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetPolicyTagPath(namespace, taxonomyId, policyTagId)
  query := make(map[string]*string)
  query["method"] = tea.String("setPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(policy, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetPolicyTagPolicy (namespace *string, taxonomyId *string, policyTagId *string) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetPolicyTagPath(namespace, taxonomyId, policyTagId)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(&Policy{}, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) CreateDataPolicy (namespace *string, dataPolicy *DataPolicy) (_result *DataPolicy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetDataPoliciesPath(namespace)
  _result = &DataPolicy{}
  _body, _err := client.RequestWithModel(dataPolicy, tea.String("POST"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) DeleteDataPolicy (namespace *string, dataPolicyName *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetDataPolicyPath(namespace, dataPolicyName)
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(&DataPolicy{}, tea.String("DELETE"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetDataPolicy (namespace *string, dataPolicyName *string) (_result *DataPolicy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetDataPolicyPath(namespace, dataPolicyName)
  _result = &DataPolicy{}
  _body, _err := client.RequestWithModel(&DataPolicy{}, tea.String("GET"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) ListDataPolicies (namespace *string, pageSize *int, pageToken *string) (_result *ListDataPoliciesResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetDataPoliciesPath(namespace)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListDataPoliciesResponse{}
  _body, _err := client.RequestWithModel(&ListDataPoliciesResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) SetDataPolicyPolicy (namespace *string, dataPolicyName *string, request *SetPolicyRequest) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetDataPolicyPath(namespace, dataPolicyName)
  query := make(map[string]*string)
  query["method"] = tea.String("setPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(request, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetDataPolicyPolicy (namespace *string, dataPolicyName *string) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetDataPolicyPath(namespace, dataPolicyName)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(&Policy{}, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetDataPolicyPath (namespace *string, dataPolicyName *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/dataPolicies/" + tea.StringValue(dataPolicyName))
  return _result
}

func (client *Client) GetDataPoliciesPath (namespace *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/dataPolicies")
  return _result
}

// Paths
func (client *Client) GetProjectPath (projectId *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId))
  return _result
}

func (client *Client) GetSchemaPath (projectId *string, schemaName *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName))
  return _result
}

// Methods
func (client *Client) ListProjects (pageSize *int, pageToken *string) (_result *ListProjectsResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListProjectsResponse{}
  _body, _err := client.RequestWithModel(&ListProjectsResponse{}, tea.String("GET"), tea.String("/api/catalog/v1alpha/projects"), query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetProject (projectId *string) (_result *Project, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &Project{}
  _body, _err := client.RequestWithModel(&Project{}, tea.String("GET"), client.GetProjectPath(projectId), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) CreateSchema (projectId *string, schema *Schema) (_result *Schema, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas")
  _result = &Schema{}
  _body, _err := client.RequestWithModel(schema, tea.String("POST"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) ListSchemas (projectId *string, pageSize *int, pageToken *string) (_result *ListSchemasResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas")
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListSchemasResponse{}
  _body, _err := client.RequestWithModel(&ListSchemasResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetSchema (projectId *string, schemaName *string) (_result *Schema, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &Schema{}
  _body, _err := client.RequestWithModel(&Schema{}, tea.String("GET"), client.GetSchemaPath(projectId, schemaName), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) UpdateSchema (projectId *string, schemaName *string, updateMask *string, schema *Schema) (_result *Schema, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetSchemaPath(projectId, schemaName)
  query := make(map[string]*string)
  query["updateMask"] = updateMask
  _result = &Schema{}
  _body, _err := client.RequestWithModel(schema, tea.String("PATCH"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) DeleteSchema (projectId *string, schemaName *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetSchemaPath(projectId, schemaName)
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(&Schema{}, tea.String("DELETE"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) SetSchemaPolicy (projectId *string, schemaName *string, policy *Policy) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetSchemaPath(projectId, schemaName)
  query := make(map[string]*string)
  query["method"] = tea.String("setPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(policy, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetSchemaPolicy (projectId *string, schemaName *string) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetSchemaPath(projectId, schemaName)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(&Policy{}, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Path Functions
func (client *Client) GetTablePartitionsPath (projectId *string, schemaName *string, tableName *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/tables/" + tea.StringValue(tableName) + "/partitions")
  return _result
}

// Methods
func (client *Client) ListPartitions (projectId *string, schemaName *string, tableName *string, pageSize *int, pageToken *string) (_result *ListPartitionsResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetTablePartitionsPath(projectId, schemaName, tableName)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListPartitionsResponse{}
  _body, _err := client.RequestWithModel(&ListPartitionsResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetDataScanPath (namespace *string, dataScanName *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/dataScans/" + tea.StringValue(dataScanName))
  return _result
}

func (client *Client) GetDataScansPath (namespace *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/dataScans")
  return _result
}

func (client *Client) GetTriggerDataScanPath (namespace *string, dataScanName *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/dataScans/" + tea.StringValue(dataScanName) + ":trigger")
  return _result
}

func (client *Client) TriggerDataScan (namespace *string, dataScanName *string) (_result *HttpResponse, _err error) {
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(&ScanJob{}, tea.String("POST"), client.GetTriggerDataScanPath(namespace, dataScanName), nil, &util.RuntimeOptions{})
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) UpdateDataScan (namespace *string, dataScan *DataScan, updateMask *string) (_result *DataScan, _err error) {
  runtime := &util.RuntimeOptions{}
  query := make(map[string]*string)
  query["updateMask"] = updateMask
  _result = &DataScan{}
  _body, _err := client.RequestWithModel(dataScan, tea.String("PATCH"), client.GetDataScanPath(namespace, dataScan.ScanName), query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) DeleteDataScan (namespace *string, dataScanName *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(&DataScan{}, tea.String("DELETE"), client.GetDataScanPath(namespace, dataScanName), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) CreateDataScan (namespace *string, dataScan *DataScan) (_result *DataScan, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &DataScan{}
  _body, _err := client.RequestWithModel(dataScan, tea.String("POST"), client.GetDataScansPath(namespace), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetDataScan (namespace *string, dataScanName *string) (_result *DataScan, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &DataScan{}
  _body, _err := client.RequestWithModel(&DataScan{}, tea.String("GET"), client.GetDataScanPath(namespace, dataScanName), nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) ListDataScans (namespace *string, pageSize *int32, pageToken *string) (_result *ListDataScansResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetDataScansPath(namespace)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListDataScansResponse{}
  _body, _err := client.RequestWithModel(&ListDataScansResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetDataScanJobsPath (namespace *string, dataScanName *string) (_result *string) {
  _result = tea.String("/api/catalog/v1alpha/namespaces/" + tea.StringValue(namespace) + "/dataScans/" + tea.StringValue(dataScanName) + "/scanJobs")
  return _result
}

func (client *Client) ListDataScanJobs (namespace *string, dataScanName *string, pageSize *int32, pageToken *string) (_result *ListDataScanJobsResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetDataScanJobsPath(namespace, dataScanName)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListDataScanJobsResponse{}
  _body, _err := client.RequestWithModel(&ListDataScanJobsResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 路径生成函数
func (client *Client) GetModelPath (projectId *string, schemaName *string, modelName *string, versionName *string) (_result *string) {
  if tea.BoolValue(util.IsUnset(versionName)) {
    _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/models/" + tea.StringValue(modelName))
    return _result
  } else {
    _result = tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/models/" + tea.StringValue(modelName) + "@" + tea.StringValue(versionName))
    return _result
  }

}

// 创建模型
func (client *Client) CreateModel (projectId *string, schemaName *string, model *Model) (_result *Model, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/models")
  _result = &Model{}
  _body, _err := client.RequestWithModel(model, tea.String("POST"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 列出模型
func (client *Client) ListModels (projectId *string, schemaName *string, pageSize *int, pageToken *string) (_result *ListModelsResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/models")
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListModelsResponse{}
  _body, _err := client.RequestWithModel(&ListModelsResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 获取模型
func (client *Client) GetModel (projectId *string, schemaName *string, modelName *string, versionName *string) (_result *Model, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetModelPath(projectId, schemaName, modelName, versionName)
  _result = &Model{}
  _body, _err := client.RequestWithModel(&Model{}, tea.String("GET"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 更新模型
func (client *Client) UpdateModel (projectId *string, schemaName *string, modelName *string, model *Model, updateMask *string, versionName *string) (_result *Model, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetModelPath(projectId, schemaName, modelName, versionName)
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(updateMask)) {
    query["updateMask"] = updateMask
  }

  _result = &Model{}
  _body, _err := client.RequestWithModel(model, tea.String("PATCH"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 删除模型
func (client *Client) DeleteModel (projectId *string, schemaName *string, modelName *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetModelPath(projectId, schemaName, modelName, nil)
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(nil, tea.String("DELETE"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 创建模型版本
func (client *Client) CreateModelVersion (projectId *string, schemaName *string, modelName *string, model *Model) (_result *Model, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/models/" + tea.StringValue(modelName) + ":createVersion")
  _result = &Model{}
  _body, _err := client.RequestWithModel(model, tea.String("POST"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 删除模型版本
func (client *Client) DeleteModelVersion (projectId *string, schemaName *string, modelName *string, versionName *string) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/models/" + tea.StringValue(modelName) + "@" + tea.StringValue(versionName) + ":deleteVersion")
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(nil, tea.String("DELETE"), path, nil, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 列出模型版本
func (client *Client) ListModelVersions (projectId *string, schemaName *string, modelName *string, pageSize *int, pageToken *string) (_result *ListModelVersionsResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  path := tea.String("/api/catalog/v1alpha/projects/" + tea.StringValue(projectId) + "/schemas/" + tea.StringValue(schemaName) + "/models/" + tea.StringValue(modelName) + ":listVersions")
  query := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(pageSize)) {
    query["pageSize"] = mcutil.ToString(pageSize)
  }

  if !tea.BoolValue(util.IsUnset(pageToken)) {
    query["pageToken"] = pageToken
  }

  _result = &ListModelVersionsResponse{}
  _body, _err := client.RequestWithModel(&ListModelVersionsResponse{}, tea.String("GET"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 获取模型策略
func (client *Client) GetModelPolicy (projectId *string, schemaName *string, modelName *string) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetModelPath(projectId, schemaName, modelName, nil)
  query := make(map[string]*string)
  query["method"] = tea.String("getPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(&Policy{}, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// 设置模型策略
func (client *Client) SetModelPolicy (projectId *string, schemaName *string, modelName *string, policy *Policy) (_result *Policy, _err error) {
  runtime := &util.RuntimeOptions{}
  path := client.GetModelPath(projectId, schemaName, modelName, nil)
  query := make(map[string]*string)
  query["method"] = tea.String("setPolicy")
  _result = &Policy{}
  _body, _err := client.RequestWithModel(policy, tea.String("POST"), path, query, runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

