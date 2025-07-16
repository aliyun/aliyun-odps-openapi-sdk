// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class DataScanTarget extends TeaModel {
    /**
     * <p>结果写入的project name。</p>
     */
    @NameInMap("project")
    public String project;

    /**
     * <p>当dataScan.type为table时，table写入的schema</p>
     */
    @NameInMap("schema")
    public String schema;

    /**
     * <p>爬取任务自动生成的table/schema名称的前缀，防止命名冲突。</p>
     */
    @NameInMap("namePrefix")
    public String namePrefix;

    /**
     * <p>用户可指定的最终表 / schema 的属性</p>
     */
    @NameInMap("properties")
    public String properties;

    public static DataScanTarget build(java.util.Map<String, ?> map) throws Exception {
        DataScanTarget self = new DataScanTarget();
        return TeaModel.build(map, self);
    }

    public DataScanTarget setProject(String project) {
        this.project = project;
        return this;
    }
    public String getProject() {
        return this.project;
    }

    public DataScanTarget setSchema(String schema) {
        this.schema = schema;
        return this;
    }
    public String getSchema() {
        return this.schema;
    }

    public DataScanTarget setNamePrefix(String namePrefix) {
        this.namePrefix = namePrefix;
        return this;
    }
    public String getNamePrefix() {
        return this.namePrefix;
    }

    public DataScanTarget setProperties(String properties) {
        this.properties = properties;
        return this;
    }
    public String getProperties() {
        return this.properties;
    }

}
