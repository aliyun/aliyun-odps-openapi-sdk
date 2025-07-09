// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListSchemasResponse extends TeaModel {
    @NameInMap("schemas")
    @Validation(required = true)
    public java.util.List<Schema> schemas;

    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListSchemasResponse build(java.util.Map<String, ?> map) throws Exception {
        ListSchemasResponse self = new ListSchemasResponse();
        return TeaModel.build(map, self);
    }

    public ListSchemasResponse setSchemas(java.util.List<Schema> schemas) {
        this.schemas = schemas;
        return this;
    }
    public java.util.List<Schema> getSchemas() {
        return this.schemas;
    }

    public ListSchemasResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
