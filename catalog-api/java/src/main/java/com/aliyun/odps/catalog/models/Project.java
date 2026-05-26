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
    public String projectId;

    /**
     * <p>Project的拥有者</p>
     */
    @NameInMap("owner")
    public String owner;

    /**
     * <p>Project描述</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>创建时间戳（UTC毫秒）</p>
     */
    @NameInMap("createTime")
    public String createTime;

    /**
     * <p>最后修改时间戳（UTC毫秒）</p>
     */
    @NameInMap("lastModifiedTime")
    public String lastModifiedTime;

    /**
     * <p>是否开启三层模型</p>
     */
    @NameInMap("schemaEnabled")
    public Boolean schemaEnabled;

    /**
     * <p>所属region</p>
     */
    @NameInMap("region")
    public String region;

    /**
     * <p>是否为外部 catalog project</p>
     */
    @NameInMap("externalCatalog")
    public Boolean externalCatalog;

    /**
     * <p>是否开启同城容灾。</p>
     */
    @NameInMap("zoneDisasterRecoveryEnabled")
    public Boolean zoneDisasterRecoveryEnabled;

    /**
     * <p>Project 下普通表（含外表）的个数。仅输出。</p>
     */
    @NameInMap("numTables")
    public Integer numTables;

    /**
     * <p>Project 下物化视图的个数。仅输出。</p>
     */
    @NameInMap("numMaterializedViews")
    public Integer numMaterializedViews;

    /**
     * <p>Project 下 snapshot 表的个数。仅输出。</p>
     */
    @NameInMap("numSnapshots")
    public Integer numSnapshots;

    /**
     * <p>Project 下资源的个数。仅输出。</p>
     */
    @NameInMap("numResources")
    public Integer numResources;

    /**
     * <p>Project 的总存储字节数。仅输出。</p>
     */
    @NameInMap("numStorageBytes")
    public String numStorageBytes;

    /**
     * <p>Project 下普通表的存储字节数。仅输出。</p>
     */
    @NameInMap("numTablesBytes")
    public String numTablesBytes;

    /**
     * <p>Project 下 snapshot 表的存储字节数。仅输出。</p>
     */
    @NameInMap("numSnapshotsBytes")
    public String numSnapshotsBytes;

    /**
     * <p>Project 下物化视图的存储字节数。仅输出。</p>
     */
    @NameInMap("numMaterializedViewsBytes")
    public String numMaterializedViewsBytes;

    /**
     * <p>Project 下资源的存储字节数。仅输出。</p>
     */
    @NameInMap("numResourcesBytes")
    public String numResourcesBytes;

    /**
     * <p>Project 的回收站存储字节数。仅输出。</p>
     */
    @NameInMap("numRecycleBinBytes")
    public String numRecycleBinBytes;

    /**
     * <p>Project 的计费存储明细。仅输出。</p>
     */
    @NameInMap("billableStorageDetails")
    public BillStorageDetails billableStorageDetails;

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

    public Project setExternalCatalog(Boolean externalCatalog) {
        this.externalCatalog = externalCatalog;
        return this;
    }
    public Boolean getExternalCatalog() {
        return this.externalCatalog;
    }

    public Project setZoneDisasterRecoveryEnabled(Boolean zoneDisasterRecoveryEnabled) {
        this.zoneDisasterRecoveryEnabled = zoneDisasterRecoveryEnabled;
        return this;
    }
    public Boolean getZoneDisasterRecoveryEnabled() {
        return this.zoneDisasterRecoveryEnabled;
    }

    public Project setNumTables(Integer numTables) {
        this.numTables = numTables;
        return this;
    }
    public Integer getNumTables() {
        return this.numTables;
    }

    public Project setNumMaterializedViews(Integer numMaterializedViews) {
        this.numMaterializedViews = numMaterializedViews;
        return this;
    }
    public Integer getNumMaterializedViews() {
        return this.numMaterializedViews;
    }

    public Project setNumSnapshots(Integer numSnapshots) {
        this.numSnapshots = numSnapshots;
        return this;
    }
    public Integer getNumSnapshots() {
        return this.numSnapshots;
    }

    public Project setNumResources(Integer numResources) {
        this.numResources = numResources;
        return this;
    }
    public Integer getNumResources() {
        return this.numResources;
    }

    public Project setNumStorageBytes(String numStorageBytes) {
        this.numStorageBytes = numStorageBytes;
        return this;
    }
    public String getNumStorageBytes() {
        return this.numStorageBytes;
    }

    public Project setNumTablesBytes(String numTablesBytes) {
        this.numTablesBytes = numTablesBytes;
        return this;
    }
    public String getNumTablesBytes() {
        return this.numTablesBytes;
    }

    public Project setNumSnapshotsBytes(String numSnapshotsBytes) {
        this.numSnapshotsBytes = numSnapshotsBytes;
        return this;
    }
    public String getNumSnapshotsBytes() {
        return this.numSnapshotsBytes;
    }

    public Project setNumMaterializedViewsBytes(String numMaterializedViewsBytes) {
        this.numMaterializedViewsBytes = numMaterializedViewsBytes;
        return this;
    }
    public String getNumMaterializedViewsBytes() {
        return this.numMaterializedViewsBytes;
    }

    public Project setNumResourcesBytes(String numResourcesBytes) {
        this.numResourcesBytes = numResourcesBytes;
        return this;
    }
    public String getNumResourcesBytes() {
        return this.numResourcesBytes;
    }

    public Project setNumRecycleBinBytes(String numRecycleBinBytes) {
        this.numRecycleBinBytes = numRecycleBinBytes;
        return this;
    }
    public String getNumRecycleBinBytes() {
        return this.numRecycleBinBytes;
    }

    public Project setBillableStorageDetails(BillStorageDetails billableStorageDetails) {
        this.billableStorageDetails = billableStorageDetails;
        return this;
    }
    public BillStorageDetails getBillableStorageDetails() {
        return this.billableStorageDetails;
    }

}
