// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class TableFormatDefinition extends TeaModel {
    @NameInMap("transactional")
    public Boolean transactional;

    @NameInMap("version")
    public String version;

    public static TableFormatDefinition build(java.util.Map<String, ?> map) throws Exception {
        TableFormatDefinition self = new TableFormatDefinition();
        return TeaModel.build(map, self);
    }

    public TableFormatDefinition setTransactional(Boolean transactional) {
        this.transactional = transactional;
        return this;
    }
    public Boolean getTransactional() {
        return this.transactional;
    }

    public TableFormatDefinition setVersion(String version) {
        this.version = version;
        return this;
    }
    public String getVersion() {
        return this.version;
    }

}
