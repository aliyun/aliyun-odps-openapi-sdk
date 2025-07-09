// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListConnectionsResponse extends TeaModel {
    @NameInMap("connections")
    @Validation(required = true)
    public java.util.List<Connection> connections;

    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListConnectionsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListConnectionsResponse self = new ListConnectionsResponse();
        return TeaModel.build(map, self);
    }

    public ListConnectionsResponse setConnections(java.util.List<Connection> connections) {
        this.connections = connections;
        return this;
    }
    public java.util.List<Connection> getConnections() {
        return this.connections;
    }

    public ListConnectionsResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
