// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class PolicyTag extends TeaModel {
    @NameInMap("names")
    public java.util.List<String> names;

    public static PolicyTag build(java.util.Map<String, ?> map) throws Exception {
        PolicyTag self = new PolicyTag();
        return TeaModel.build(map, self);
    }

    public PolicyTag setNames(java.util.List<String> names) {
        this.names = names;
        return this;
    }
    public java.util.List<String> getNames() {
        return this.names;
    }

}