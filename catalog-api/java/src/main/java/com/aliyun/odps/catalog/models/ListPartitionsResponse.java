// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListPartitionsResponse extends TeaModel {
    @NameInMap("partitions")
    @Validation(required = true)
    public java.util.List<Partition> partitions;

    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListPartitionsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListPartitionsResponse self = new ListPartitionsResponse();
        return TeaModel.build(map, self);
    }

    public ListPartitionsResponse setPartitions(java.util.List<Partition> partitions) {
        this.partitions = partitions;
        return this;
    }
    public java.util.List<Partition> getPartitions() {
        return this.partitions;
    }

    public ListPartitionsResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
