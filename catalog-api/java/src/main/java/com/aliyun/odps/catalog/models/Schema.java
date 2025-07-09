// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class Schema extends TeaModel {
    /**
     * <p>Schema的资源全名：projects/{projectId}/schemas/{schemaName}。仅输出。</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>Project下唯一名称</p>
     */
    @NameInMap("schemaName")
    @Validation(required = true, maxLength = 128)
    public String schemaName;

    /**
     * <p>可选描述，不超过xxKB</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>Schema类型：DEFAULT/EXTERNAL</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>Schema拥有者</p>
     */
    @NameInMap("owner")
    @Validation(required = true)
    public String owner;

    /**
     * <p>外部schema配置</p>
     */
    @NameInMap("externalSchemaConfiguration")
    public ExternalSchemaConfiguration externalSchemaConfiguration;

    public static Schema build(java.util.Map<String, ?> map) throws Exception {
        Schema self = new Schema();
        return TeaModel.build(map, self);
    }

    public Schema setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public Schema setSchemaName(String schemaName) {
        this.schemaName = schemaName;
        return this;
    }
    public String getSchemaName() {
        return this.schemaName;
    }

    public Schema setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public Schema setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public Schema setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public Schema setExternalSchemaConfiguration(ExternalSchemaConfiguration externalSchemaConfiguration) {
        this.externalSchemaConfiguration = externalSchemaConfiguration;
        return this;
    }
    public ExternalSchemaConfiguration getExternalSchemaConfiguration() {
        return this.externalSchemaConfiguration;
    }

}
