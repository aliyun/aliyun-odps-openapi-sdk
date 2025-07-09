// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== DataPolicy ====================================</p>
 */
public class DataPolicy extends TeaModel {
    /**
     * <p>namespaces/{namespace_ID}/dataPolicies/{dataPolicyName}。仅输出。</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>用户指定的 data policy 名，在账号级唯一。</p>
     */
    @NameInMap("dataPolicyName")
    @Validation(required = true)
    public String dataPolicyName;

    /**
     * <p>Data policy 绑定的 policy tag 资源全名。</p>
     */
    @NameInMap("policyTag")
    @Validation(required = true)
    public String policyTag;

    /**
     * <p>data policy 的类型，目前仅支持 DATA_MASKING_POLICY 类型。</p>
     */
    @NameInMap("dataPolicyType")
    @Validation(required = true)
    public String dataPolicyType;

    /**
     * <p>Data policy 上定义的脱敏规则。</p>
     */
    @NameInMap("dataMaskingPolicy")
    public DataMaskingPolicy dataMaskingPolicy;

    public static DataPolicy build(java.util.Map<String, ?> map) throws Exception {
        DataPolicy self = new DataPolicy();
        return TeaModel.build(map, self);
    }

    public DataPolicy setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public DataPolicy setDataPolicyName(String dataPolicyName) {
        this.dataPolicyName = dataPolicyName;
        return this;
    }
    public String getDataPolicyName() {
        return this.dataPolicyName;
    }

    public DataPolicy setPolicyTag(String policyTag) {
        this.policyTag = policyTag;
        return this;
    }
    public String getPolicyTag() {
        return this.policyTag;
    }

    public DataPolicy setDataPolicyType(String dataPolicyType) {
        this.dataPolicyType = dataPolicyType;
        return this;
    }
    public String getDataPolicyType() {
        return this.dataPolicyType;
    }

    public DataPolicy setDataMaskingPolicy(DataMaskingPolicy dataMaskingPolicy) {
        this.dataMaskingPolicy = dataMaskingPolicy;
        return this;
    }
    public DataMaskingPolicy getDataMaskingPolicy() {
        return this.dataMaskingPolicy;
    }

}
