// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>Model for initing client</p>
 */
public class Config extends TeaModel {
    /**
     * <p>project</p>
     */
    @NameInMap("project")
    public String project;

    /**
     * <p>accesskey id</p>
     */
    @NameInMap("accessKeyId")
    public String accessKeyId;

    /**
     * <p>accesskey secret</p>
     */
    @NameInMap("accessKeySecret")
    public String accessKeySecret;

    /**
     * <p>security token</p>
     * 
     * <strong>example:</strong>
     * <p>a.txt</p>
     */
    @NameInMap("securityToken")
    public String securityToken;

    /**
     * <p>bearer token</p>
     * 
     * <strong>example:</strong>
     * <p>the-bearer-token</p>
     */
    @NameInMap("bearerToken")
    public String bearerToken;

    /**
     * <p>http protocol</p>
     * 
     * <strong>example:</strong>
     * <p>http</p>
     */
    @NameInMap("protocol")
    public String protocol;

    /**
     * <p>http method</p>
     * 
     * <strong>example:</strong>
     * <p>GET</p>
     */
    @NameInMap("method")
    public String method;

    /**
     * <p>region id</p>
     * 
     * <strong>example:</strong>
     * <p>cn-hangzhou</p>
     */
    @NameInMap("regionId")
    public String regionId;

    /**
     * <p>read timeout</p>
     * 
     * <strong>example:</strong>
     * <p>60</p>
     */
    @NameInMap("readTimeout")
    public Integer readTimeout;

    /**
     * <p>connect timeout</p>
     * 
     * <strong>example:</strong>
     * <p>60</p>
     */
    @NameInMap("connectTimeout")
    public Integer connectTimeout;

    /**
     * <p>credential</p>
     */
    @NameInMap("credential")
    public com.aliyun.credentials.Client credential;

    /**
     * <p>endpoint</p>
     * 
     * <strong>example:</strong>
     * <p>cs.aliyuncs.com</p>
     */
    @NameInMap("endpoint")
    public String endpoint;

    /**
     * <p>credential type</p>
     * 
     * <strong>example:</strong>
     * <p>access_key</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>user agent</p>
     * 
     * <strong>example:</strong>
     * <p>maxcompute-openapi</p>
     */
    @NameInMap("userAgent")
    public String userAgent;

    /**
     * <p>suffix for endpoint</p>
     * 
     * <strong>example:</strong>
     * <p>aliyun</p>
     */
    @NameInMap("suffix")
    public String suffix;

    /**
     * <p>Signature Version</p>
     * 
     * <strong>example:</strong>
     * <p>v2</p>
     */
    @NameInMap("signatureVersion")
    public String signatureVersion;

    /**
     * <p>Global Parameters</p>
     */
    @NameInMap("globalParameters")
    public GlobalParameters globalParameters;

    public static Config build(java.util.Map<String, ?> map) throws Exception {
        Config self = new Config();
        return TeaModel.build(map, self);
    }

    public Config setProject(String project) {
        this.project = project;
        return this;
    }
    public String getProject() {
        return this.project;
    }

    public Config setAccessKeyId(String accessKeyId) {
        this.accessKeyId = accessKeyId;
        return this;
    }
    public String getAccessKeyId() {
        return this.accessKeyId;
    }

    public Config setAccessKeySecret(String accessKeySecret) {
        this.accessKeySecret = accessKeySecret;
        return this;
    }
    public String getAccessKeySecret() {
        return this.accessKeySecret;
    }

    public Config setSecurityToken(String securityToken) {
        this.securityToken = securityToken;
        return this;
    }
    public String getSecurityToken() {
        return this.securityToken;
    }

    public Config setBearerToken(String bearerToken) {
        this.bearerToken = bearerToken;
        return this;
    }
    public String getBearerToken() {
        return this.bearerToken;
    }

    public Config setProtocol(String protocol) {
        this.protocol = protocol;
        return this;
    }
    public String getProtocol() {
        return this.protocol;
    }

    public Config setMethod(String method) {
        this.method = method;
        return this;
    }
    public String getMethod() {
        return this.method;
    }

    public Config setRegionId(String regionId) {
        this.regionId = regionId;
        return this;
    }
    public String getRegionId() {
        return this.regionId;
    }

    public Config setReadTimeout(Integer readTimeout) {
        this.readTimeout = readTimeout;
        return this;
    }
    public Integer getReadTimeout() {
        return this.readTimeout;
    }

    public Config setConnectTimeout(Integer connectTimeout) {
        this.connectTimeout = connectTimeout;
        return this;
    }
    public Integer getConnectTimeout() {
        return this.connectTimeout;
    }

    public Config setCredential(com.aliyun.credentials.Client credential) {
        this.credential = credential;
        return this;
    }
    public com.aliyun.credentials.Client getCredential() {
        return this.credential;
    }

    public Config setEndpoint(String endpoint) {
        this.endpoint = endpoint;
        return this;
    }
    public String getEndpoint() {
        return this.endpoint;
    }

    public Config setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public Config setUserAgent(String userAgent) {
        this.userAgent = userAgent;
        return this;
    }
    public String getUserAgent() {
        return this.userAgent;
    }

    public Config setSuffix(String suffix) {
        this.suffix = suffix;
        return this;
    }
    public String getSuffix() {
        return this.suffix;
    }

    public Config setSignatureVersion(String signatureVersion) {
        this.signatureVersion = signatureVersion;
        return this;
    }
    public String getSignatureVersion() {
        return this.signatureVersion;
    }

    public Config setGlobalParameters(GlobalParameters globalParameters) {
        this.globalParameters = globalParameters;
        return this;
    }
    public GlobalParameters getGlobalParameters() {
        return this.globalParameters;
    }

}
