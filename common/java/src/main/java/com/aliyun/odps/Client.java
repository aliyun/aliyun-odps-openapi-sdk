// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps;

import com.aliyun.tea.*;
import com.aliyun.tea.interceptor.InterceptorChain;
import com.aliyun.tea.interceptor.RuntimeOptionsInterceptor;
import com.aliyun.tea.interceptor.RequestInterceptor;
import com.aliyun.tea.interceptor.ResponseInterceptor;
import com.aliyun.odps.models.*;

public class Client {

    private final static InterceptorChain interceptorChain = InterceptorChain.create();

    public String _endpoint;
    public String _project;
    public String _regionId;
    public String _protocol;
    public String _method;
    public String _userAgent;
    public Integer _readTimeout;
    public Integer _connectTimeout;
    public com.aliyun.credentials.Client _credential;
    public String _signatureVersion;
    public java.util.Map<String, String> _headers;
    public String _suffix;
    public GlobalParameters _globalParameters;
    /**
     * <b>description</b> :
     * <p>Init client with Config</p>
     * 
     * @param config config contains the necessary information to create a client
     */
    public Client(com.aliyun.odps.models.Config config) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(config)) {
            throw new TeaException(TeaConverter.buildMap(
                new TeaPair("code", "ParameterMissing"),
                new TeaPair("message", "'config' can not be unset")
            ));
        }

        if (!com.aliyun.teautil.Common.empty(config.accessKeyId) && !com.aliyun.teautil.Common.empty(config.accessKeySecret)) {
            if (!com.aliyun.teautil.Common.empty(config.securityToken)) {
                config.type = "sts";
            } else {
                config.type = "access_key";
            }

            com.aliyun.credentials.models.Config credentialConfig = com.aliyun.credentials.models.Config.build(TeaConverter.buildMap(
                new TeaPair("accessKeyId", config.accessKeyId),
                new TeaPair("type", config.type),
                new TeaPair("accessKeySecret", config.accessKeySecret)
            ));
            credentialConfig.securityToken = config.securityToken;
            this._credential = new com.aliyun.credentials.Client(credentialConfig);
        } else if (!com.aliyun.teautil.Common.empty(config.bearerToken)) {
            com.aliyun.credentials.models.Config cc = com.aliyun.credentials.models.Config.build(TeaConverter.buildMap(
                new TeaPair("type", "bearer"),
                new TeaPair("bearerToken", config.bearerToken)
            ));
            this._credential = new com.aliyun.credentials.Client(cc);
        } else if (!com.aliyun.teautil.Common.isUnset(config.credential)) {
            this._credential = config.credential;
        }

        this._project = config.project;
        this._endpoint = config.endpoint;
        this._protocol = config.protocol;
        this._method = config.method;
        this._regionId = config.regionId;
        this._userAgent = config.userAgent;
        this._readTimeout = config.readTimeout;
        this._connectTimeout = config.connectTimeout;
        this._signatureVersion = config.signatureVersion;
        this._globalParameters = config.globalParameters;
        this._suffix = config.suffix;
    }

    /**
     * <b>description</b> :
     * <p>Encapsulate the request and invoke the network</p>
     * 
     * @param action api name
     * @param version product version
     * @param protocol http or https
     * @param method e.g. GET
     * @param authType authorization type e.g. AK
     * @param bodyType response body type e.g. String
     * @param request object of OpenApiRequest
     * @param runtime which controls some details of call api, such as retry times
     * @return the response
     */
    public java.util.Map<String, ?> doRequest(Params params, OpenApiRequest request, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        TeaModel.validateParams(params, "params");
        TeaModel.validateParams(request, "request");
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", com.aliyun.teautil.Common.defaultNumber(runtime.readTimeout, _readTimeout)),
            new TeaPair("connectTimeout", com.aliyun.teautil.Common.defaultNumber(runtime.connectTimeout, _connectTimeout)),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        Exception _lastException = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, params.protocol);
                request_.method = params.method;
                if (!com.aliyun.teautil.Common.isUnset(_suffix)) {
                    request_.pathname = "/" + _suffix + "" + params.pathname + "";
                } else {
                    request_.pathname = params.pathname;
                }

                java.util.Map<String, String> globalQueries = new java.util.HashMap<>();
                java.util.Map<String, String> globalHeaders = new java.util.HashMap<>();
                if (!com.aliyun.teautil.Common.isUnset(_globalParameters)) {
                    GlobalParameters globalParams = _globalParameters;
                    if (!com.aliyun.teautil.Common.isUnset(globalParams.queries)) {
                        globalQueries = globalParams.queries;
                    }

                    if (!com.aliyun.teautil.Common.isUnset(globalParams.headers)) {
                        globalHeaders = globalParams.headers;
                    }

                }

                java.util.Map<String, String> extendsHeaders = new java.util.HashMap<>();
                java.util.Map<String, String> extendsQueries = new java.util.HashMap<>();
                if (!com.aliyun.teautil.Common.isUnset(runtime.extendsParameters)) {
                    com.aliyun.teautil.models.ExtendsParameters extendsParameters = runtime.extendsParameters;
                    if (!com.aliyun.teautil.Common.isUnset(extendsParameters.headers)) {
                        extendsHeaders = extendsParameters.headers;
                    }

                    if (!com.aliyun.teautil.Common.isUnset(extendsParameters.queries)) {
                        extendsQueries = extendsParameters.queries;
                    }

                }

                request_.query = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("curr_project", _project)
                    ),
                    globalQueries,
                    extendsQueries,
                    request.query
                );
                // endpoint is setted in product client
                request_.headers = TeaConverter.merge(String.class,
                    TeaConverter.buildMap(
                        new TeaPair("host", _endpoint),
                        new TeaPair("user-agent", this.getUserAgent()),
                        new TeaPair("x-odps-user-agent", this.getUserAgent()),
                        new TeaPair("Date", com.aliyun.odps.utils.TeaUtils.getApiTimestamp())
                    ),
                    globalHeaders,
                    extendsHeaders,
                    request.headers
                );
                if (!com.aliyun.teautil.Common.isUnset(request.stream)) {
                    byte[] tmp = com.aliyun.teautil.Common.readAsBytes(request.stream);
                    request_.body = Tea.toReadable(tmp);
                }

                if (!com.aliyun.teautil.Common.isUnset(request.body)) {
                    String jsonObj = com.aliyun.teautil.Common.toJSONString(request.body);
                    request_.body = Tea.toReadable(jsonObj);
                    request_.headers.put("content-type", "application/json; charset=utf-8");
                }

                String canonicalString = com.aliyun.odps.utils.TeaUtils.buildCanonicalString(params.method, params.pathname, request_.query, request_.headers);
                if (!com.aliyun.teautil.Common.equalString(params.authType, "Anonymous")) {
                    if (com.aliyun.teautil.Common.isUnset(_credential)) {
                        throw new TeaException(TeaConverter.buildMap(
                            new TeaPair("code", "InvalidCredentials"),
                            new TeaPair("message", "Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.")
                        ));
                    }

                    com.aliyun.credentials.models.CredentialModel credentialModel = _credential.getCredential();
                    String authType = credentialModel.type;
                    if (com.aliyun.teautil.Common.equalString(authType, "bearer")) {
                        String bearerToken = credentialModel.bearerToken;
                        request_.headers.put("x-odps-bearer-token", bearerToken);
                    } else {
                        String accessKeyId = credentialModel.accessKeyId;
                        String accessKeySecret = credentialModel.accessKeySecret;
                        String securityToken = credentialModel.securityToken;
                        request_.headers.put("Authorization", com.aliyun.odps.utils.TeaUtils.getSignature(canonicalString, accessKeyId, accessKeySecret));
                        if (!com.aliyun.teautil.Common.empty(securityToken)) {
                            request_.headers.put("authorization-sts-token", securityToken);
                        }

                    }

                }

                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_, interceptorChain);

                if (com.aliyun.teautil.Common.equalNumber(response_.statusCode, 204)) {
                    return TeaConverter.buildMap(
                        new TeaPair("headers", response_.headers)
                    );
                }

                if (com.aliyun.teautil.Common.is4xx(response_.statusCode) || com.aliyun.teautil.Common.is5xx(response_.statusCode)) {
                    Object _res = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    java.util.Map<String, Object> err = com.aliyun.teautil.Common.assertAsMap(_res);
                    Object requestId = Client.defaultAny(response_.headers.get("x-odps-request-id"), response_.headers.get("X-Odps-Request-Id"));
                    err.put("statusCode", response_.statusCode);
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("code", "" + Client.defaultAny(err.get("Code"), err.get("code")) + ""),
                        new TeaPair("message", "code: " + response_.statusCode + ", " + Client.defaultAny(err.get("Message"), err.get("message")) + " request id: " + requestId + ""),
                        new TeaPair("data", err),
                        new TeaPair("description", "" + Client.defaultAny(err.get("Description"), err.get("description")) + ""),
                        new TeaPair("accessDeniedDetail", Client.defaultAny(err.get("AccessDeniedDetail"), err.get("accessDeniedDetail")))
                    ));
                }

                if (com.aliyun.teautil.Common.equalString(params.bodyType, "binary")) {
                    java.util.Map<String, Object> resp = TeaConverter.buildMap(
                        new TeaPair("body", response_.body),
                        new TeaPair("headers", response_.headers),
                        new TeaPair("statusCode", response_.statusCode)
                    );
                    return resp;
                } else if (com.aliyun.teautil.Common.equalString(params.bodyType, "byte")) {
                    byte[] byt = com.aliyun.teautil.Common.readAsBytes(response_.body);
                    return TeaConverter.buildMap(
                        new TeaPair("body", byt),
                        new TeaPair("headers", response_.headers),
                        new TeaPair("statusCode", response_.statusCode)
                    );
                } else if (com.aliyun.teautil.Common.equalString(params.bodyType, "string")) {
                    String str = com.aliyun.teautil.Common.readAsString(response_.body);
                    return TeaConverter.buildMap(
                        new TeaPair("body", str),
                        new TeaPair("headers", response_.headers),
                        new TeaPair("statusCode", response_.statusCode)
                    );
                } else if (com.aliyun.teautil.Common.equalString(params.bodyType, "json")) {
                    Object obj = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    java.util.Map<String, Object> res = com.aliyun.teautil.Common.assertAsMap(obj);
                    return res;
                } else if (com.aliyun.teautil.Common.equalString(params.bodyType, "array")) {
                    Object arr = com.aliyun.teautil.Common.readAsJSON(response_.body);
                    return TeaConverter.buildMap(
                        new TeaPair("body", arr),
                        new TeaPair("headers", response_.headers),
                        new TeaPair("statusCode", response_.statusCode)
                    );
                } else {
                    String anything = com.aliyun.teautil.Common.readAsString(response_.body);
                    return TeaConverter.buildMap(
                        new TeaPair("body", anything),
                        new TeaPair("headers", response_.headers),
                        new TeaPair("statusCode", response_.statusCode)
                    );
                }

            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    _lastException = e;
                    continue;
                }
                throw e;
            }
        }
        throw new TeaUnretryableException(_lastRequest, _lastException);
    }

    public void addRuntimeOptionsInterceptor(RuntimeOptionsInterceptor interceptor) {
        interceptorChain.addRuntimeOptionsInterceptor(interceptor);
    }

    public void addRequestInterceptor(RequestInterceptor interceptor) {
        interceptorChain.addRequestInterceptor(interceptor);
    }

    public void addResponseInterceptor(ResponseInterceptor interceptor) {
        interceptorChain.addResponseInterceptor(interceptor);
    }

    public java.util.Map<String, ?> requestWithModel(TeaModel model, String method, String path, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        com.aliyun.teautil.Common.validateModel(model);
        OpenApiRequest req = OpenApiRequest.build(TeaConverter.buildMap(
            new TeaPair("body", com.aliyun.teautil.Common.toMap(model))
        ));
        Params openapiParams = Params.build(TeaConverter.buildMap(
            new TeaPair("pathname", path),
            new TeaPair("method", method),
            new TeaPair("bodyType", "json")
        ));
        return this.callApi(openapiParams, req, runtime);
    }

    public java.util.Map<String, ?> requestWithoutModel(TeaModel model, String method, String path, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        com.aliyun.teautil.Common.validateModel(model);
        OpenApiRequest req = OpenApiRequest.build(TeaConverter.buildMap(
            new TeaPair("body", com.aliyun.teautil.Common.toMap(model))
        ));
        Params openapiParams = Params.build(TeaConverter.buildMap(
            new TeaPair("pathname", path),
            new TeaPair("method", method),
            new TeaPair("bodyType", "none")
        ));
        return this.callApi(openapiParams, req, runtime);
    }

    public java.util.Map<String, ?> callApi(Params params, OpenApiRequest request, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(params)) {
            throw new TeaException(TeaConverter.buildMap(
                new TeaPair("code", "ParameterMissing"),
                new TeaPair("message", "'params' can not be unset")
            ));
        }

        return this.doRequest(params, request, runtime);
    }

    /**
     * <b>description</b> :
     * <p>Get user agent</p>
     * @return user agent
     */
    public String getUserAgent() throws Exception {
        String userAgent = com.aliyun.teautil.Common.getUserAgent(_userAgent);
        return userAgent;
    }

    /**
     * <b>description</b> :
     * <p>Get accesskey id by using credential</p>
     * @return accesskey id
     */
    public String getAccessKeyId() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_credential)) {
            return "";
        }

        String accessKeyId = _credential.getAccessKeyId();
        return accessKeyId;
    }

    /**
     * <b>description</b> :
     * <p>Get accesskey secret by using credential</p>
     * @return accesskey secret
     */
    public String getAccessKeySecret() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_credential)) {
            return "";
        }

        String secret = _credential.getAccessKeySecret();
        return secret;
    }

    /**
     * <b>description</b> :
     * <p>Get security token by using credential</p>
     * @return security token
     */
    public String getSecurityToken() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_credential)) {
            return "";
        }

        String token = _credential.getSecurityToken();
        return token;
    }

    /**
     * <b>description</b> :
     * <p>Get bearer token by credential</p>
     * @return bearer token
     */
    public String getBearerToken() throws Exception {
        if (com.aliyun.teautil.Common.isUnset(_credential)) {
            return "";
        }

        String token = _credential.getBearerToken();
        return token;
    }

    /**
     * <b>description</b> :
     * <p>If inputValue is not null, return it or return defaultValue</p>
     * 
     * @param inputValue users input value
     * @param defaultValue default value
     * @return the final result
     */
    public static Object defaultAny(Object inputValue, Object defaultValue) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(inputValue)) {
            return defaultValue;
        }

        return inputValue;
    }
}
