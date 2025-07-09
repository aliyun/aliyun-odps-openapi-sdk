// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class Table extends TeaModel {
    /**
     * <p>用于 read-modify-write 一致性校验。</p>
     */
    @NameInMap("etag")
    public String etag;

    /**
     * <p>表的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/tables/{tableName}</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>表所属的 project ID。</p>
     */
    @NameInMap("projectId")
    @Validation(required = true)
    public String projectId;

    /**
     * <p>表所属的 schema 名。</p>
     */
    @NameInMap("schemaName")
    public String schemaName;

    /**
     * <p>表名。</p>
     */
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    /**
     * <p>表的类型。</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>表的描述。等价于 SQL DDL 中表的 comment。</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>表列的 schema 定义。</p>
     */
    @NameInMap("tableSchema")
    public TableFieldSchema tableSchema;

    /**
     * <p>表的 cluster 属性定义，只有 cluster 表才有。</p>
     */
    @NameInMap("clustering")
    public Clustering clustering;

    /**
     * <p>表的主键约束定义，只有 delta 表才有。</p>
     */
    @NameInMap("tableConstraints")
    public TableConstraints tableConstraints;

    /**
     * <p>表的分区列定义，只有分区表才有。</p>
     */
    @NameInMap("partitionDefinition")
    public PartitionDefinition partitionDefinition;

    /**
     * <p>可选。仅内表有此字段。默认为普通表格式。</p>
     */
    @NameInMap("tableFormatDefinition")
    public TableFormatDefinition tableFormatDefinition;

    /**
     * <p>表的创建时间（毫秒）。仅输出。</p>
     */
    @NameInMap("createTime")
    public String createTime;

    /**
     * <p>表的修改时间（毫秒）。仅输出。</p>
     */
    @NameInMap("lastModifiedTime")
    public String lastModifiedTime;

    /**
     * <p>可选。表的过期时间配置。</p>
     */
    @NameInMap("expirationOptions")
    public ExpirationOptions expirationOptions;

    /**
     * <p>可选。表上的标签。</p>
     */
    @NameInMap("labels")
    public java.util.Map<String, String> labels;

    /**
     * <p>外部表配置</p>
     */
    @NameInMap("externalDataConfiguration")
    public ExternalDataConfiguration externalDataConfiguration;

    // 新增字段
    public static Table build(java.util.Map<String, ?> map) throws Exception {
        Table self = new Table();
        return TeaModel.build(map, self);
    }

    public Table setEtag(String etag) {
        this.etag = etag;
        return this;
    }
    public String getEtag() {
        return this.etag;
    }

    public Table setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public Table setProjectId(String projectId) {
        this.projectId = projectId;
        return this;
    }
    public String getProjectId() {
        return this.projectId;
    }

    public Table setSchemaName(String schemaName) {
        this.schemaName = schemaName;
        return this;
    }
    public String getSchemaName() {
        return this.schemaName;
    }

    public Table setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public Table setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public Table setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public Table setTableSchema(TableFieldSchema tableSchema) {
        this.tableSchema = tableSchema;
        return this;
    }
    public TableFieldSchema getTableSchema() {
        return this.tableSchema;
    }

    public Table setClustering(Clustering clustering) {
        this.clustering = clustering;
        return this;
    }
    public Clustering getClustering() {
        return this.clustering;
    }

    public Table setTableConstraints(TableConstraints tableConstraints) {
        this.tableConstraints = tableConstraints;
        return this;
    }
    public TableConstraints getTableConstraints() {
        return this.tableConstraints;
    }

    public Table setPartitionDefinition(PartitionDefinition partitionDefinition) {
        this.partitionDefinition = partitionDefinition;
        return this;
    }
    public PartitionDefinition getPartitionDefinition() {
        return this.partitionDefinition;
    }

    public Table setTableFormatDefinition(TableFormatDefinition tableFormatDefinition) {
        this.tableFormatDefinition = tableFormatDefinition;
        return this;
    }
    public TableFormatDefinition getTableFormatDefinition() {
        return this.tableFormatDefinition;
    }

    public Table setCreateTime(String createTime) {
        this.createTime = createTime;
        return this;
    }
    public String getCreateTime() {
        return this.createTime;
    }

    public Table setLastModifiedTime(String lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
        return this;
    }
    public String getLastModifiedTime() {
        return this.lastModifiedTime;
    }

    public Table setExpirationOptions(ExpirationOptions expirationOptions) {
        this.expirationOptions = expirationOptions;
        return this;
    }
    public ExpirationOptions getExpirationOptions() {
        return this.expirationOptions;
    }

    public Table setLabels(java.util.Map<String, String> labels) {
        this.labels = labels;
        return this;
    }
    public java.util.Map<String, String> getLabels() {
        return this.labels;
    }

    public Table setExternalDataConfiguration(ExternalDataConfiguration externalDataConfiguration) {
        this.externalDataConfiguration = externalDataConfiguration;
        return this;
    }
    public ExternalDataConfiguration getExternalDataConfiguration() {
        return this.externalDataConfiguration;
    }

}
