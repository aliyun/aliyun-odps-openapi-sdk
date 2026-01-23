// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class DataScan extends TeaModel {
    /**
     * <p>资源全局唯一名。e.g., namespaces/{namespaceID}/dataScans/{dataScanName}</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>用户指定的爬取任务名称</p>
     */
    @NameInMap("scanName")
    public String scanName;

    /**
     * <p>取值范围为：TABLE_DISCOVERY, SCHEMA_DISCOVERY</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>dataScan 的创建者</p>
     */
    @NameInMap("creator")
    public String creator;

    /**
     * <p>客户 ID</p>
     */
    @NameInMap("customerId")
    public String customerId;

    /**
     * <p>dataScan 所属的 namespace</p>
     */
    @NameInMap("namespaceId")
    public String namespaceId;

    /**
     * <p>用户自定义的描述</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>系统自动生成的 scan ID，只读字段。展示项</p>
     */
    @NameInMap("scanId")
    public String scanId;

    /**
     * <p>创建的时间，UTC timestamp</p>
     */
    @NameInMap("creationTime")
    public Long creationTime;

    /**
     * <p>上次修改的时间，UTC timestamp</p>
     */
    @NameInMap("lastModifiedTime")
    public Long lastModifiedTime;

    /**
     * <p>爬取任务上次触发的时间（开始调度时间），UTC timestamp。未触发过默认值为 0</p>
     */
    @NameInMap("lastTriggeredTime")
    public Long lastTriggeredTime;

    /**
     * <p>最近一次成功的 DatascanJob 的执行时间。 默认值为 0</p>
     */
    @NameInMap("lastSuccessfulScheduleTime")
    public Long lastSuccessfulScheduleTime;

    /**
     * <p>触发当前调度的来源；具体用户或调度器</p>
     */
    @NameInMap("lastTriggeredBy")
    public String lastTriggeredBy;

    /**
     * <p>dataScan 对象的调度状态。包含 IDLE/IMMEDIATE/PENDING/SCHEDULING 四种状态。dataScan 初始化状态为 IDLE，如果创建后立刻执行，设置为 IMMEDIATE</p>
     */
    @NameInMap("schedulingStatus")
    public String schedulingStatus;

    /**
     * <p>元数据爬取和发现来源，包括 location、connection 等信息</p>
     */
    @NameInMap("source")
    public DataScanSource source;

    /**
     * <p>控制 dataScan 发现结果写入的参数，包含 project、namePrefix、以及透传的 Tbl Properties 等</p>
     */
    @NameInMap("target")
    public DataScanTarget target;

    /**
     * <p>爬取任务的可选参数，包含更新策略、分类器等</p>
     */
    @NameInMap("properties")
    public DataScanProperties properties;

    /**
     * <p>manual/periodic，手动触发或者周期性自动触发</p>
     */
    @NameInMap("schedulerMode")
    public String schedulerMode;

    /**
     * <p>当 schedulerMode 为 periodic 时，两次爬取任务之间间隔的最大间隔，取值为 [1h-7d]</p>
     */
    @NameInMap("schedulerInterval")
    public String schedulerInterval;

    /**
     * <p>这个dataScan一共被调度了多少次</p>
     */
    @NameInMap("scheduledCount")
    public Long scheduledCount;

    public static DataScan build(java.util.Map<String, ?> map) throws Exception {
        DataScan self = new DataScan();
        return TeaModel.build(map, self);
    }

    public DataScan setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public DataScan setScanName(String scanName) {
        this.scanName = scanName;
        return this;
    }
    public String getScanName() {
        return this.scanName;
    }

    public DataScan setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public DataScan setCreator(String creator) {
        this.creator = creator;
        return this;
    }
    public String getCreator() {
        return this.creator;
    }

    public DataScan setCustomerId(String customerId) {
        this.customerId = customerId;
        return this;
    }
    public String getCustomerId() {
        return this.customerId;
    }

    public DataScan setNamespaceId(String namespaceId) {
        this.namespaceId = namespaceId;
        return this;
    }
    public String getNamespaceId() {
        return this.namespaceId;
    }

    public DataScan setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public DataScan setScanId(String scanId) {
        this.scanId = scanId;
        return this;
    }
    public String getScanId() {
        return this.scanId;
    }

    public DataScan setCreationTime(Long creationTime) {
        this.creationTime = creationTime;
        return this;
    }
    public Long getCreationTime() {
        return this.creationTime;
    }

    public DataScan setLastModifiedTime(Long lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
        return this;
    }
    public Long getLastModifiedTime() {
        return this.lastModifiedTime;
    }

    public DataScan setLastTriggeredTime(Long lastTriggeredTime) {
        this.lastTriggeredTime = lastTriggeredTime;
        return this;
    }
    public Long getLastTriggeredTime() {
        return this.lastTriggeredTime;
    }

    public DataScan setLastSuccessfulScheduleTime(Long lastSuccessfulScheduleTime) {
        this.lastSuccessfulScheduleTime = lastSuccessfulScheduleTime;
        return this;
    }
    public Long getLastSuccessfulScheduleTime() {
        return this.lastSuccessfulScheduleTime;
    }

    public DataScan setLastTriggeredBy(String lastTriggeredBy) {
        this.lastTriggeredBy = lastTriggeredBy;
        return this;
    }
    public String getLastTriggeredBy() {
        return this.lastTriggeredBy;
    }

    public DataScan setSchedulingStatus(String schedulingStatus) {
        this.schedulingStatus = schedulingStatus;
        return this;
    }
    public String getSchedulingStatus() {
        return this.schedulingStatus;
    }

    public DataScan setSource(DataScanSource source) {
        this.source = source;
        return this;
    }
    public DataScanSource getSource() {
        return this.source;
    }

    public DataScan setTarget(DataScanTarget target) {
        this.target = target;
        return this;
    }
    public DataScanTarget getTarget() {
        return this.target;
    }

    public DataScan setProperties(DataScanProperties properties) {
        this.properties = properties;
        return this;
    }
    public DataScanProperties getProperties() {
        return this.properties;
    }

    public DataScan setSchedulerMode(String schedulerMode) {
        this.schedulerMode = schedulerMode;
        return this;
    }
    public String getSchedulerMode() {
        return this.schedulerMode;
    }

    public DataScan setSchedulerInterval(String schedulerInterval) {
        this.schedulerInterval = schedulerInterval;
        return this;
    }
    public String getSchedulerInterval() {
        return this.schedulerInterval;
    }

    public DataScan setScheduledCount(Long scheduledCount) {
        this.scheduledCount = scheduledCount;
        return this;
    }
    public Long getScheduledCount() {
        return this.scheduledCount;
    }

}
