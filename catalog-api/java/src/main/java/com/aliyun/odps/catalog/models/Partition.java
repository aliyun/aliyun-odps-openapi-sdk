// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Partition ====================================</p>
 */
public class Partition extends TeaModel {
    /**
     * <p>分区spec，格式样例为 bu=tt/ds=20250515</p>
     */
    @NameInMap("spec")
    public String spec;

    /**
     * <p>分区的创建时间（毫秒）。仅输出。</p>
     */
    @NameInMap("createTime")
    public String createTime;

    /**
     * <p>分区的修改时间（毫秒）。仅输出。</p>
     */
    @NameInMap("lastModifiedTime")
    public String lastModifiedTime;

    /**
     * <p>分区的最后访问时间（毫秒）。仅输出。</p>
     */
    @NameInMap("lastAccessTime")
    public String lastAccessTime;

    public static Partition build(java.util.Map<String, ?> map) throws Exception {
        Partition self = new Partition();
        return TeaModel.build(map, self);
    }

    public Partition setSpec(String spec) {
        this.spec = spec;
        return this;
    }
    public String getSpec() {
        return this.spec;
    }

    public Partition setCreateTime(String createTime) {
        this.createTime = createTime;
        return this;
    }
    public String getCreateTime() {
        return this.createTime;
    }

    public Partition setLastModifiedTime(String lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
        return this;
    }
    public String getLastModifiedTime() {
        return this.lastModifiedTime;
    }

    public Partition setLastAccessTime(String lastAccessTime) {
        this.lastAccessTime = lastAccessTime;
        return this;
    }
    public String getLastAccessTime() {
        return this.lastAccessTime;
    }

}
