// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListTaxonomiesResponse extends TeaModel {
    /**
     * <p>Taxonomy列表。</p>
     */
    @NameInMap("taxonomies")
    public java.util.List<Taxonomy> taxonomies;

    /**
     * <p>下一页的token。</p>
     */
    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListTaxonomiesResponse build(java.util.Map<String, ?> map) throws Exception {
        ListTaxonomiesResponse self = new ListTaxonomiesResponse();
        return TeaModel.build(map, self);
    }

    public ListTaxonomiesResponse setTaxonomies(java.util.List<Taxonomy> taxonomies) {
        this.taxonomies = taxonomies;
        return this;
    }
    public java.util.List<Taxonomy> getTaxonomies() {
        return this.taxonomies;
    }

    public ListTaxonomiesResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
