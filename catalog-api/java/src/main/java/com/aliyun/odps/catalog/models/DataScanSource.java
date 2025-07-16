// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== DataScans ====================================</p>
 */
public class DataScanSource extends TeaModel {
    /**
     * <p>location地址。支持oss、dlf 和 holo</p>
     */
    @NameInMap("location")
    public String location;

    /**
     * <p>connection name。提供访问source需要的身份与网络信息。需要鉴权</p>
     */
    @NameInMap("connection")
    public String connection;

    /**
     * <p>忽略访问的路径。支持正则表达式</p>
     */
    @NameInMap("ignores")
    public java.util.List<String> ignores;

    public static DataScanSource build(java.util.Map<String, ?> map) throws Exception {
        DataScanSource self = new DataScanSource();
        return TeaModel.build(map, self);
    }

    public DataScanSource setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public DataScanSource setConnection(String connection) {
        this.connection = connection;
        return this;
    }
    public String getConnection() {
        return this.connection;
    }

    public DataScanSource setIgnores(java.util.List<String> ignores) {
        this.ignores = ignores;
        return this;
    }
    public java.util.List<String> getIgnores() {
        return this.ignores;
    }

}
