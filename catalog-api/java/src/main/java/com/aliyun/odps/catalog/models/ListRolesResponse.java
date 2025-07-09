// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListRolesResponse extends TeaModel {
    /**
     * <p>角色列表。</p>
     */
    @NameInMap("roles")
    public java.util.List<Role> roles;

    /**
     * <p>下一页的token。</p>
     */
    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListRolesResponse build(java.util.Map<String, ?> map) throws Exception {
        ListRolesResponse self = new ListRolesResponse();
        return TeaModel.build(map, self);
    }

    public ListRolesResponse setRoles(java.util.List<Role> roles) {
        this.roles = roles;
        return this;
    }
    public java.util.List<Role> getRoles() {
        return this.roles;
    }

    public ListRolesResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
