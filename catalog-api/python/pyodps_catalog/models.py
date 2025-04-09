# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class PolicyTag(TeaModel):
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
    def __init__(
        self,
        field_name: str = None,
        sql_type_definition: str = None,
        type_category: str = None,
        mode: str = None,
        fields: List['TableFieldSchema'] = None,
        description: str = None,
        policy_tags: PolicyTag = None,
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
            temp_model = PolicyTag()
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

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.table_name, 'table_name')
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
        return self


class HttpResponse(TeaModel):
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


