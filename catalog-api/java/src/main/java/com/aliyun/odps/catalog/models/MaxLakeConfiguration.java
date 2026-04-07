// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class MaxLakeConfiguration extends TeaModel {
    /**
     * <p>表所在的 URI</p>
     */
    @NameInMap("storageUri")
    public String storageUri;

    /**
     * <p>支持格式：ICEBERG</p>
     */
    @NameInMap("tableFormat")
    public String tableFormat;

    /**
     * <p>关联的 Connection ID</p>
     */
    @NameInMap("connection")
    public String connection;

    public static MaxLakeConfiguration build(java.util.Map<String, ?> map) throws Exception {
        MaxLakeConfiguration self = new MaxLakeConfiguration();
        return TeaModel.build(map, self);
    }

    public MaxLakeConfiguration setStorageUri(String storageUri) {
        this.storageUri = storageUri;
        return this;
    }
    public String getStorageUri() {
        return this.storageUri;
    }

    public MaxLakeConfiguration setTableFormat(String tableFormat) {
        this.tableFormat = tableFormat;
        return this;
    }
    public String getTableFormat() {
        return this.tableFormat;
    }

    public MaxLakeConfiguration setConnection(String connection) {
        this.connection = connection;
        return this;
    }
    public String getConnection() {
        return this.connection;
    }

}
