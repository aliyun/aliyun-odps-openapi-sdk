// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class CloudResourceOptions extends TeaModel {
    /**
     * <p>被委托的账号名。在创建 connection 时自动保存为创建者的账号。</p>
     */
    @NameInMap("delegatedAccount")
    public String delegatedAccount;

    /**
     * <p>授权给 MaxCompute 服务扮演的 RAM 角色 ARN。</p>
     */
    @NameInMap("ramRoleArn")
    @Validation(required = true)
    public String ramRoleArn;

    public static CloudResourceOptions build(java.util.Map<String, ?> map) throws Exception {
        CloudResourceOptions self = new CloudResourceOptions();
        return TeaModel.build(map, self);
    }

    public CloudResourceOptions setDelegatedAccount(String delegatedAccount) {
        this.delegatedAccount = delegatedAccount;
        return this;
    }
    public String getDelegatedAccount() {
        return this.delegatedAccount;
    }

    public CloudResourceOptions setRamRoleArn(String ramRoleArn) {
        this.ramRoleArn = ramRoleArn;
        return this;
    }
    public String getRamRoleArn() {
        return this.ramRoleArn;
    }

}
