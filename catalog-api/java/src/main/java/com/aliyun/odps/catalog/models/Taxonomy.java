// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Taxonomy ====================================</p>
 */
public class Taxonomy extends TeaModel {
    /**
     * <p>资源全局唯一名。e.g., namespaces/{namespace_ID}/taxonomies/{ID}</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。</p>
     */
    @NameInMap("taxonomyName")
    @Validation(required = true)
    public String taxonomyName;

    /**
     * <p>可选。最多 1KB。</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>Taxonomy 下开启的 policy 类型列表，默认为 POLICY_TYPE_UNSPECIFIED</p>
     */
    @NameInMap("activatedPolicyTypes")
    public java.util.List<String> activatedPolicyTypes;

    /**
     * <p>此 Taxonomy 内 policy tag 的个数。</p>
     */
    @NameInMap("policyTagCount")
    public Integer policyTagCount;

    /**
     * <p>Taxonomy 的创建时间戳（毫秒）。仅输出。</p>
     */
    @NameInMap("createTime")
    public String createTime;

    /**
     * <p>Taxonomy 的最后修改时间戳（毫秒）。仅输出。</p>
     */
    @NameInMap("lastModifiedTime")
    public String lastModifiedTime;

    public static Taxonomy build(java.util.Map<String, ?> map) throws Exception {
        Taxonomy self = new Taxonomy();
        return TeaModel.build(map, self);
    }

    public Taxonomy setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public Taxonomy setTaxonomyName(String taxonomyName) {
        this.taxonomyName = taxonomyName;
        return this;
    }
    public String getTaxonomyName() {
        return this.taxonomyName;
    }

    public Taxonomy setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public Taxonomy setActivatedPolicyTypes(java.util.List<String> activatedPolicyTypes) {
        this.activatedPolicyTypes = activatedPolicyTypes;
        return this;
    }
    public java.util.List<String> getActivatedPolicyTypes() {
        return this.activatedPolicyTypes;
    }

    public Taxonomy setPolicyTagCount(Integer policyTagCount) {
        this.policyTagCount = policyTagCount;
        return this;
    }
    public Integer getPolicyTagCount() {
        return this.policyTagCount;
    }

    public Taxonomy setCreateTime(String createTime) {
        this.createTime = createTime;
        return this;
    }
    public String getCreateTime() {
        return this.createTime;
    }

    public Taxonomy setLastModifiedTime(String lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
        return this;
    }
    public String getLastModifiedTime() {
        return this.lastModifiedTime;
    }

}
