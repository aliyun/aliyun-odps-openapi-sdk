# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class HttpResponse(TeaModel):
    """
    ==================================== Common ====================================\
    """
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: str = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class Binding(TeaModel):
    def __init__(
        self,
        role: str = None,
        members: List[str] = None,
    ):
        self.role = role
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['role'] = self.role
        if self.members is not None:
            result['members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('members') is not None:
            self.members = m.get('members')
        return self


class Policy(TeaModel):
    def __init__(
        self,
        etag: str = None,
        bindings: List[Binding] = None,
    ):
        self.etag = etag
        self.bindings = bindings

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['etag'] = self.etag
        result['bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['bindings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        self.bindings = []
        if m.get('bindings') is not None:
            for k in m.get('bindings'):
                temp_model = Binding()
                self.bindings.append(temp_model.from_map(k))
        return self


class SetPolicyRequest(TeaModel):
    def __init__(
        self,
        policy: Policy = None,
    ):
        # 设置的 Policy。
        self.policy = policy

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['policy'] = self.policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['policy'])
        return self


class PolicyTags(TeaModel):
    def __init__(
        self,
        names: List[str] = None,
    ):
        self.names = names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['names'] = self.names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('names') is not None:
            self.names = m.get('names')
        return self


class TableFieldSchema(TeaModel):
    """
    ==================================== Table ====================================\
    """
    def __init__(
        self,
        field_name: str = None,
        sql_type_definition: str = None,
        type_category: str = None,
        mode: str = None,
        fields: List['TableFieldSchema'] = None,
        description: str = None,
        policy_tags: PolicyTags = None,
        max_length: str = None,
        precision: str = None,
        scale: str = None,
        default_value_expression: str = None,
    ):
        # 列名（如果是顶层列），或者 struct 字段名。
        self.field_name = field_name
        # 在 SQL DDL 语句中填写的表示列类型的字符串定义。
        self.sql_type_definition = sql_type_definition
        # 字段类型。
        self.type_category = type_category
        # REQUIRED 或 NULLABLE。
        self.mode = mode
        # 如果是 STRUCT 类型，表示 STRUCT 的子字段。
        self.fields = fields
        # 列的评论。
        self.description = description
        # 可选。列绑定的 policy tag。
        self.policy_tags = policy_tags
        # 如果是 CHAR/VARCHAR 类型，表示字段的最大长度。
        self.max_length = max_length
        # 如果 DECIMAL 类型，表示精度。
        self.precision = precision
        # 如果 DECIMAL 类型，表示 scale。
        self.scale = scale
        # 可选。默认值的表达式字符串。
        self.default_value_expression = default_value_expression

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.policy_tags:
            self.policy_tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.sql_type_definition is not None:
            result['sqlTypeDefinition'] = self.sql_type_definition
        if self.type_category is not None:
            result['typeCategory'] = self.type_category
        if self.mode is not None:
            result['mode'] = self.mode
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.policy_tags is not None:
            result['policyTags'] = self.policy_tags.to_map()
        if self.max_length is not None:
            result['maxLength'] = self.max_length
        if self.precision is not None:
            result['precision'] = self.precision
        if self.scale is not None:
            result['scale'] = self.scale
        if self.default_value_expression is not None:
            result['defaultValueExpression'] = self.default_value_expression
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('sqlTypeDefinition') is not None:
            self.sql_type_definition = m.get('sqlTypeDefinition')
        if m.get('typeCategory') is not None:
            self.type_category = m.get('typeCategory')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = TableFieldSchema()
                self.fields.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('policyTags') is not None:
            temp_model = PolicyTags()
            self.policy_tags = temp_model.from_map(m['policyTags'])
        if m.get('maxLength') is not None:
            self.max_length = m.get('maxLength')
        if m.get('precision') is not None:
            self.precision = m.get('precision')
        if m.get('scale') is not None:
            self.scale = m.get('scale')
        if m.get('defaultValueExpression') is not None:
            self.default_value_expression = m.get('defaultValueExpression')
        return self


class Field(TeaModel):
    def __init__(
        self,
        field_name: str = None,
    ):
        # 列名（如果是顶层列），或者 struct 字段名。
        self.field_name = field_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        return self


class SortingField(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        order: str = None,
    ):
        # 列名（如果是顶层列），或者 struct 字段名。
        self.field_name = field_name
        # 排序顺序
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class Clustering(TeaModel):
    def __init__(
        self,
        type: str = None,
        fields: List[str] = None,
        num_buckets: str = None,
    ):
        # 表的聚簇类型，目前支持 hash/range。
        self.type = type
        # 聚簇列定义。
        self.fields = fields
        # 聚簇桶的个数。只有 hash clustering 才有此属性。创建 hash clustering 表时，如不指定桶个数，默认为 16。
        self.num_buckets = num_buckets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.fields is not None:
            result['fields'] = self.fields
        if self.num_buckets is not None:
            result['numBuckets'] = self.num_buckets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('numBuckets') is not None:
            self.num_buckets = m.get('numBuckets')
        return self


class Fields(TeaModel):
    def __init__(
        self,
        fields: List[str] = None,
    ):
        # 主键列名列表。
        self.fields = fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        return self


class TableConstraints(TeaModel):
    def __init__(
        self,
        primary_key: Fields = None,
    ):
        # 表的主键。系统不为主键自动去重。
        self.primary_key = primary_key

    def validate(self):
        if self.primary_key:
            self.primary_key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('primaryKey') is not None:
            temp_model = Fields()
            self.primary_key = temp_model.from_map(m['primaryKey'])
        return self


class PartitionedColumn(TeaModel):
    def __init__(
        self,
        field: str = None,
    ):
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['field'] = self.field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')
        return self


class PartitionDefinition(TeaModel):
    def __init__(
        self,
        partitioned_column: List[PartitionedColumn] = None,
    ):
        self.partitioned_column = partitioned_column

    def validate(self):
        if self.partitioned_column:
            for k in self.partitioned_column:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['partitionedColumn'] = []
        if self.partitioned_column is not None:
            for k in self.partitioned_column:
                result['partitionedColumn'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.partitioned_column = []
        if m.get('partitionedColumn') is not None:
            for k in m.get('partitionedColumn'):
                temp_model = PartitionedColumn()
                self.partitioned_column.append(temp_model.from_map(k))
        return self


class TableFormatDefinition(TeaModel):
    def __init__(
        self,
        transactional: bool = None,
        version: str = None,
    ):
        self.transactional = transactional
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transactional is not None:
            result['transactional'] = self.transactional
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transactional') is not None:
            self.transactional = m.get('transactional')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ExpirationOptions(TeaModel):
    def __init__(
        self,
        expiration_days: int = None,
        partition_expiration_days: int = None,
    ):
        self.expiration_days = expiration_days
        self.partition_expiration_days = partition_expiration_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_days is not None:
            result['expirationDays'] = self.expiration_days
        if self.partition_expiration_days is not None:
            result['partitionExpirationDays'] = self.partition_expiration_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationDays') is not None:
            self.expiration_days = m.get('expirationDays')
        if m.get('partitionExpirationDays') is not None:
            self.partition_expiration_days = m.get('partitionExpirationDays')
        return self


class ExternalDataConfiguration(TeaModel):
    def __init__(
        self,
        source_uris: List[str] = None,
        source_format: str = None,
        connection: str = None,
    ):
        # 表数据所在的 URI
        self.source_uris = source_uris
        # 支持格式：PAIMON/ICEBERG/ORC/PARQUET/CSV 等
        self.source_format = source_format
        # 关联的 Connection ID
        self.connection = connection

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_uris is not None:
            result['sourceUris'] = self.source_uris
        if self.source_format is not None:
            result['sourceFormat'] = self.source_format
        if self.connection is not None:
            result['connection'] = self.connection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceUris') is not None:
            self.source_uris = m.get('sourceUris')
        if m.get('sourceFormat') is not None:
            self.source_format = m.get('sourceFormat')
        if m.get('connection') is not None:
            self.connection = m.get('connection')
        return self


class Table(TeaModel):
    def __init__(
        self,
        etag: str = None,
        name: str = None,
        project_id: str = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
        description: str = None,
        table_schema: TableFieldSchema = None,
        clustering: Clustering = None,
        table_constraints: TableConstraints = None,
        partition_definition: PartitionDefinition = None,
        table_format_definition: TableFormatDefinition = None,
        create_time: str = None,
        last_modified_time: str = None,
        expiration_options: ExpirationOptions = None,
        labels: Dict[str, str] = None,
        external_data_configuration: ExternalDataConfiguration = None,
    ):
        # 用于 read-modify-write 一致性校验。
        self.etag = etag
        # 表的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/tables/{tableName}
        self.name = name
        # 表所属的 project ID。
        self.project_id = project_id
        # 表所属的 schema 名。
        self.schema_name = schema_name
        # 表名。
        self.table_name = table_name
        # 表的类型。
        self.type = type
        # 表的描述。等价于 SQL DDL 中表的 comment。
        self.description = description
        # 表列的 schema 定义。
        self.table_schema = table_schema
        # 表的 cluster 属性定义，只有 cluster 表才有。
        self.clustering = clustering
        # 表的主键约束定义，只有 delta 表才有。
        self.table_constraints = table_constraints
        # 表的分区列定义，只有分区表才有。
        self.partition_definition = partition_definition
        # 可选。仅内表有此字段。默认为普通表格式。
        self.table_format_definition = table_format_definition
        # 表的创建时间（毫秒）。仅输出。
        self.create_time = create_time
        # 表的修改时间（毫秒）。仅输出。
        self.last_modified_time = last_modified_time
        # 可选。表的过期时间配置。
        self.expiration_options = expiration_options
        # 可选。表上的标签。
        self.labels = labels
        # 外部表配置
        self.external_data_configuration = external_data_configuration

    def validate(self):
        if self.table_schema:
            self.table_schema.validate()
        if self.clustering:
            self.clustering.validate()
        if self.table_constraints:
            self.table_constraints.validate()
        if self.partition_definition:
            self.partition_definition.validate()
        if self.table_format_definition:
            self.table_format_definition.validate()
        if self.expiration_options:
            self.expiration_options.validate()
        if self.external_data_configuration:
            self.external_data_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['etag'] = self.etag
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        if self.description is not None:
            result['description'] = self.description
        if self.table_schema is not None:
            result['tableSchema'] = self.table_schema.to_map()
        if self.clustering is not None:
            result['clustering'] = self.clustering.to_map()
        if self.table_constraints is not None:
            result['tableConstraints'] = self.table_constraints.to_map()
        if self.partition_definition is not None:
            result['partitionDefinition'] = self.partition_definition.to_map()
        if self.table_format_definition is not None:
            result['tableFormatDefinition'] = self.table_format_definition.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.expiration_options is not None:
            result['expirationOptions'] = self.expiration_options.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.external_data_configuration is not None:
            result['externalDataConfiguration'] = self.external_data_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tableSchema') is not None:
            temp_model = TableFieldSchema()
            self.table_schema = temp_model.from_map(m['tableSchema'])
        if m.get('clustering') is not None:
            temp_model = Clustering()
            self.clustering = temp_model.from_map(m['clustering'])
        if m.get('tableConstraints') is not None:
            temp_model = TableConstraints()
            self.table_constraints = temp_model.from_map(m['tableConstraints'])
        if m.get('partitionDefinition') is not None:
            temp_model = PartitionDefinition()
            self.partition_definition = temp_model.from_map(m['partitionDefinition'])
        if m.get('tableFormatDefinition') is not None:
            temp_model = TableFormatDefinition()
            self.table_format_definition = temp_model.from_map(m['tableFormatDefinition'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('expirationOptions') is not None:
            temp_model = ExpirationOptions()
            self.expiration_options = temp_model.from_map(m['expirationOptions'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('externalDataConfiguration') is not None:
            temp_model = ExternalDataConfiguration()
            self.external_data_configuration = temp_model.from_map(m['externalDataConfiguration'])
        return self


class ListTablesResponse(TeaModel):
    def __init__(
        self,
        tables: List[Table] = None,
        next_page_token: str = None,
    ):
        self.tables = tables
        self.next_page_token = next_page_token

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['tables'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tables = []
        if m.get('tables') is not None:
            for k in m.get('tables'):
                temp_model = Table()
                self.tables.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class CloudResourceOptions(TeaModel):
    def __init__(
        self,
        delegated_account: str = None,
        ram_role_arn: str = None,
    ):
        # 被委托的账号名。在创建 connection 时自动保存为创建者的账号。
        self.delegated_account = delegated_account
        # 授权给 MaxCompute 服务扮演的 RAM 角色 ARN。
        self.ram_role_arn = ram_role_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegated_account is not None:
            result['delegatedAccount'] = self.delegated_account
        if self.ram_role_arn is not None:
            result['ramRoleArn'] = self.ram_role_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delegatedAccount') is not None:
            self.delegated_account = m.get('delegatedAccount')
        if m.get('ramRoleArn') is not None:
            self.ram_role_arn = m.get('ramRoleArn')
        return self


class Connection(TeaModel):
    """
    ==================================== Connection ====================================\
    """
    def __init__(
        self,
        name: str = None,
        connection_name: str = None,
        description: str = None,
        creation_time: str = None,
        last_modified_time: str = None,
        connection_type: str = None,
        cloud_resource: CloudResourceOptions = None,
        region: str = None,
    ):
        # 资源全局唯一名：namespaces/{namespace_ID}/connections/{connectionName}
        self.name = name
        # namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 32]。
        self.connection_name = connection_name
        # 可选。最多 1KB。
        self.description = description
        # Connection 的创建时间（毫秒）
        self.creation_time = creation_time
        # 最后修改时间（毫秒）
        self.last_modified_time = last_modified_time
        # Connection 的类型。必需项。
        self.connection_type = connection_type
        # 云上资源类型的 connection 对应的选项配置。仅当 connectionType 为 CLOUD_RESOURCE 时才设置。
        self.cloud_resource = cloud_resource
        # 此 connection 所属的 region。
        self.region = region

    def validate(self):
        if self.cloud_resource:
            self.cloud_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.connection_name is not None:
            result['connectionName'] = self.connection_name
        if self.description is not None:
            result['description'] = self.description
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.connection_type is not None:
            result['connectionType'] = self.connection_type
        if self.cloud_resource is not None:
            result['cloudResource'] = self.cloud_resource.to_map()
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('connectionName') is not None:
            self.connection_name = m.get('connectionName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('connectionType') is not None:
            self.connection_type = m.get('connectionType')
        if m.get('cloudResource') is not None:
            temp_model = CloudResourceOptions()
            self.cloud_resource = temp_model.from_map(m['cloudResource'])
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class ListConnectionsResponse(TeaModel):
    def __init__(
        self,
        connections: List[Connection] = None,
        next_page_token: str = None,
    ):
        self.connections = connections
        self.next_page_token = next_page_token

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['connections'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('connections') is not None:
            for k in m.get('connections'):
                temp_model = Connection()
                self.connections.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class Role(TeaModel):
    """
    ==================================== Role ====================================\
    """
    def __init__(
        self,
        name: str = None,
        role_name: str = None,
        description: str = None,
        included_permissions: List[str] = None,
        etag: str = None,
        deleted: bool = None,
    ):
        # 资源全局唯一名。e.g., namespaces/{namespace_ID}/roles/{roleName}
        self.name = name
        # namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。
        self.role_name = role_name
        # 可选。最多 1KB。
        self.description = description
        # Role 包含的权限。
        self.included_permissions = included_permissions
        # 用于一致性校验。
        self.etag = etag
        # 表示是否被删除。
        self.deleted = deleted
        # ListRolesResponse model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.description is not None:
            result['description'] = self.description
        if self.included_permissions is not None:
            result['includedPermissions'] = self.included_permissions
        if self.etag is not None:
            result['etag'] = self.etag
        if self.deleted is not None:
            result['deleted'] = self.deleted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('includedPermissions') is not None:
            self.included_permissions = m.get('includedPermissions')
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        roles: List[Role] = None,
        next_page_token: str = None,
    ):
        # 角色列表。
        self.roles = roles
        # 下一页的token。
        self.next_page_token = next_page_token
        # Path generation helper

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = Role()
                self.roles.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class Taxonomy(TeaModel):
    """
    ==================================== Taxonomy ====================================\
    """
    def __init__(
        self,
        name: str = None,
        taxonomy_name: str = None,
        description: str = None,
        activated_policy_types: List[str] = None,
        policy_tag_count: int = None,
        create_time: str = None,
        last_modified_time: str = None,
    ):
        # 资源全局唯一名。e.g., namespaces/{namespace_ID}/taxonomies/{ID}
        self.name = name
        # namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。
        self.taxonomy_name = taxonomy_name
        # 可选。最多 1KB。
        self.description = description
        # Taxonomy 下开启的 policy 类型列表，默认为 POLICY_TYPE_UNSPECIFIED
        self.activated_policy_types = activated_policy_types
        # 此 Taxonomy 内 policy tag 的个数。
        self.policy_tag_count = policy_tag_count
        # Taxonomy 的创建时间戳（毫秒）。仅输出。
        self.create_time = create_time
        # Taxonomy 的最后修改时间戳（毫秒）。仅输出。
        self.last_modified_time = last_modified_time
        # PolicyTag model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.taxonomy_name is not None:
            result['taxonomyName'] = self.taxonomy_name
        if self.description is not None:
            result['description'] = self.description
        if self.activated_policy_types is not None:
            result['activatedPolicyTypes'] = self.activated_policy_types
        if self.policy_tag_count is not None:
            result['policyTagCount'] = self.policy_tag_count
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('taxonomyName') is not None:
            self.taxonomy_name = m.get('taxonomyName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('activatedPolicyTypes') is not None:
            self.activated_policy_types = m.get('activatedPolicyTypes')
        if m.get('policyTagCount') is not None:
            self.policy_tag_count = m.get('policyTagCount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        return self


class PolicyTag(TeaModel):
    def __init__(
        self,
        name: str = None,
        policy_tag_name: str = None,
        description: str = None,
        parent_policy_tag: str = None,
        child_policy_tags: List[str] = None,
    ):
        # PolicyTag的完整路径。e.g., namespaces/{namespace_ID}/taxonomies/{TID}/policyTags/{ID}
        self.name = name
        # 父 Taxonomy 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。
        self.policy_tag_name = policy_tag_name
        # 可选。最多 1KB。
        self.description = description
        # 父节点的name。空代表根节点。
        self.parent_policy_tag = parent_policy_tag
        # 子节点的name列表。仅输出。
        self.child_policy_tags = child_policy_tags
        # List responses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.policy_tag_name is not None:
            result['policyTagName'] = self.policy_tag_name
        if self.description is not None:
            result['description'] = self.description
        if self.parent_policy_tag is not None:
            result['parentPolicyTag'] = self.parent_policy_tag
        if self.child_policy_tags is not None:
            result['childPolicyTags'] = self.child_policy_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyTagName') is not None:
            self.policy_tag_name = m.get('policyTagName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('parentPolicyTag') is not None:
            self.parent_policy_tag = m.get('parentPolicyTag')
        if m.get('childPolicyTags') is not None:
            self.child_policy_tags = m.get('childPolicyTags')
        return self


class ListTaxonomiesResponse(TeaModel):
    def __init__(
        self,
        taxonomies: List[Taxonomy] = None,
        next_page_token: str = None,
    ):
        # Taxonomy列表。
        self.taxonomies = taxonomies
        # 下一页的token。
        self.next_page_token = next_page_token

    def validate(self):
        if self.taxonomies:
            for k in self.taxonomies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['taxonomies'] = []
        if self.taxonomies is not None:
            for k in self.taxonomies:
                result['taxonomies'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.taxonomies = []
        if m.get('taxonomies') is not None:
            for k in m.get('taxonomies'):
                temp_model = Taxonomy()
                self.taxonomies.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class ListPolicyTagsResponse(TeaModel):
    def __init__(
        self,
        policy_tags: List[PolicyTag] = None,
        next_page_token: str = None,
    ):
        # PolicyTag列表。
        self.policy_tags = policy_tags
        # 下一页的token。
        self.next_page_token = next_page_token
        # Path generation helpers

    def validate(self):
        if self.policy_tags:
            for k in self.policy_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['policyTags'] = []
        if self.policy_tags is not None:
            for k in self.policy_tags:
                result['policyTags'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_tags = []
        if m.get('policyTags') is not None:
            for k in m.get('policyTags'):
                temp_model = PolicyTag()
                self.policy_tags.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class DataMaskingPolicy(TeaModel):
    def __init__(
        self,
        predefined_expression: str = None,
        parameters: List[str] = None,
    ):
        # 预定义脱敏策略的类型。
        self.predefined_expression = predefined_expression
        # 预定义脱敏策略的参数。
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_expression is not None:
            result['predefinedExpression'] = self.predefined_expression
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('predefinedExpression') is not None:
            self.predefined_expression = m.get('predefinedExpression')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class DataPolicy(TeaModel):
    """
    ==================================== DataPolicy ====================================\
    """
    def __init__(
        self,
        name: str = None,
        data_policy_name: str = None,
        policy_tag: str = None,
        data_policy_type: str = None,
        data_masking_policy: DataMaskingPolicy = None,
    ):
        # namespaces/{namespace_ID}/dataPolicies/{dataPolicyName}。仅输出。
        self.name = name
        # 用户指定的 data policy 名，在账号级唯一。
        self.data_policy_name = data_policy_name
        # Data policy 绑定的 policy tag 资源全名。
        self.policy_tag = policy_tag
        # data policy 的类型，目前仅支持 DATA_MASKING_POLICY 类型。
        self.data_policy_type = data_policy_type
        # Data policy 上定义的脱敏规则。
        self.data_masking_policy = data_masking_policy

    def validate(self):
        if self.data_masking_policy:
            self.data_masking_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.data_policy_name is not None:
            result['dataPolicyName'] = self.data_policy_name
        if self.policy_tag is not None:
            result['policyTag'] = self.policy_tag
        if self.data_policy_type is not None:
            result['dataPolicyType'] = self.data_policy_type
        if self.data_masking_policy is not None:
            result['dataMaskingPolicy'] = self.data_masking_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('dataPolicyName') is not None:
            self.data_policy_name = m.get('dataPolicyName')
        if m.get('policyTag') is not None:
            self.policy_tag = m.get('policyTag')
        if m.get('dataPolicyType') is not None:
            self.data_policy_type = m.get('dataPolicyType')
        if m.get('dataMaskingPolicy') is not None:
            temp_model = DataMaskingPolicy()
            self.data_masking_policy = temp_model.from_map(m['dataMaskingPolicy'])
        return self


class ListDataPoliciesResponse(TeaModel):
    def __init__(
        self,
        data_policies: List[DataPolicy] = None,
        next_page_token: str = None,
    ):
        self.data_policies = data_policies
        # 分页标记。
        self.next_page_token = next_page_token

    def validate(self):
        if self.data_policies:
            for k in self.data_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataPolicies'] = []
        if self.data_policies is not None:
            for k in self.data_policies:
                result['dataPolicies'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_policies = []
        if m.get('dataPolicies') is not None:
            for k in m.get('dataPolicies'):
                temp_model = DataPolicy()
                self.data_policies.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class Project(TeaModel):
    """
    ==================================== Project/Schema ====================================\
    """
    def __init__(
        self,
        name: str = None,
        project_id: str = None,
        owner: str = None,
        description: str = None,
        create_time: str = None,
        last_modified_time: str = None,
        schema_enabled: bool = None,
        region: str = None,
    ):
        # Project的资源全名：projects/{projectId}。仅输出。
        self.name = name
        # Project唯一ID
        self.project_id = project_id
        # Project的拥有者
        self.owner = owner
        # Project描述
        self.description = description
        # 创建时间戳（UTC毫秒）
        self.create_time = create_time
        # 最后修改时间戳（UTC毫秒）
        self.last_modified_time = last_modified_time
        # 是否开启三层模型
        self.schema_enabled = schema_enabled
        # 所属region
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.owner is not None:
            result['owner'] = self.owner
        if self.description is not None:
            result['description'] = self.description
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.schema_enabled is not None:
            result['schemaEnabled'] = self.schema_enabled
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('schemaEnabled') is not None:
            self.schema_enabled = m.get('schemaEnabled')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class ExternalCatalogSchemaOptions(TeaModel):
    def __init__(
        self,
        parameters: Dict[str, str] = None,
    ):
        # 外部schema属性配置
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class ExternalSchemaConfiguration(TeaModel):
    def __init__(
        self,
        connection: str = None,
        external_catalog_schema_options: ExternalCatalogSchemaOptions = None,
    ):
        # 关联的connection ID
        self.connection = connection
        # 外部catalog schema配置
        self.external_catalog_schema_options = external_catalog_schema_options

    def validate(self):
        if self.external_catalog_schema_options:
            self.external_catalog_schema_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection is not None:
            result['connection'] = self.connection
        if self.external_catalog_schema_options is not None:
            result['externalCatalogSchemaOptions'] = self.external_catalog_schema_options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connection') is not None:
            self.connection = m.get('connection')
        if m.get('externalCatalogSchemaOptions') is not None:
            temp_model = ExternalCatalogSchemaOptions()
            self.external_catalog_schema_options = temp_model.from_map(m['externalCatalogSchemaOptions'])
        return self


class Schema(TeaModel):
    def __init__(
        self,
        name: str = None,
        schema_name: str = None,
        description: str = None,
        type: str = None,
        owner: str = None,
        external_schema_configuration: ExternalSchemaConfiguration = None,
    ):
        # Schema的资源全名：projects/{projectId}/schemas/{schemaName}。仅输出。
        self.name = name
        # Project下唯一名称
        self.schema_name = schema_name
        # 可选描述，不超过xxKB
        self.description = description
        # Schema类型：DEFAULT/EXTERNAL
        self.type = type
        # Schema拥有者
        self.owner = owner
        # 外部schema配置
        self.external_schema_configuration = external_schema_configuration

    def validate(self):
        if self.schema_name is not None:
            self.validate_max_length(self.schema_name, 'schema_name', 128)
        if self.external_schema_configuration:
            self.external_schema_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        if self.owner is not None:
            result['owner'] = self.owner
        if self.external_schema_configuration is not None:
            result['externalSchemaConfiguration'] = self.external_schema_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('externalSchemaConfiguration') is not None:
            temp_model = ExternalSchemaConfiguration()
            self.external_schema_configuration = temp_model.from_map(m['externalSchemaConfiguration'])
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        projects: List[Project] = None,
        next_page_token: str = None,
    ):
        self.projects = projects
        self.next_page_token = next_page_token

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = Project()
                self.projects.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class ListSchemasResponse(TeaModel):
    def __init__(
        self,
        schemas: List[Schema] = None,
        next_page_token: str = None,
    ):
        self.schemas = schemas
        self.next_page_token = next_page_token
        # Paths

    def validate(self):
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['schemas'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.schemas = []
        if m.get('schemas') is not None:
            for k in m.get('schemas'):
                temp_model = Schema()
                self.schemas.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class Partition(TeaModel):
    """
    ==================================== Partition ====================================\
    """
    def __init__(
        self,
        spec: str = None,
    ):
        # 分区spec，格式样例为 bu=tt/ds=20250515
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ListPartitionsResponse(TeaModel):
    def __init__(
        self,
        partitions: List[Partition] = None,
        next_page_token: str = None,
    ):
        self.partitions = partitions
        self.next_page_token = next_page_token
        # Path Functions

    def validate(self):
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['partitions'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.partitions = []
        if m.get('partitions') is not None:
            for k in m.get('partitions'):
                temp_model = Partition()
                self.partitions.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class DataScanSource(TeaModel):
    """
    ==================================== DataScans ====================================\
    """
    def __init__(
        self,
        location: str = None,
        connection: str = None,
        ignores: List[str] = None,
    ):
        # location地址。支持oss、dlf 和 holo
        self.location = location
        # connection name。提供访问source需要的身份与网络信息。需要鉴权
        self.connection = connection
        # 忽略访问的路径。支持正则表达式
        self.ignores = ignores

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['location'] = self.location
        if self.connection is not None:
            result['connection'] = self.connection
        if self.ignores is not None:
            result['ignores'] = self.ignores
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('connection') is not None:
            self.connection = m.get('connection')
        if m.get('ignores') is not None:
            self.ignores = m.get('ignores')
        return self


class DataScanTarget(TeaModel):
    def __init__(
        self,
        project: str = None,
        schema: str = None,
        name_prefix: str = None,
        properties: str = None,
    ):
        # 结果写入的project name。
        self.project = project
        # 当dataScan.type为table时，table写入的schema
        self.schema = schema
        # 爬取任务自动生成的table/schema名称的前缀，防止命名冲突。
        self.name_prefix = name_prefix
        # 用户可指定的最终表 / schema 的属性
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project
        if self.schema is not None:
            result['schema'] = self.schema
        if self.name_prefix is not None:
            result['namePrefix'] = self.name_prefix
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('namePrefix') is not None:
            self.name_prefix = m.get('namePrefix')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self


class DataScanProperties(TeaModel):
    def __init__(
        self,
        format_filter: str = None,
        scan_mode: str = None,
        enable_stats: bool = None,
        options: str = None,
        pattern: str = None,
        update_policy: str = None,
        sync_remove: bool = None,
        auto_commit: bool = None,
    ):
        # AUTO/PARQUET/ORC/JSON/CSV。只爬取对应属性的数据。若指定，则忽略其他类型的文件。auto为不指定属性自动探测。
        self.format_filter = format_filter
        # enum	SAMPLE/TOTAL。 默认为SAMPLE。扫描时抽样扫描或者完整扫描
        self.scan_mode = scan_mode
        # 是否统计信息用于查询优化
        self.enable_stats = enable_stats
        # 其余的配置可选项，如csv格式下的一些额外选项
        self.options = options
        # 分区路径识别的pattern, 例如{table}/{part1}={value1}/{part2}={value2}
        self.pattern = pattern
        # 发现表元数据发生变化时的处理策略。APPEND_ONLY/OVERWRITE/IGNORE
        self.update_policy = update_policy
        # 发现表删除时是否自动删除
        self.sync_remove = sync_remove
        # false代表爬取任务只输出结果，不提交ddl
        self.auto_commit = auto_commit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format_filter is not None:
            result['formatFilter'] = self.format_filter
        if self.scan_mode is not None:
            result['scanMode'] = self.scan_mode
        if self.enable_stats is not None:
            result['enableStats'] = self.enable_stats
        if self.options is not None:
            result['options'] = self.options
        if self.pattern is not None:
            result['options'] = self.pattern
        if self.update_policy is not None:
            result['updatePolicy'] = self.update_policy
        if self.sync_remove is not None:
            result['syncRemove'] = self.sync_remove
        if self.auto_commit is not None:
            result['autoCommit'] = self.auto_commit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formatFilter') is not None:
            self.format_filter = m.get('formatFilter')
        if m.get('scanMode') is not None:
            self.scan_mode = m.get('scanMode')
        if m.get('enableStats') is not None:
            self.enable_stats = m.get('enableStats')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('options') is not None:
            self.pattern = m.get('options')
        if m.get('updatePolicy') is not None:
            self.update_policy = m.get('updatePolicy')
        if m.get('syncRemove') is not None:
            self.sync_remove = m.get('syncRemove')
        if m.get('autoCommit') is not None:
            self.auto_commit = m.get('autoCommit')
        return self


class DataScan(TeaModel):
    def __init__(
        self,
        name: str = None,
        scan_name: str = None,
        type: str = None,
        creator: str = None,
        customer_id: str = None,
        namespace_id: str = None,
        description: str = None,
        scan_id: str = None,
        creation_time: int = None,
        last_modified_time: int = None,
        last_triggered_time: int = None,
        last_triggered_by: str = None,
        scheduling_status: str = None,
        source: DataScanSource = None,
        target: DataScanTarget = None,
        properties: DataScanProperties = None,
        scheduler_mode: str = None,
        scheduler_interval: str = None,
    ):
        # 资源全局唯一名。e.g., namespaces/{namespaceID}/dataScans/{dataScanName}
        self.name = name
        # 用户指定的爬取任务名称
        self.scan_name = scan_name
        # 取值范围为：TABLE_DISCOVERY, SCHEMA_DISCOVERY
        self.type = type
        # dataScan 的创建者
        self.creator = creator
        # 客户 ID
        self.customer_id = customer_id
        # dataScan 所属的 namespace
        self.namespace_id = namespace_id
        # 用户自定义的描述
        self.description = description
        # 系统自动生成的 scan ID，只读字段。展示项
        self.scan_id = scan_id
        # 创建的时间，UTC timestamp
        self.creation_time = creation_time
        # 上次修改的时间，UTC timestamp
        self.last_modified_time = last_modified_time
        # 爬取任务上次触发的时间（开始调度时间），UTC timestamp。未触发过默认值为 0
        self.last_triggered_time = last_triggered_time
        # 触发当前调度的来源；具体用户或调度器
        self.last_triggered_by = last_triggered_by
        # dataScan 对象的调度状态。包含 IDLE/IMMEDIATE/PENDING/SCHEDULING 四种状态。dataScan 初始化状态为 IDLE，如果创建后立刻执行，设置为 IMMEDIATE
        self.scheduling_status = scheduling_status
        # 元数据爬取和发现来源，包括 location、connection 等信息
        self.source = source
        # 控制 dataScan 发现结果写入的参数，包含 project、namePrefix、以及透传的 Tbl Properties 等
        self.target = target
        # 爬取任务的可选参数，包含更新策略、分类器等
        self.properties = properties
        # manual/periodic，手动触发或者周期性自动触发
        self.scheduler_mode = scheduler_mode
        # 当 schedulerMode 为 periodic 时，两次爬取任务之间间隔的最大间隔，取值为 [1h-7d]
        self.scheduler_interval = scheduler_interval

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()
        if self.properties:
            self.properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.scan_name is not None:
            result['scanName'] = self.scan_name
        if self.type is not None:
            result['type'] = self.type
        if self.creator is not None:
            result['creator'] = self.creator
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id
        if self.description is not None:
            result['description'] = self.description
        if self.scan_id is not None:
            result['scanId'] = self.scan_id
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.last_triggered_time is not None:
            result['lastTriggeredTime'] = self.last_triggered_time
        if self.last_triggered_by is not None:
            result['lastTriggeredBy'] = self.last_triggered_by
        if self.scheduling_status is not None:
            result['schedulingStatus'] = self.scheduling_status
        if self.source is not None:
            result['source'] = self.source.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.properties is not None:
            result['properties'] = self.properties.to_map()
        if self.scheduler_mode is not None:
            result['schedulerMode'] = self.scheduler_mode
        if self.scheduler_interval is not None:
            result['schedulerInterval'] = self.scheduler_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scanName') is not None:
            self.scan_name = m.get('scanName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('scanId') is not None:
            self.scan_id = m.get('scanId')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('lastTriggeredTime') is not None:
            self.last_triggered_time = m.get('lastTriggeredTime')
        if m.get('lastTriggeredBy') is not None:
            self.last_triggered_by = m.get('lastTriggeredBy')
        if m.get('schedulingStatus') is not None:
            self.scheduling_status = m.get('schedulingStatus')
        if m.get('source') is not None:
            temp_model = DataScanSource()
            self.source = temp_model.from_map(m['source'])
        if m.get('target') is not None:
            temp_model = DataScanTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('properties') is not None:
            temp_model = DataScanProperties()
            self.properties = temp_model.from_map(m['properties'])
        if m.get('schedulerMode') is not None:
            self.scheduler_mode = m.get('schedulerMode')
        if m.get('schedulerInterval') is not None:
            self.scheduler_interval = m.get('schedulerInterval')
        return self


class ScanJob(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        namespace_id: str = None,
        data_scan_id: str = None,
        data_scan_name: str = None,
        triggered_by: str = None,
        start_time: int = None,
        end_time: int = None,
        status: str = None,
        status_detail: str = None,
        ddl: str = None,
        stats: str = None,
    ):
        # Job ID
        self.job_id = job_id
        # 作业所属的 namespace
        self.namespace_id = namespace_id
        # 系统自动生成的 dataScan ID
        self.data_scan_id = data_scan_id
        # 所属爬取任务名称。此处为全称 namespace/$nsId/dataScan/$scanName
        self.data_scan_name = data_scan_name
        # 触发此次爬取作业的人，定时触发则为 scheduler
        self.triggered_by = triggered_by
        # 爬取作业开始时间，UTC timestamp
        self.start_time = start_time
        # 爬取作业结束时间，UTC timestamp
        self.end_time = end_time
        # 爬取作业状态，取值范围：Created/Running/Terminated/Failed
        self.status = status
        # 爬取作业状态详细信息，如报错信息
        self.status_detail = status_detail
        # 爬取作业返回的需要提交的 DDL 信息
        self.ddl = ddl
        # 爬取作业返回的 stats 信息，JSON 格式
        self.stats = stats

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id
        if self.data_scan_id is not None:
            result['dataScanId'] = self.data_scan_id
        if self.data_scan_name is not None:
            result['dataScanName'] = self.data_scan_name
        if self.triggered_by is not None:
            result['triggeredBy'] = self.triggered_by
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_detail is not None:
            result['statusDetail'] = self.status_detail
        if self.ddl is not None:
            result['ddl'] = self.ddl
        if self.stats is not None:
            result['stats'] = self.stats
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')
        if m.get('dataScanId') is not None:
            self.data_scan_id = m.get('dataScanId')
        if m.get('dataScanName') is not None:
            self.data_scan_name = m.get('dataScanName')
        if m.get('triggeredBy') is not None:
            self.triggered_by = m.get('triggeredBy')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusDetail') is not None:
            self.status_detail = m.get('statusDetail')
        if m.get('ddl') is not None:
            self.ddl = m.get('ddl')
        if m.get('stats') is not None:
            self.stats = m.get('stats')
        return self


class ListDataScansResponse(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        data_scans: List[DataScan] = None,
    ):
        # 分页 token
        self.next_page_token = next_page_token
        # 返回所有的 dataScans 列表。
        self.data_scans = data_scans

    def validate(self):
        if self.data_scans:
            for k in self.data_scans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        result['dataScans'] = []
        if self.data_scans is not None:
            for k in self.data_scans:
                result['dataScans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        self.data_scans = []
        if m.get('dataScans') is not None:
            for k in m.get('dataScans'):
                temp_model = DataScan()
                self.data_scans.append(temp_model.from_map(k))
        return self


class ListDataScanJobsResponse(TeaModel):
    def __init__(
        self,
        scan_jobs: List[ScanJob] = None,
        next_page_token: str = None,
    ):
        # 返回所有的 dataScan jobs 列表
        self.scan_jobs = scan_jobs
        # 分页 token
        self.next_page_token = next_page_token

    def validate(self):
        if self.scan_jobs:
            for k in self.scan_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['scanJobs'] = []
        if self.scan_jobs is not None:
            for k in self.scan_jobs:
                result['scanJobs'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scan_jobs = []
        if m.get('scanJobs') is not None:
            for k in m.get('scanJobs'):
                temp_model = ScanJob()
                self.scan_jobs.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class ModelFieldSchema(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        sql_type_definition: str = None,
        type_category: str = None,
        mode: str = None,
        fields: List['ModelFieldSchema'] = None,
        description: str = None,
        max_length: str = None,
        precision: str = None,
        scale: str = None,
        default_value_expression: str = None,
    ):
        # 列名或 struct 字段名
        self.field_name = field_name
        # SQL DDL 中的列类型定义
        self.sql_type_definition = sql_type_definition
        # 字段类型
        self.type_category = type_category
        # 字段模式：REQUIRED 或 NULLABLE
        self.mode = mode
        # STRUCT 类型的子字段
        self.fields = fields
        # 列的 comment
        self.description = description
        # CHAR/VARCHAR 类型的最大长度
        self.max_length = max_length
        # DECIMAL 类型的精度
        self.precision = precision
        # DECIMAL 类型的 scale
        self.scale = scale
        # 默认值的表达式字符串
        self.default_value_expression = default_value_expression

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.sql_type_definition is not None:
            result['sqlTypeDefinition'] = self.sql_type_definition
        if self.type_category is not None:
            result['typeCategory'] = self.type_category
        if self.mode is not None:
            result['mode'] = self.mode
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.max_length is not None:
            result['maxLength'] = self.max_length
        if self.precision is not None:
            result['precision'] = self.precision
        if self.scale is not None:
            result['scale'] = self.scale
        if self.default_value_expression is not None:
            result['defaultValueExpression'] = self.default_value_expression
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('sqlTypeDefinition') is not None:
            self.sql_type_definition = m.get('sqlTypeDefinition')
        if m.get('typeCategory') is not None:
            self.type_category = m.get('typeCategory')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = ModelFieldSchema()
                self.fields.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('maxLength') is not None:
            self.max_length = m.get('maxLength')
        if m.get('precision') is not None:
            self.precision = m.get('precision')
        if m.get('scale') is not None:
            self.scale = m.get('scale')
        if m.get('defaultValueExpression') is not None:
            self.default_value_expression = m.get('defaultValueExpression')
        return self


class Model(TeaModel):
    """
    ==================================== Models ====================================\
    """
    def __init__(
        self,
        name: str = None,
        model_name: str = None,
        version_name: str = None,
        default_version: str = None,
        create_time: str = None,
        update_time: str = None,
        version_create_time: str = None,
        version_update_time: str = None,
        description: str = None,
        version_description: str = None,
        expiration_days: int = None,
        version_expiration_days: int = None,
        source_type: str = None,
        model_type: str = None,
        labels: Dict[str, str] = None,
        transform: Dict[str, str] = None,
        path: str = None,
        options: Dict[str, str] = None,
        extra_info: Dict[str, str] = None,
        version_extra_info: Dict[str, str] = None,
        training_info: Dict[str, str] = None,
        inference_parameters: Dict[str, str] = None,
        feature_columns: ModelFieldSchema = None,
        tasks: List[str] = None,
    ):
        # 模型的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/models/{modelName}
        self.name = name
        # 模型名。上级 Schema 内唯一。大小写不敏感。包含字符：[a-z][A-Z][0-9]_，字节个数范围 [3, 255]
        self.model_name = model_name
        # 版本名。同一 model 范围内唯一。大小写不敏感。包含字符：[a-z][A-Z][0-9]_，字节个数范围 [3, 255]
        self.version_name = version_name
        # 模型的默认版本名
        self.default_version = default_version
        # 模型的创建时间（毫秒）
        self.create_time = create_time
        # 模型的修改时间（毫秒）
        self.update_time = update_time
        # 版本的创建时间（毫秒）
        self.version_create_time = version_create_time
        # 版本的修改时间（毫秒）
        self.version_update_time = version_update_time
        # 模型的描述，最长 1KB
        self.description = description
        # 版本的描述，最长 1KB
        self.version_description = version_description
        # 模型基于最近更新时间的生命周期（天）
        self.expiration_days = expiration_days
        # 版本基于最近更新时间的生命周期（天）
        self.version_expiration_days = version_expiration_days
        # 模型的来源类型，创建后不支持修改
        self.source_type = source_type
        # 模型的类型，创建后不支持修改
        self.model_type = model_type
        # 模型的标签
        self.labels = labels
        # 版本的预处理信息
        self.transform = transform
        # 版本对应模型文件的路径
        self.path = path
        # 版本的参数
        self.options = options
        # 模型的额外信息
        self.extra_info = extra_info
        # 版本的额外信息
        self.version_extra_info = version_extra_info
        # 版本的训练信息
        self.training_info = training_info
        # 版本的推理参数
        self.inference_parameters = inference_parameters
        # 版本的列 schema 定义
        self.feature_columns = feature_columns
        # version 支持的所有 task 类型。要求：对于 LLM/MLLM 类型模型，可取值 text-generation，chat，sentence-embedding 中的一个或多个. 对于 BOOSTED_TREE_CLASSIFIER 类型模型，只能取值为 [predict, predict-proba, feature-importance]（顺序任意）. 对于 BOOSTED_TREE_REGRESSOR 类型模型，只能取值为 [predict, feature-importance]（顺序任意）
        self.tasks = tasks

    def validate(self):
        if self.feature_columns:
            self.feature_columns.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.version_name is not None:
            result['versionName'] = self.version_name
        if self.default_version is not None:
            result['defaultVersion'] = self.default_version
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.version_create_time is not None:
            result['versionCreateTime'] = self.version_create_time
        if self.version_update_time is not None:
            result['versionUpdateTime'] = self.version_update_time
        if self.description is not None:
            result['description'] = self.description
        if self.version_description is not None:
            result['versionDescription'] = self.version_description
        if self.expiration_days is not None:
            result['expirationDays'] = self.expiration_days
        if self.version_expiration_days is not None:
            result['versionExpirationDays'] = self.version_expiration_days
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.model_type is not None:
            result['modelType'] = self.model_type
        if self.labels is not None:
            result['labels'] = self.labels
        if self.transform is not None:
            result['transform'] = self.transform
        if self.path is not None:
            result['path'] = self.path
        if self.options is not None:
            result['options'] = self.options
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.version_extra_info is not None:
            result['versionExtraInfo'] = self.version_extra_info
        if self.training_info is not None:
            result['trainingInfo'] = self.training_info
        if self.inference_parameters is not None:
            result['inferenceParameters'] = self.inference_parameters
        if self.feature_columns is not None:
            result['featureColumns'] = self.feature_columns.to_map()
        if self.tasks is not None:
            result['tasks'] = self.tasks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('versionName') is not None:
            self.version_name = m.get('versionName')
        if m.get('defaultVersion') is not None:
            self.default_version = m.get('defaultVersion')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('versionCreateTime') is not None:
            self.version_create_time = m.get('versionCreateTime')
        if m.get('versionUpdateTime') is not None:
            self.version_update_time = m.get('versionUpdateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')
        if m.get('expirationDays') is not None:
            self.expiration_days = m.get('expirationDays')
        if m.get('versionExpirationDays') is not None:
            self.version_expiration_days = m.get('versionExpirationDays')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('transform') is not None:
            self.transform = m.get('transform')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('versionExtraInfo') is not None:
            self.version_extra_info = m.get('versionExtraInfo')
        if m.get('trainingInfo') is not None:
            self.training_info = m.get('trainingInfo')
        if m.get('inferenceParameters') is not None:
            self.inference_parameters = m.get('inferenceParameters')
        if m.get('featureColumns') is not None:
            temp_model = ModelFieldSchema()
            self.feature_columns = temp_model.from_map(m['featureColumns'])
        if m.get('tasks') is not None:
            self.tasks = m.get('tasks')
        return self


class ListModelsResponse(TeaModel):
    def __init__(
        self,
        models: List[Model] = None,
        next_page_token: str = None,
    ):
        self.models = models
        self.next_page_token = next_page_token

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['models'] = []
        if self.models is not None:
            for k in self.models:
                result['models'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.models = []
        if m.get('models') is not None:
            for k in m.get('models'):
                temp_model = Model()
                self.models.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


class ListModelVersionsResponse(TeaModel):
    def __init__(
        self,
        models: List[Model] = None,
        next_page_token: str = None,
    ):
        self.models = models
        self.next_page_token = next_page_token
        # 路径生成函数

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['models'] = []
        if self.models is not None:
            for k in self.models:
                result['models'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.models = []
        if m.get('models') is not None:
            for k in m.get('models'):
                temp_model = Model()
                self.models.append(temp_model.from_map(k))
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')
        return self


