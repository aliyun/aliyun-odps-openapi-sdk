// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class SetPolicyRequest extends TeaModel {
    /**
     * <p>设置的 Policy。</p>
     */
    @NameInMap("policy")
    @Validation(required = true)
    public Policy policy;

    public static SetPolicyRequest build(java.util.Map<String, ?> map) throws Exception {
        SetPolicyRequest self = new SetPolicyRequest();
        return TeaModel.build(map, self);
    }

    public SetPolicyRequest setPolicy(Policy policy) {
        this.policy = policy;
        return this;
    }
    public Policy getPolicy() {
        return this.policy;
    }

}
