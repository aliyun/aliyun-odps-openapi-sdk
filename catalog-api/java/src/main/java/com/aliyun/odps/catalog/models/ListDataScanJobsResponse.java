// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListDataScanJobsResponse extends TeaModel {
    /**
     * <p>返回所有的 dataScan jobs 列表</p>
     */
    @NameInMap("scanJobs")
    public java.util.List<ScanJob> scanJobs;

    /**
     * <p>分页 token</p>
     */
    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListDataScanJobsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDataScanJobsResponse self = new ListDataScanJobsResponse();
        return TeaModel.build(map, self);
    }

    public ListDataScanJobsResponse setScanJobs(java.util.List<ScanJob> scanJobs) {
        this.scanJobs = scanJobs;
        return this;
    }
    public java.util.List<ScanJob> getScanJobs() {
        return this.scanJobs;
    }

    public ListDataScanJobsResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
