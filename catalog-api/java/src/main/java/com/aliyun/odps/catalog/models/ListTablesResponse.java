// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListTablesResponse extends TeaModel {
    @NameInMap("tables")
    public java.util.List<Table> tables;

    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListTablesResponse build(java.util.Map<String, ?> map) throws Exception {
        ListTablesResponse self = new ListTablesResponse();
        return TeaModel.build(map, self);
    }

    public ListTablesResponse setTables(java.util.List<Table> tables) {
        this.tables = tables;
        return this;
    }
    public java.util.List<Table> getTables() {
        return this.tables;
    }

    public ListTablesResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
