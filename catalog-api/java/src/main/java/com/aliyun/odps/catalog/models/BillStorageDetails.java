// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class BillStorageDetails extends TeaModel {
    /**
     * <p>参与计费的总存储字节数。</p>
     */
    @NameInMap("numBillableStorageBytes")
    public String numBillableStorageBytes;

    /**
     * <p>参与计费的标准存储字节数。</p>
     */
    @NameInMap("numBillableStandardStorageBytes")
    public String numBillableStandardStorageBytes;

    /**
     * <p>参与计费的低频存储字节数。</p>
     */
    @NameInMap("numBillableLowfrequencyStorageBytes")
    public String numBillableLowfrequencyStorageBytes;

    /**
     * <p>参与计费的长期存储字节数。</p>
     */
    @NameInMap("numBillableLongtermStorageBytes")
    public String numBillableLongtermStorageBytes;

    /**
     * <p>参与计费的冷归档存储字节数。</p>
     */
    @NameInMap("numBillableColdStorageBytes")
    public String numBillableColdStorageBytes;

    /**
     * <p>参与计费的回收站存储字节数。</p>
     */
    @NameInMap("numBillableRecycleBinStorageBytes")
    public String numBillableRecycleBinStorageBytes;

    public static BillStorageDetails build(java.util.Map<String, ?> map) throws Exception {
        BillStorageDetails self = new BillStorageDetails();
        return TeaModel.build(map, self);
    }

    public BillStorageDetails setNumBillableStorageBytes(String numBillableStorageBytes) {
        this.numBillableStorageBytes = numBillableStorageBytes;
        return this;
    }
    public String getNumBillableStorageBytes() {
        return this.numBillableStorageBytes;
    }

    public BillStorageDetails setNumBillableStandardStorageBytes(String numBillableStandardStorageBytes) {
        this.numBillableStandardStorageBytes = numBillableStandardStorageBytes;
        return this;
    }
    public String getNumBillableStandardStorageBytes() {
        return this.numBillableStandardStorageBytes;
    }

    public BillStorageDetails setNumBillableLowfrequencyStorageBytes(String numBillableLowfrequencyStorageBytes) {
        this.numBillableLowfrequencyStorageBytes = numBillableLowfrequencyStorageBytes;
        return this;
    }
    public String getNumBillableLowfrequencyStorageBytes() {
        return this.numBillableLowfrequencyStorageBytes;
    }

    public BillStorageDetails setNumBillableLongtermStorageBytes(String numBillableLongtermStorageBytes) {
        this.numBillableLongtermStorageBytes = numBillableLongtermStorageBytes;
        return this;
    }
    public String getNumBillableLongtermStorageBytes() {
        return this.numBillableLongtermStorageBytes;
    }

    public BillStorageDetails setNumBillableColdStorageBytes(String numBillableColdStorageBytes) {
        this.numBillableColdStorageBytes = numBillableColdStorageBytes;
        return this;
    }
    public String getNumBillableColdStorageBytes() {
        return this.numBillableColdStorageBytes;
    }

    public BillStorageDetails setNumBillableRecycleBinStorageBytes(String numBillableRecycleBinStorageBytes) {
        this.numBillableRecycleBinStorageBytes = numBillableRecycleBinStorageBytes;
        return this;
    }
    public String getNumBillableRecycleBinStorageBytes() {
        return this.numBillableRecycleBinStorageBytes;
    }

}
