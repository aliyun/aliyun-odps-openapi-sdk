// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class PartitionDefinition extends TeaModel {
    @NameInMap("partitionedColumns")
    public java.util.List<PartitionedColumn> partitionedColumns;

    public static PartitionDefinition build(java.util.Map<String, ?> map) throws Exception {
        PartitionDefinition self = new PartitionDefinition();
        return TeaModel.build(map, self);
    }

    public PartitionDefinition setPartitionedColumns(java.util.List<PartitionedColumn> partitionedColumns) {
        this.partitionedColumns = partitionedColumns;
        return this;
    }
    public java.util.List<PartitionedColumn> getPartitionedColumns() {
        return this.partitionedColumns;
    }

}
