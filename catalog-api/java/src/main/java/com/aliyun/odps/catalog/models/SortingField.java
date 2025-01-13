// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class SortingField extends TeaModel {
    /**
     * <p>列名（如果是顶层列），或者 struct 字段名。</p>
     */
    @NameInMap("fieldName")
    public String fieldName;

    /**
     * <p>排序顺序</p>
     * 
     * <strong>example:</strong>
     * <p>DESC</p>
     */
    @NameInMap("order")
    public String order;

    public static SortingField build(java.util.Map<String, ?> map) throws Exception {
        SortingField self = new SortingField();
        return TeaModel.build(map, self);
    }

    public SortingField setFieldName(String fieldName) {
        this.fieldName = fieldName;
        return this;
    }
    public String getFieldName() {
        return this.fieldName;
    }

    public SortingField setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

}
