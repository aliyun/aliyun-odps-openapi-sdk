// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Project/Schema ====================================</p>
 */
public class Project extends TeaModel {
    /**
     * <p>Project的资源全名：projects/{projectId}。仅输出。</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>Project唯一ID</p>
     */
    @NameInMap("projectId")
    @Validation(required = true)
    public String projectId;

    /**
     * <p>Project的拥有者</p>
     */
    @NameInMap("owner")
    @Validation(required = true)
    public String owner;

    /**
     * <p>Project描述</p>
     */
    @NameInMap("description")
    @Validation(required = true)
    public String description;

    /**
     * <p>创建时间戳（UTC毫秒）</p>
     */
    @NameInMap("createTime")
    @Validation(required = true)
    public String createTime;

    /**
     * <p>最后修改时间戳（UTC毫秒）</p>
     */
    @NameInMap("lastModifiedTime")
    @Validation(required = true)
    public String lastModifiedTime;

    /**
     * <p>是否开启三层模型</p>
     */
    @NameInMap("schemaEnabled")
    @Validation(required = true)
    public Boolean schemaEnabled;

    /**
     * <p>所属region</p>
     */
    @NameInMap("region")
    @Validation(required = true)
    public String region;

    public static Project build(java.util.Map<String, ?> map) throws Exception {
        Project self = new Project();
        return TeaModel.build(map, self);
    }

    public Project setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public Project setProjectId(String projectId) {
        this.projectId = projectId;
        return this;
    }
    public String getProjectId() {
        return this.projectId;
    }

    public Project setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public Project setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public Project setCreateTime(String createTime) {
        this.createTime = createTime;
        return this;
    }
    public String getCreateTime() {
        return this.createTime;
    }

    public Project setLastModifiedTime(String lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
        return this;
    }
    public String getLastModifiedTime() {
        return this.lastModifiedTime;
    }

    public Project setSchemaEnabled(Boolean schemaEnabled) {
        this.schemaEnabled = schemaEnabled;
        return this;
    }
    public Boolean getSchemaEnabled() {
        return this.schemaEnabled;
    }

    public Project setRegion(String region) {
        this.region = region;
        return this;
    }
    public String getRegion() {
        return this.region;
    }

}
