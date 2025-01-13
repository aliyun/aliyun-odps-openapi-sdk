// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ExpirationOptions extends TeaModel {
    @NameInMap("expirationDays")
    public Integer expirationDays;

    @NameInMap("partitionExpirationDays")
    public Integer partitionExpirationDays;

    public static ExpirationOptions build(java.util.Map<String, ?> map) throws Exception {
        ExpirationOptions self = new ExpirationOptions();
        return TeaModel.build(map, self);
    }

    public ExpirationOptions setExpirationDays(Integer expirationDays) {
        this.expirationDays = expirationDays;
        return this;
    }
    public Integer getExpirationDays() {
        return this.expirationDays;
    }

    public ExpirationOptions setPartitionExpirationDays(Integer partitionExpirationDays) {
        this.partitionExpirationDays = partitionExpirationDays;
        return this;
    }
    public Integer getPartitionExpirationDays() {
        return this.partitionExpirationDays;
    }

}
