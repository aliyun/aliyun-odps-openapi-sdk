// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.models;

import com.aliyun.tea.*;

public class RoutingResponse extends TeaModel {
    @NameInMap("body")
    public String body;

    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("statusCode")
    public Integer statusCode;

    public static RoutingResponse build(java.util.Map<String, ?> map) throws Exception {
        RoutingResponse self = new RoutingResponse();
        return TeaModel.build(map, self);
    }

    public RoutingResponse setBody(String body) {
        this.body = body;
        return this;
    }
    public String getBody() {
        return this.body;
    }

    public RoutingResponse setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public RoutingResponse setStatusCode(Integer statusCode) {
        this.statusCode = statusCode;
        return this;
    }
    public Integer getStatusCode() {
        return this.statusCode;
    }

}
