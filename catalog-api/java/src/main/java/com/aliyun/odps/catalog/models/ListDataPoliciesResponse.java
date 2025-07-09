// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListDataPoliciesResponse extends TeaModel {
    @NameInMap("dataPolicies")
    @Validation(required = true)
    public java.util.List<DataPolicy> dataPolicies;

    /**
     * <p>分页标记。</p>
     */
    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListDataPoliciesResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDataPoliciesResponse self = new ListDataPoliciesResponse();
        return TeaModel.build(map, self);
    }

    public ListDataPoliciesResponse setDataPolicies(java.util.List<DataPolicy> dataPolicies) {
        this.dataPolicies = dataPolicies;
        return this;
    }
    public java.util.List<DataPolicy> getDataPolicies() {
        return this.dataPolicies;
    }

    public ListDataPoliciesResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
