// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class PolicyTag extends TeaModel {
    /**
     * <p>PolicyTag的完整路径。e.g., namespaces/{namespace_ID}/taxonomies/{TID}/policyTags/{ID}</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>父 Taxonomy 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。</p>
     */
    @NameInMap("policyTagName")
    @Validation(required = true)
    public String policyTagName;

    /**
     * <p>可选。最多 1KB。</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>父节点的name。空代表根节点。</p>
     */
    @NameInMap("parentPolicyTag")
    public String parentPolicyTag;

    /**
     * <p>子节点的name列表。仅输出。</p>
     */
    @NameInMap("childPolicyTags")
    public java.util.List<String> childPolicyTags;

    public static PolicyTag build(java.util.Map<String, ?> map) throws Exception {
        PolicyTag self = new PolicyTag();
        return TeaModel.build(map, self);
    }

    public PolicyTag setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public PolicyTag setPolicyTagName(String policyTagName) {
        this.policyTagName = policyTagName;
        return this;
    }
    public String getPolicyTagName() {
        return this.policyTagName;
    }

    public PolicyTag setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public PolicyTag setParentPolicyTag(String parentPolicyTag) {
        this.parentPolicyTag = parentPolicyTag;
        return this;
    }
    public String getParentPolicyTag() {
        return this.parentPolicyTag;
    }

    public PolicyTag setChildPolicyTags(java.util.List<String> childPolicyTags) {
        this.childPolicyTags = childPolicyTags;
        return this;
    }
    public java.util.List<String> getChildPolicyTags() {
        return this.childPolicyTags;
    }

}
