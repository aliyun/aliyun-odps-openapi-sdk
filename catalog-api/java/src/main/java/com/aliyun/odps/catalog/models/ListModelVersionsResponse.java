// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListModelVersionsResponse extends TeaModel {
    @NameInMap("models")
    public java.util.List<Model> models;

    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListModelVersionsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListModelVersionsResponse self = new ListModelVersionsResponse();
        return TeaModel.build(map, self);
    }

    public ListModelVersionsResponse setModels(java.util.List<Model> models) {
        this.models = models;
        return this;
    }
    public java.util.List<Model> getModels() {
        return this.models;
    }

    public ListModelVersionsResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
