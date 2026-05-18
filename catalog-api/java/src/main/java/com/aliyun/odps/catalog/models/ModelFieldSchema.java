// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ModelFieldSchema extends TeaModel {
    /**
     * <p>列名或 struct 字段名</p>
     */
    @NameInMap("fieldName")
    public String fieldName;

    /**
     * <p>SQL DDL 中的列类型定义</p>
     */
    @NameInMap("sqlTypeDefinition")
    public String sqlTypeDefinition;

    /**
     * <p>字段类型</p>
     */
    @NameInMap("typeCategory")
    public String typeCategory;

    /**
     * <p>字段模式：REQUIRED 或 NULLABLE</p>
     */
    @NameInMap("mode")
    public String mode;

    /**
     * <p>STRUCT 类型的子字段</p>
     */
    @NameInMap("fields")
    public java.util.List<ModelFieldSchema> fields;

    /**
     * <p>列的 comment</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>CHAR/VARCHAR 类型的最大长度</p>
     */
    @NameInMap("maxLength")
    public String maxLength;

    /**
     * <p>DECIMAL 类型的精度</p>
     */
    @NameInMap("precision")
    public String precision;

    /**
     * <p>DECIMAL 类型的 scale</p>
     */
    @NameInMap("scale")
    public String scale;

    /**
     * <p>默认值的表达式字符串</p>
     */
    @NameInMap("defaultValueExpression")
    public String defaultValueExpression;

    /**
     * <p>如果是 VECTOR 类型，表示向量的维度</p>
     */
    @NameInMap("dimension")
    public String dimension;

    public static ModelFieldSchema build(java.util.Map<String, ?> map) throws Exception {
        ModelFieldSchema self = new ModelFieldSchema();
        return TeaModel.build(map, self);
    }

    public ModelFieldSchema setFieldName(String fieldName) {
        this.fieldName = fieldName;
        return this;
    }
    public String getFieldName() {
        return this.fieldName;
    }

    public ModelFieldSchema setSqlTypeDefinition(String sqlTypeDefinition) {
        this.sqlTypeDefinition = sqlTypeDefinition;
        return this;
    }
    public String getSqlTypeDefinition() {
        return this.sqlTypeDefinition;
    }

    public ModelFieldSchema setTypeCategory(String typeCategory) {
        this.typeCategory = typeCategory;
        return this;
    }
    public String getTypeCategory() {
        return this.typeCategory;
    }

    public ModelFieldSchema setMode(String mode) {
        this.mode = mode;
        return this;
    }
    public String getMode() {
        return this.mode;
    }

    public ModelFieldSchema setFields(java.util.List<ModelFieldSchema> fields) {
        this.fields = fields;
        return this;
    }
    public java.util.List<ModelFieldSchema> getFields() {
        return this.fields;
    }

    public ModelFieldSchema setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public ModelFieldSchema setMaxLength(String maxLength) {
        this.maxLength = maxLength;
        return this;
    }
    public String getMaxLength() {
        return this.maxLength;
    }

    public ModelFieldSchema setPrecision(String precision) {
        this.precision = precision;
        return this;
    }
    public String getPrecision() {
        return this.precision;
    }

    public ModelFieldSchema setScale(String scale) {
        this.scale = scale;
        return this;
    }
    public String getScale() {
        return this.scale;
    }

    public ModelFieldSchema setDefaultValueExpression(String defaultValueExpression) {
        this.defaultValueExpression = defaultValueExpression;
        return this;
    }
    public String getDefaultValueExpression() {
        return this.defaultValueExpression;
    }

    public ModelFieldSchema setDimension(String dimension) {
        this.dimension = dimension;
        return this;
    }
    public String getDimension() {
        return this.dimension;
    }

}
