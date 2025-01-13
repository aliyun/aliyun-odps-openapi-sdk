// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class PartitionDefinition extends TeaModel {
    @NameInMap("partitionedColumn")
    public java.util.List<PartitionedColumn> partitionedColumn;

    public static PartitionDefinition build(java.util.Map<String, ?> map) throws Exception {
        PartitionDefinition self = new PartitionDefinition();
        return TeaModel.build(map, self);
    }

    public PartitionDefinition setPartitionedColumn(java.util.List<PartitionedColumn> partitionedColumn) {
        this.partitionedColumn = partitionedColumn;
        return this;
    }
    public java.util.List<PartitionedColumn> getPartitionedColumn() {
        return this.partitionedColumn;
    }

}
