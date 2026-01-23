// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Search ====================================</p>
 */
public class SearchResultEntry extends TeaModel {
    /**
     * <p>实体的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/tables/{tableName}</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>实体的名称</p>
     */
    @NameInMap("displayName")
    public String displayName;

    /**
     * <p>实体的类型，例如 TABLE、RESOURCE、SCHEMA 等</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>实体的其他信息</p>
     */
    @NameInMap("aspects")
    public java.util.Map<String, String> aspects;

    /**
     * <p>实体的创建时间（毫秒）</p>
     */
    @NameInMap("createTime")
    public String createTime;

    /**
     * <p>实体的修改时间（毫秒）</p>
     */
    @NameInMap("lastModifiedTime")
    public String lastModifiedTime;

    /**
     * <p>实体的描述</p>
     */
    @NameInMap("description")
    public String description;

    public static SearchResultEntry build(java.util.Map<String, ?> map) throws Exception {
        SearchResultEntry self = new SearchResultEntry();
        return TeaModel.build(map, self);
    }

    public SearchResultEntry setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public SearchResultEntry setDisplayName(String displayName) {
        this.displayName = displayName;
        return this;
    }
    public String getDisplayName() {
        return this.displayName;
    }

    public SearchResultEntry setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public SearchResultEntry setAspects(java.util.Map<String, String> aspects) {
        this.aspects = aspects;
        return this;
    }
    public java.util.Map<String, String> getAspects() {
        return this.aspects;
    }

    public SearchResultEntry setCreateTime(String createTime) {
        this.createTime = createTime;
        return this;
    }
    public String getCreateTime() {
        return this.createTime;
    }

    public SearchResultEntry setLastModifiedTime(String lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
        return this;
    }
    public String getLastModifiedTime() {
        return this.lastModifiedTime;
    }

    public SearchResultEntry setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

}
