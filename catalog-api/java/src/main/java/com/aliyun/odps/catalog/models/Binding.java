// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class Binding extends TeaModel {
    @NameInMap("role")
    public String role;

    @NameInMap("members")
    public java.util.List<String> members;

    public static Binding build(java.util.Map<String, ?> map) throws Exception {
        Binding self = new Binding();
        return TeaModel.build(map, self);
    }

    public Binding setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public Binding setMembers(java.util.List<String> members) {
        this.members = members;
        return this;
    }
    public java.util.List<String> getMembers() {
        return this.members;
    }

}
