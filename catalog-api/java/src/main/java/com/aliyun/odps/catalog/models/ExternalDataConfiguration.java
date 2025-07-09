// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ExternalDataConfiguration extends TeaModel {
    /**
     * <p>表数据所在的 URI</p>
     */
    @NameInMap("sourceUris")
    public java.util.List<String> sourceUris;

    /**
     * <p>支持格式：PAIMON/ICEBERG/ORC/PARQUET/CSV 等</p>
     */
    @NameInMap("sourceFormat")
    public String sourceFormat;

    /**
     * <p>关联的 Connection ID</p>
     */
    @NameInMap("connection")
    public String connection;

    public static ExternalDataConfiguration build(java.util.Map<String, ?> map) throws Exception {
        ExternalDataConfiguration self = new ExternalDataConfiguration();
        return TeaModel.build(map, self);
    }

    public ExternalDataConfiguration setSourceUris(java.util.List<String> sourceUris) {
        this.sourceUris = sourceUris;
        return this;
    }
    public java.util.List<String> getSourceUris() {
        return this.sourceUris;
    }

    public ExternalDataConfiguration setSourceFormat(String sourceFormat) {
        this.sourceFormat = sourceFormat;
        return this;
    }
    public String getSourceFormat() {
        return this.sourceFormat;
    }

    public ExternalDataConfiguration setConnection(String connection) {
        this.connection = connection;
        return this;
    }
    public String getConnection() {
        return this.connection;
    }

}
