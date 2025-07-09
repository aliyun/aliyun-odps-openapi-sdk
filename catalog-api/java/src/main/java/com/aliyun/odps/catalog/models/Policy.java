// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class Policy extends TeaModel {
    @NameInMap("etag")
    public String etag;

    @NameInMap("bindings")
    public java.util.List<Binding> bindings;

    public static Policy build(java.util.Map<String, ?> map) throws Exception {
        Policy self = new Policy();
        return TeaModel.build(map, self);
    }

    public Policy setEtag(String etag) {
        this.etag = etag;
        return this;
    }
    public String getEtag() {
        return this.etag;
    }

    public Policy setBindings(java.util.List<Binding> bindings) {
        this.bindings = bindings;
        return this;
    }
    public java.util.List<Binding> getBindings() {
        return this.bindings;
    }

}
