// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class TableConstraints extends TeaModel {
    /**
     * <p>表的主键。系统不为主键自动去重。</p>
     */
    @NameInMap("primaryKey")
    public Fields primaryKey;

    public static TableConstraints build(java.util.Map<String, ?> map) throws Exception {
        TableConstraints self = new TableConstraints();
        return TeaModel.build(map, self);
    }

    public TableConstraints setPrimaryKey(Fields primaryKey) {
        this.primaryKey = primaryKey;
        return this;
    }
    public Fields getPrimaryKey() {
        return this.primaryKey;
    }

}
