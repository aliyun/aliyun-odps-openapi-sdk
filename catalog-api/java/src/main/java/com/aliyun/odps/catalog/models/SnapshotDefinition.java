// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class SnapshotDefinition extends TeaModel {
    /**
     * <p>源表所在的 project 名。</p>
     */
    @NameInMap("fromProjectName")
    public String fromProjectName;

    /**
     * <p>源表所在的 schema 名。</p>
     */
    @NameInMap("fromSchemaName")
    public String fromSchemaName;

    /**
     * <p>源表名。</p>
     */
    @NameInMap("fromTableName")
    public String fromTableName;

    public static SnapshotDefinition build(java.util.Map<String, ?> map) throws Exception {
        SnapshotDefinition self = new SnapshotDefinition();
        return TeaModel.build(map, self);
    }

    public SnapshotDefinition setFromProjectName(String fromProjectName) {
        this.fromProjectName = fromProjectName;
        return this;
    }
    public String getFromProjectName() {
        return this.fromProjectName;
    }

    public SnapshotDefinition setFromSchemaName(String fromSchemaName) {
        this.fromSchemaName = fromSchemaName;
        return this;
    }
    public String getFromSchemaName() {
        return this.fromSchemaName;
    }

    public SnapshotDefinition setFromTableName(String fromTableName) {
        this.fromTableName = fromTableName;
        return this;
    }
    public String getFromTableName() {
        return this.fromTableName;
    }

}
