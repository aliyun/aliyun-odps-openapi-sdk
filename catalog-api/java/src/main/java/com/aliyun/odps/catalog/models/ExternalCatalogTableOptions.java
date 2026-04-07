// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ExternalCatalogTableOptions extends TeaModel {
    /**
     * <p>external catalog 属性</p>
     */
    @NameInMap("parameters")
    public java.util.Map<String, String> parameters;

    public static ExternalCatalogTableOptions build(java.util.Map<String, ?> map) throws Exception {
        ExternalCatalogTableOptions self = new ExternalCatalogTableOptions();
        return TeaModel.build(map, self);
    }

    public ExternalCatalogTableOptions setParameters(java.util.Map<String, String> parameters) {
        this.parameters = parameters;
        return this;
    }
    public java.util.Map<String, String> getParameters() {
        return this.parameters;
    }

}
