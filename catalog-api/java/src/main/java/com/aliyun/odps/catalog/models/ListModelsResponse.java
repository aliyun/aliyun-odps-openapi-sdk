// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListModelsResponse extends TeaModel {
    @NameInMap("models")
    public java.util.List<Model> models;

    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListModelsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListModelsResponse self = new ListModelsResponse();
        return TeaModel.build(map, self);
    }

    public ListModelsResponse setModels(java.util.List<Model> models) {
        this.models = models;
        return this;
    }
    public java.util.List<Model> getModels() {
        return this.models;
    }

    public ListModelsResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
