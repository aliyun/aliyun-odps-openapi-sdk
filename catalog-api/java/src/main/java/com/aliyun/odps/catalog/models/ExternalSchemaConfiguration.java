// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ExternalSchemaConfiguration extends TeaModel {
    /**
     * <p>关联的connection ID</p>
     */
    @NameInMap("connection")
    public String connection;

    /**
     * <p>外部catalog schema配置</p>
     */
    @NameInMap("externalCatalogSchemaOptions")
    public ExternalCatalogSchemaOptions externalCatalogSchemaOptions;

    public static ExternalSchemaConfiguration build(java.util.Map<String, ?> map) throws Exception {
        ExternalSchemaConfiguration self = new ExternalSchemaConfiguration();
        return TeaModel.build(map, self);
    }

    public ExternalSchemaConfiguration setConnection(String connection) {
        this.connection = connection;
        return this;
    }
    public String getConnection() {
        return this.connection;
    }

    public ExternalSchemaConfiguration setExternalCatalogSchemaOptions(ExternalCatalogSchemaOptions externalCatalogSchemaOptions) {
        this.externalCatalogSchemaOptions = externalCatalogSchemaOptions;
        return this;
    }
    public ExternalCatalogSchemaOptions getExternalCatalogSchemaOptions() {
        return this.externalCatalogSchemaOptions;
    }

}
