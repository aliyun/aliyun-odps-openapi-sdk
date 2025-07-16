// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ScanJob extends TeaModel {
    /**
     * <p>Job ID</p>
     */
    @NameInMap("jobId")
    public String jobId;

    /**
     * <p>作业所属的 namespace</p>
     */
    @NameInMap("namespaceId")
    public String namespaceId;

    /**
     * <p>系统自动生成的 dataScan ID</p>
     */
    @NameInMap("dataScanId")
    public String dataScanId;

    /**
     * <p>所属爬取任务名称。此处为全称 namespace/$nsId/dataScan/$scanName</p>
     */
    @NameInMap("dataScanName")
    public String dataScanName;

    /**
     * <p>触发此次爬取作业的人，定时触发则为 scheduler</p>
     */
    @NameInMap("triggeredBy")
    public String triggeredBy;

    /**
     * <p>爬取作业开始时间，UTC timestamp</p>
     */
    @NameInMap("startTime")
    public Long startTime;

    /**
     * <p>爬取作业结束时间，UTC timestamp</p>
     */
    @NameInMap("endTime")
    public Long endTime;

    /**
     * <p>爬取作业状态，取值范围：Created/Running/Terminated/Failed</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>爬取作业状态详细信息，如报错信息</p>
     */
    @NameInMap("statusDetail")
    public String statusDetail;

    /**
     * <p>爬取作业返回的需要提交的 DDL 信息</p>
     */
    @NameInMap("ddl")
    public String ddl;

    /**
     * <p>爬取作业返回的 stats 信息，JSON 格式</p>
     */
    @NameInMap("stats")
    public String stats;

    public static ScanJob build(java.util.Map<String, ?> map) throws Exception {
        ScanJob self = new ScanJob();
        return TeaModel.build(map, self);
    }

    public ScanJob setJobId(String jobId) {
        this.jobId = jobId;
        return this;
    }
    public String getJobId() {
        return this.jobId;
    }

    public ScanJob setNamespaceId(String namespaceId) {
        this.namespaceId = namespaceId;
        return this;
    }
    public String getNamespaceId() {
        return this.namespaceId;
    }

    public ScanJob setDataScanId(String dataScanId) {
        this.dataScanId = dataScanId;
        return this;
    }
    public String getDataScanId() {
        return this.dataScanId;
    }

    public ScanJob setDataScanName(String dataScanName) {
        this.dataScanName = dataScanName;
        return this;
    }
    public String getDataScanName() {
        return this.dataScanName;
    }

    public ScanJob setTriggeredBy(String triggeredBy) {
        this.triggeredBy = triggeredBy;
        return this;
    }
    public String getTriggeredBy() {
        return this.triggeredBy;
    }

    public ScanJob setStartTime(Long startTime) {
        this.startTime = startTime;
        return this;
    }
    public Long getStartTime() {
        return this.startTime;
    }

    public ScanJob setEndTime(Long endTime) {
        this.endTime = endTime;
        return this;
    }
    public Long getEndTime() {
        return this.endTime;
    }

    public ScanJob setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public ScanJob setStatusDetail(String statusDetail) {
        this.statusDetail = statusDetail;
        return this;
    }
    public String getStatusDetail() {
        return this.statusDetail;
    }

    public ScanJob setDdl(String ddl) {
        this.ddl = ddl;
        return this;
    }
    public String getDdl() {
        return this.ddl;
    }

    public ScanJob setStats(String stats) {
        this.stats = stats;
        return this;
    }
    public String getStats() {
        return this.stats;
    }

}
