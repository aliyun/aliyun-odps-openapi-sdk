// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Table ====================================</p>
 */
public class TableFieldSchema extends TeaModel {
    /**
     * <p>列名（如果是顶层列），或者 struct 字段名。</p>
     */
    @NameInMap("fieldName")
    public String fieldName;

    /**
     * <p>在 SQL DDL 语句中填写的表示列类型的字符串定义。</p>
     */
    @NameInMap("sqlTypeDefinition")
    public String sqlTypeDefinition;

    /**
     * <p>字段类型。</p>
     */
    @NameInMap("typeCategory")
    public String typeCategory;

    /**
     * <p>REQUIRED 或 NULLABLE。</p>
     */
    @NameInMap("mode")
    public String mode;

    /**
     * <p>如果是 STRUCT 类型，表示 STRUCT 的子字段。</p>
     */
    @NameInMap("fields")
    public java.util.List<TableFieldSchema> fields;

    /**
     * <p>列的评论。</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>可选。列绑定的 policy tag。</p>
     */
    @NameInMap("policyTags")
    public PolicyTags policyTags;

    /**
     * <p>如果是 CHAR/VARCHAR 类型，表示字段的最大长度。</p>
     */
    @NameInMap("maxLength")
    public String maxLength;

    /**
     * <p>如果 DECIMAL 类型，表示精度。</p>
     */
    @NameInMap("precision")
    public String precision;

    /**
     * <p>如果 DECIMAL 类型，表示 scale。</p>
     */
    @NameInMap("scale")
    public String scale;

    /**
     * <p>可选。默认值的表达式字符串。</p>
     */
    @NameInMap("defaultValueExpression")
    public String defaultValueExpression;

    public static TableFieldSchema build(java.util.Map<String, ?> map) throws Exception {
        TableFieldSchema self = new TableFieldSchema();
        return TeaModel.build(map, self);
    }

    public TableFieldSchema setFieldName(String fieldName) {
        this.fieldName = fieldName;
        return this;
    }
    public String getFieldName() {
        return this.fieldName;
    }

    public TableFieldSchema setSqlTypeDefinition(String sqlTypeDefinition) {
        this.sqlTypeDefinition = sqlTypeDefinition;
        return this;
    }
    public String getSqlTypeDefinition() {
        return this.sqlTypeDefinition;
    }

    public TableFieldSchema setTypeCategory(String typeCategory) {
        this.typeCategory = typeCategory;
        return this;
    }
    public String getTypeCategory() {
        return this.typeCategory;
    }

    public TableFieldSchema setMode(String mode) {
        this.mode = mode;
        return this;
    }
    public String getMode() {
        return this.mode;
    }

    public TableFieldSchema setFields(java.util.List<TableFieldSchema> fields) {
        this.fields = fields;
        return this;
    }
    public java.util.List<TableFieldSchema> getFields() {
        return this.fields;
    }

    public TableFieldSchema setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public TableFieldSchema setPolicyTags(PolicyTags policyTags) {
        this.policyTags = policyTags;
        return this;
    }
    public PolicyTags getPolicyTags() {
        return this.policyTags;
    }

    public TableFieldSchema setMaxLength(String maxLength) {
        this.maxLength = maxLength;
        return this;
    }
    public String getMaxLength() {
        return this.maxLength;
    }

    public TableFieldSchema setPrecision(String precision) {
        this.precision = precision;
        return this;
    }
    public String getPrecision() {
        return this.precision;
    }

    public TableFieldSchema setScale(String scale) {
        this.scale = scale;
        return this;
    }
    public String getScale() {
        return this.scale;
    }

    public TableFieldSchema setDefaultValueExpression(String defaultValueExpression) {
        this.defaultValueExpression = defaultValueExpression;
        return this;
    }
    public String getDefaultValueExpression() {
        return this.defaultValueExpression;
    }

}
