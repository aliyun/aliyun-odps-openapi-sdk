// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListDataScansResponse extends TeaModel {
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
     * <p>分页参数，每页最大结果数</p>
     */
    @NameInMap("maxResults")
    public Integer maxResults;

    /**
     * <p>返回所有的 dataScans 列表。</p>
     */
    @NameInMap("dataScans")
    public java.util.List<DataScan> dataScans;

    public static ListDataScansResponse build(java.util.Map<String, ?> map) throws Exception {
        ListDataScansResponse self = new ListDataScansResponse();
        return TeaModel.build(map, self);
    }

    public ListDataScansResponse setNextToken(String nextToken) {
        this.nextToken = nextToken;
        return this;
    }
    public String getNextToken() {
        return this.nextToken;
    }

    public ListDataScansResponse setTotalCount(Integer totalCount) {
        this.totalCount = totalCount;
        return this;
    }
    public Integer getTotalCount() {
        return this.totalCount;
    }

    public ListDataScansResponse setMaxResults(Integer maxResults) {
        this.maxResults = maxResults;
        return this;
    }
    public Integer getMaxResults() {
        return this.maxResults;
    }

    public ListDataScansResponse setDataScans(java.util.List<DataScan> dataScans) {
        this.dataScans = dataScans;
        return this;
    }
    public java.util.List<DataScan> getDataScans() {
        return this.dataScans;
    }

}
