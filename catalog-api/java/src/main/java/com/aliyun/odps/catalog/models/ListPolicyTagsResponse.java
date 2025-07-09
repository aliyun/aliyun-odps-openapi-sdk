// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListPolicyTagsResponse extends TeaModel {
    /**
     * <p>PolicyTag列表。</p>
     */
    @NameInMap("policyTags")
    public java.util.List<PolicyTag> policyTags;

    /**
     * <p>下一页的token。</p>
     */
    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListPolicyTagsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListPolicyTagsResponse self = new ListPolicyTagsResponse();
        return TeaModel.build(map, self);
    }

    public ListPolicyTagsResponse setPolicyTags(java.util.List<PolicyTag> policyTags) {
        this.policyTags = policyTags;
        return this;
    }
    public java.util.List<PolicyTag> getPolicyTags() {
        return this.policyTags;
    }

    public ListPolicyTagsResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
