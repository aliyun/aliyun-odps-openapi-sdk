// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class Clustering extends TeaModel {
    /**
     * <p>表的聚簇类型，目前支持 hash/range。</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>聚簇列定义。</p>
     */
    @NameInMap("fields")
    public java.util.List<String> fields;

    /**
     * <p>聚簇桶的个数。只有 hash clustering 才有此属性。创建 hash clustering 表时，如不指定桶个数，默认为 16。</p>
     */
    @NameInMap("numBuckets")
    public String numBuckets;

    public static Clustering build(java.util.Map<String, ?> map) throws Exception {
        Clustering self = new Clustering();
        return TeaModel.build(map, self);
    }

    public Clustering setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public Clustering setFields(java.util.List<String> fields) {
        this.fields = fields;
        return this;
    }
    public java.util.List<String> getFields() {
        return this.fields;
    }

    public Clustering setNumBuckets(String numBuckets) {
        this.numBuckets = numBuckets;
        return this;
    }
    public String getNumBuckets() {
        return this.numBuckets;
    }

}
