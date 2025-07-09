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
    @Validation(required = true)
    public String spec;

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

}
