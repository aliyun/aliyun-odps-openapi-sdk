// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Partition ====================================</p>
 */
public class Partition extends TeaModel {
    /**
     * <p>分区spec，格式样例为 bu=tt/ds=20250515</p>
     */
    @NameInMap("spec")
    public String spec;

    /**
     * <p>分区的创建时间（毫秒）。仅输出。</p>
     */
    @NameInMap("createTime")
    public String createTime;

    /**
     * <p>分区的修改时间（毫秒）。仅输出。</p>
     */
    @NameInMap("lastModifiedTime")
    public String lastModifiedTime;

    /**
     * <p>分区的最后访问时间（毫秒）。仅输出。</p>
     */
    @NameInMap("lastAccessTime")
    public String lastAccessTime;

    /**
     * <p>分区的存储层级。仅输出。</p>
     */
    @NameInMap("storageTier")
    public String storageTier;

    /**
     * <p>分区的存储字节数。仅输出。</p>
     */
    @NameInMap("numStorageBytes")
    public String numStorageBytes;

    /**
     * <p>分区的计费存储明细。仅输出。</p>
     */
    @NameInMap("billableStorageDetails")
    public BillStorageDetails billableStorageDetails;

    public static Partition build(java.util.Map<String, ?> map) throws Exception {
        Partition self = new Partition();
        return TeaModel.build(map, self);
    }

    public Partition setSpec(String spec) {
        this.spec = spec;
        return this;
    }
    public String getSpec() {
        return this.spec;
    }

    public Partition setCreateTime(String createTime) {
        this.createTime = createTime;
        return this;
    }
    public String getCreateTime() {
        return this.createTime;
    }

    public Partition setLastModifiedTime(String lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
        return this;
    }
    public String getLastModifiedTime() {
        return this.lastModifiedTime;
    }

    public Partition setLastAccessTime(String lastAccessTime) {
        this.lastAccessTime = lastAccessTime;
        return this;
    }
    public String getLastAccessTime() {
        return this.lastAccessTime;
    }

    public Partition setStorageTier(String storageTier) {
        this.storageTier = storageTier;
        return this;
    }
    public String getStorageTier() {
        return this.storageTier;
    }

    public Partition setNumStorageBytes(String numStorageBytes) {
        this.numStorageBytes = numStorageBytes;
        return this;
    }
    public String getNumStorageBytes() {
        return this.numStorageBytes;
    }

    public Partition setBillableStorageDetails(BillStorageDetails billableStorageDetails) {
        this.billableStorageDetails = billableStorageDetails;
        return this;
    }
    public BillStorageDetails getBillableStorageDetails() {
        return this.billableStorageDetails;
    }

}
