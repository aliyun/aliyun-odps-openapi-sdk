// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class DataToken extends TeaModel {
    /**
     * <p>格式版本，目前为 V1</p>
     */
    @NameInMap("version")
    public String version;

    /**
     * <p>类型，目前只支持 STS</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>Token 的内容，base64 编码</p>
     */
    @NameInMap("value")
    public String value;

    /**
     * <p>过期时间</p>
     */
    @NameInMap("expiration")
    public String expiration;

    public static DataToken build(java.util.Map<String, ?> map) throws Exception {
        DataToken self = new DataToken();
        return TeaModel.build(map, self);
    }

    public DataToken setVersion(String version) {
        this.version = version;
        return this;
    }
    public String getVersion() {
        return this.version;
    }

    public DataToken setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public DataToken setValue(String value) {
        this.value = value;
        return this;
    }
    public String getValue() {
        return this.value;
    }

    public DataToken setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

}
