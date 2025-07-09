// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class DataMaskingPolicy extends TeaModel {
    /**
     * <p>预定义脱敏策略的类型。</p>
     */
    @NameInMap("predefinedExpression")
    @Validation(required = true)
    public String predefinedExpression;

    /**
     * <p>预定义脱敏策略的参数。</p>
     */
    @NameInMap("parameters")
    public java.util.List<String> parameters;

    public static DataMaskingPolicy build(java.util.Map<String, ?> map) throws Exception {
        DataMaskingPolicy self = new DataMaskingPolicy();
        return TeaModel.build(map, self);
    }

    public DataMaskingPolicy setPredefinedExpression(String predefinedExpression) {
        this.predefinedExpression = predefinedExpression;
        return this;
    }
    public String getPredefinedExpression() {
        return this.predefinedExpression;
    }

    public DataMaskingPolicy setParameters(java.util.List<String> parameters) {
        this.parameters = parameters;
        return this;
    }
    public java.util.List<String> getParameters() {
        return this.parameters;
    }

}
