// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListDataScanJobsResponse extends TeaModel {
    /**
     * <p>返回所有的 dataScan jobs 列表</p>
     */
    @NameInMap("data")
    public java.util.List<ScanJob> data;

    /**
     * <p>分页 token</p>
     */
    @NameInMap("nextToken")
    public String nextToken;

    /**
     * <p>数据总量</p>
     */
    @NameInMap("totalCount")
    public Integer totalCount;

    /**
     * <p>每页最大结果数</p>
     */
    @NameInMap("maxResults")
    public Integer maxResults;

    public static ListDataScanJobsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDataScanJobsResponse self = new ListDataScanJobsResponse();
        return TeaModel.build(map, self);
    }

    public ListDataScanJobsResponse setData(java.util.List<ScanJob> data) {
        this.data = data;
        return this;
    }
    public java.util.List<ScanJob> getData() {
        return this.data;
    }

    public ListDataScanJobsResponse setNextToken(String nextToken) {
        this.nextToken = nextToken;
        return this;
    }
    public String getNextToken() {
        return this.nextToken;
    }

    public ListDataScanJobsResponse setTotalCount(Integer totalCount) {
        this.totalCount = totalCount;
        return this;
    }
    public Integer getTotalCount() {
        return this.totalCount;
    }

    public ListDataScanJobsResponse setMaxResults(Integer maxResults) {
        this.maxResults = maxResults;
        return this;
    }
    public Integer getMaxResults() {
        return this.maxResults;
    }

}
