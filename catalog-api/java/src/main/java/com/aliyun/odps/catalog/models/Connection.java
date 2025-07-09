// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Connection ====================================</p>
 */
public class Connection extends TeaModel {
    /**
     * <p>资源全局唯一名：namespaces/{namespace_ID}/connections/{connectionName}</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 32]。</p>
     */
    @NameInMap("connectionName")
    @Validation(required = true)
    public String connectionName;

    /**
     * <p>可选。最多 1KB。</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>Connection 的创建时间（毫秒）</p>
     */
    @NameInMap("creationTime")
    public String creationTime;

    /**
     * <p>最后修改时间（毫秒）</p>
     */
    @NameInMap("lastModifiedTime")
    public String lastModifiedTime;

    /**
     * <p>Connection 的类型。必需项。</p>
     */
    @NameInMap("connectionType")
    @Validation(required = true)
    public String connectionType;

    /**
     * <p>云上资源类型的 connection 对应的选项配置。仅当 connectionType 为 CLOUD_RESOURCE 时才设置。</p>
     */
    @NameInMap("cloudResource")
    public CloudResourceOptions cloudResource;

    /**
     * <p>此 connection 所属的 region。</p>
     */
    @NameInMap("region")
    public String region;

    public static Connection build(java.util.Map<String, ?> map) throws Exception {
        Connection self = new Connection();
        return TeaModel.build(map, self);
    }

    public Connection setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public Connection setConnectionName(String connectionName) {
        this.connectionName = connectionName;
        return this;
    }
    public String getConnectionName() {
        return this.connectionName;
    }

    public Connection setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public Connection setCreationTime(String creationTime) {
        this.creationTime = creationTime;
        return this;
    }
    public String getCreationTime() {
        return this.creationTime;
    }

    public Connection setLastModifiedTime(String lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
        return this;
    }
    public String getLastModifiedTime() {
        return this.lastModifiedTime;
    }

    public Connection setConnectionType(String connectionType) {
        this.connectionType = connectionType;
        return this;
    }
    public String getConnectionType() {
        return this.connectionType;
    }

    public Connection setCloudResource(CloudResourceOptions cloudResource) {
        this.cloudResource = cloudResource;
        return this;
    }
    public CloudResourceOptions getCloudResource() {
        return this.cloudResource;
    }

    public Connection setRegion(String region) {
        this.region = region;
        return this;
    }
    public String getRegion() {
        return this.region;
    }

}
