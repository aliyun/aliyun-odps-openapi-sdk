// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class PolicyTags extends TeaModel {
    @NameInMap("names")
    public java.util.List<String> names;

    public static PolicyTags build(java.util.Map<String, ?> map) throws Exception {
        PolicyTags self = new PolicyTags();
        return TeaModel.build(map, self);
    }

    public PolicyTags setNames(java.util.List<String> names) {
        this.names = names;
        return this;
    }
    public java.util.List<String> getNames() {
        return this.names;
    }

}
