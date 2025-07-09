// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Role ====================================</p>
 */
public class Role extends TeaModel {
    /**
     * <p>资源全局唯一名。e.g., namespaces/{namespace_ID}/roles/{roleName}</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>namespace 内唯一。大小写敏感。包含字符：[a-z][A-Z][0-9]_，字节数范围 [3, 255]。</p>
     */
    @NameInMap("roleName")
    @Validation(required = true)
    public String roleName;

    /**
     * <p>可选。最多 1KB。</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>Role 包含的权限。</p>
     */
    @NameInMap("includedPermissions")
    public java.util.List<String> includedPermissions;

    /**
     * <p>用于一致性校验。</p>
     */
    @NameInMap("etag")
    public String etag;

    /**
     * <p>表示是否被删除。</p>
     * 
     * <strong>example:</strong>
     * <p>false</p>
     */
    @NameInMap("deleted")
    public Boolean deleted;

    public static Role build(java.util.Map<String, ?> map) throws Exception {
        Role self = new Role();
        return TeaModel.build(map, self);
    }

    public Role setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public Role setRoleName(String roleName) {
        this.roleName = roleName;
        return this;
    }
    public String getRoleName() {
        return this.roleName;
    }

    public Role setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public Role setIncludedPermissions(java.util.List<String> includedPermissions) {
        this.includedPermissions = includedPermissions;
        return this;
    }
    public java.util.List<String> getIncludedPermissions() {
        return this.includedPermissions;
    }

    public Role setEtag(String etag) {
        this.etag = etag;
        return this;
    }
    public String getEtag() {
        return this.etag;
    }

    public Role setDeleted(Boolean deleted) {
        this.deleted = deleted;
        return this;
    }
    public Boolean getDeleted() {
        return this.deleted;
    }

}
