// This file is auto-generated, don't edit it. Thanks.
package client

import (
  openapi  "github.com/aliyun/aliyun-odps-openapi-sdk/common/go/client"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  "github.com/alibabacloud-go/tea/tea"
)

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
  PolicyTags *PolicyTag `json:"policyTags,omitempty" xml:"policyTags,omitempty"`
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

func (s *TableFieldSchema) SetPolicyTags(v *PolicyTag) *TableFieldSchema {
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

type PolicyTag struct {
  Names []*string `json:"names,omitempty" xml:"names,omitempty" type:"Repeated"`
}

func (s PolicyTag) String() string {
  return tea.Prettify(s)
}

func (s PolicyTag) GoString() string {
  return s.String()
}

func (s *PolicyTag) SetNames(v []*string) *PolicyTag {
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
  PartitionedColumn []*PartitionedColumn `json:"partitionedColumn,omitempty" xml:"partitionedColumn,omitempty" type:"Repeated"`
}

func (s PartitionDefinition) String() string {
  return tea.Prettify(s)
}

func (s PartitionDefinition) GoString() string {
  return s.String()
}

func (s *PartitionDefinition) SetPartitionedColumn(v []*PartitionedColumn) *PartitionDefinition {
  s.PartitionedColumn = v
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

type Table struct {
  // 用于 read-modify-write 一致性校验。
  Etag *string `json:"etag,omitempty" xml:"etag,omitempty"`
  // 表的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/tables/{tableName}
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // 表所属的 project ID。
  ProjectId *string `json:"projectId,omitempty" xml:"projectId,omitempty" require:"true"`
  // 表所属的 schema 名。
  SchemaName *string `json:"schemaName,omitempty" xml:"schemaName,omitempty"`
  // 表名。
  TableName *string `json:"tableName,omitempty" xml:"tableName,omitempty" require:"true"`
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
  _body, _err := client.RequestWithModel(table, tea.String("PUT"), client.GetTablePath(table), runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) DeleteTable (table *Table) (_result *HttpResponse, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &HttpResponse{}
  _body, _err := client.RequestWithoutModel(table, tea.String("DELETE"), client.GetTablePath(table), runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) CreateTable (table *Table) (_result *Table, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &Table{}
  _body, _err := client.RequestWithModel(table, tea.String("POST"), client.GetTablesPath(table), runtime)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

func (client *Client) GetTable (table *Table) (_result *Table, _err error) {
  runtime := &util.RuntimeOptions{}
  _result = &Table{}
  _body, _err := client.RequestWithModel(table, tea.String("GET"), client.GetTablePath(table), runtime)
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

