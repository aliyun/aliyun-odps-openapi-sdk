// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListDataScansResponse extends TeaModel {
    /**
     * <p>分页 token</p>
     */
    @NameInMap("nextToken")
    public String nextPageToken;

    /**
     * <p>返回所有的 dataScans 列表。</p>
     */
    @NameInMap("dataScans")
    public java.util.List<DataScan> dataScans;

    public static ListDataScansResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDataScansResponse self = new ListDataScansResponse();
        return TeaModel.build(map, self);
    }

    public ListDataScansResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

    public ListDataScansResponse setDataScans(java.util.List<DataScan> dataScans) {
        this.dataScans = dataScans;
        return this;
    }
    public java.util.List<DataScan> getDataScans() {
        return this.dataScans;
    }

}
