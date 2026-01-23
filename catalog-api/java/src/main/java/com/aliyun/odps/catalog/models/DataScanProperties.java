// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class DataScanProperties extends TeaModel {
    /**
     * <p>AUTO/PARQUET/ORC/JSON/CSV。只爬取对应属性的数据。若指定，则忽略其他类型的文件。auto为不指定属性自动探测。</p>
     */
    @NameInMap("formatFilter")
    public String formatFilter;

    /**
     * <p>enum	SAMPLE/TOTAL。 默认为SAMPLE。扫描时抽样扫描或者完整扫描</p>
     */
    @NameInMap("scanMode")
    public String scanMode;

    /**
     * <p>是否统计信息用于查询优化</p>
     */
    @NameInMap("enableStats")
    public Boolean enableStats;

    /**
     * <p>其余的配置可选项，如csv格式下的一些额外选项</p>
     */
    @NameInMap("options")
    public String options;

    /**
     * <p>分区路径识别的pattern, 例如{table}/{part1}={value1}/{part2}={value2}</p>
     */
    @NameInMap("options")
    public String pattern;

    /**
     * <p>发现表元数据发生变化时的处理策略。APPEND_ONLY/OVERWRITE/IGNORE</p>
     */
    @NameInMap("updatePolicy")
    public String updatePolicy;

    /**
     * <p>发现表删除时是否自动删除</p>
     */
    @NameInMap("syncRemove")
    public Boolean syncRemove;

    /**
     * <p>false代表爬取任务只输出结果，不提交ddl</p>
     */
    @NameInMap("autoCommit")
    public Boolean autoCommit;

    /**
     * <p>指定 OSS Inventory 日志的存储位置，用于增量扫描功能</p>
     */
    @NameInMap("inventoryLocation")
    public String inventoryLocation;

    public static DataScanProperties build(java.util.Map<String, ?> map) throws Exception {
        DataScanProperties self = new DataScanProperties();
        return TeaModel.build(map, self);
    }

    public DataScanProperties setFormatFilter(String formatFilter) {
        this.formatFilter = formatFilter;
        return this;
    }
    public String getFormatFilter() {
        return this.formatFilter;
    }

    public DataScanProperties setScanMode(String scanMode) {
        this.scanMode = scanMode;
        return this;
    }
    public String getScanMode() {
        return this.scanMode;
    }

    public DataScanProperties setEnableStats(Boolean enableStats) {
        this.enableStats = enableStats;
        return this;
    }
    public Boolean getEnableStats() {
        return this.enableStats;
    }

    public DataScanProperties setOptions(String options) {
        this.options = options;
        return this;
    }
    public String getOptions() {
        return this.options;
    }

    public DataScanProperties setPattern(String pattern) {
        this.pattern = pattern;
        return this;
    }
    public String getPattern() {
        return this.pattern;
    }

    public DataScanProperties setUpdatePolicy(String updatePolicy) {
        this.updatePolicy = updatePolicy;
        return this;
    }
    public String getUpdatePolicy() {
        return this.updatePolicy;
    }

    public DataScanProperties setSyncRemove(Boolean syncRemove) {
        this.syncRemove = syncRemove;
        return this;
    }
    public Boolean getSyncRemove() {
        return this.syncRemove;
    }

    public DataScanProperties setAutoCommit(Boolean autoCommit) {
        this.autoCommit = autoCommit;
        return this;
    }
    public Boolean getAutoCommit() {
        return this.autoCommit;
    }

    public DataScanProperties setInventoryLocation(String inventoryLocation) {
        this.inventoryLocation = inventoryLocation;
        return this;
    }
    public String getInventoryLocation() {
        return this.inventoryLocation;
    }

}
