// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class SearchResponse extends TeaModel {
    @NameInMap("entries")
    public java.util.List<SearchResultEntry> entries;

    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static SearchResponse build(java.util.Map<String, ?> map) throws Exception {
        SearchResponse self = new SearchResponse();
        return TeaModel.build(map, self);
    }

    public SearchResponse setEntries(java.util.List<SearchResultEntry> entries) {
        this.entries = entries;
        return this;
    }
    public java.util.List<SearchResultEntry> getEntries() {
        return this.entries;
    }

    public SearchResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
