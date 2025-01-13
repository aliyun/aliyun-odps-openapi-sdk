// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class Fields extends TeaModel {
    /**
     * <p>主键列名列表。</p>
     */
    @NameInMap("fields")
    public java.util.List<String> fields;

    public static Fields build(java.util.Map<String, ?> map) throws Exception {
        Fields self = new Fields();
        return TeaModel.build(map, self);
    }

    public Fields setFields(java.util.List<String> fields) {
        this.fields = fields;
        return this;
    }
    public java.util.List<String> getFields() {
        return this.fields;
    }

}
