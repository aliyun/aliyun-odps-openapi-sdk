// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class PartitionedColumn extends TeaModel {
    @NameInMap("field")
    public String field;

    public static PartitionedColumn build(java.util.Map<String, ?> map) throws Exception {
        PartitionedColumn self = new PartitionedColumn();
        return TeaModel.build(map, self);
    }

    public PartitionedColumn setField(String field) {
        this.field = field;
        return this;
    }
    public String getField() {
        return this.field;
    }

}
