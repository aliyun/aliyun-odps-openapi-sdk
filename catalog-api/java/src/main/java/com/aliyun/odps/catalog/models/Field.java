// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class Field extends TeaModel {
    /**
     * <p>列名（如果是顶层列），或者 struct 字段名。</p>
     */
    @NameInMap("fieldName")
    public String fieldName;

    public static Field build(java.util.Map<String, ?> map) throws Exception {
        Field self = new Field();
        return TeaModel.build(map, self);
    }

    public Field setFieldName(String fieldName) {
        this.fieldName = fieldName;
        return this;
    }
    public String getFieldName() {
        return this.fieldName;
    }

}
