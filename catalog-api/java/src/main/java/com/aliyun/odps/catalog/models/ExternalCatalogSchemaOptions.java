// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ExternalCatalogSchemaOptions extends TeaModel {
    /**
     * <p>外部schema属性配置</p>
     */
    @NameInMap("parameters")
    public java.util.Map<String, String> parameters;

    public static ExternalCatalogSchemaOptions build(java.util.Map<String, ?> map) throws Exception {
        ExternalCatalogSchemaOptions self = new ExternalCatalogSchemaOptions();
        return TeaModel.build(map, self);
    }

    public ExternalCatalogSchemaOptions setParameters(java.util.Map<String, String> parameters) {
        this.parameters = parameters;
        return this;
    }
    public java.util.Map<String, String> getParameters() {
        return this.parameters;
    }

}
