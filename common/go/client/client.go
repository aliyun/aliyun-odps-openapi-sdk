// This file is auto-generated, don't edit it. Thanks.
package client

import (
  "io"
  mcutil  "github.com/aliyun/aliyun-odps-go-sdk/tea/utils"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  credential  "github.com/aliyun/credentials-go/credentials"
  "github.com/alibabacloud-go/tea/tea"
)

type GlobalParameters struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Queries map[string]*string `json:"queries,omitempty" xml:"queries,omitempty"`
}

func (s GlobalParameters) String() string {
  return tea.Prettify(s)
}

func (s GlobalParameters) GoString() string {
  return s.String()
}

func (s *GlobalParameters) SetHeaders(v map[string]*string) *GlobalParameters {
  s.Headers = v
  return s
}

func (s *GlobalParameters) SetQueries(v map[string]*string) *GlobalParameters {
  s.Queries = v
  return s
}

/**
 * Model for initing client
 */
type Config struct {
  // project
  Project *string `json:"project,omitempty" xml:"project,omitempty"`
  // accesskey id
  AccessKeyId *string `json:"accessKeyId,omitempty" xml:"accessKeyId,omitempty"`
  // accesskey secret
  AccessKeySecret *string `json:"accessKeySecret,omitempty" xml:"accessKeySecret,omitempty"`
  // security token
  SecurityToken *string `json:"securityToken,omitempty" xml:"securityToken,omitempty"`
  // bearer token
  BearerToken *string `json:"bearerToken,omitempty" xml:"bearerToken,omitempty"`
  // http protocol
  Protocol *string `json:"protocol,omitempty" xml:"protocol,omitempty"`
  // http method
  Method *string `json:"method,omitempty" xml:"method,omitempty"`
  // region id
  RegionId *string `json:"regionId,omitempty" xml:"regionId,omitempty"`
  // read timeout
  ReadTimeout *int `json:"readTimeout,omitempty" xml:"readTimeout,omitempty"`
  // connect timeout
  ConnectTimeout *int `json:"connectTimeout,omitempty" xml:"connectTimeout,omitempty"`
  // credential
  Credential credential.Credential `json:"credential,omitempty" xml:"credential,omitempty"`
  // endpoint
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
  // credential type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // user agent
  UserAgent *string `json:"userAgent,omitempty" xml:"userAgent,omitempty"`
  // suffix for endpoint
  Suffix *string `json:"suffix,omitempty" xml:"suffix,omitempty"`
  // Signature Version
  SignatureVersion *string `json:"signatureVersion,omitempty" xml:"signatureVersion,omitempty"`
  // Global Parameters
  GlobalParameters *GlobalParameters `json:"globalParameters,omitempty" xml:"globalParameters,omitempty"`
}

func (s Config) String() string {
  return tea.Prettify(s)
}

func (s Config) GoString() string {
  return s.String()
}

func (s *Config) SetProject(v string) *Config {
  s.Project = &v
  return s
}

func (s *Config) SetAccessKeyId(v string) *Config {
  s.AccessKeyId = &v
  return s
}

func (s *Config) SetAccessKeySecret(v string) *Config {
  s.AccessKeySecret = &v
  return s
}

func (s *Config) SetSecurityToken(v string) *Config {
  s.SecurityToken = &v
  return s
}

func (s *Config) SetBearerToken(v string) *Config {
  s.BearerToken = &v
  return s
}

func (s *Config) SetProtocol(v string) *Config {
  s.Protocol = &v
  return s
}

func (s *Config) SetMethod(v string) *Config {
  s.Method = &v
  return s
}

func (s *Config) SetRegionId(v string) *Config {
  s.RegionId = &v
  return s
}

func (s *Config) SetReadTimeout(v int) *Config {
  s.ReadTimeout = &v
  return s
}

func (s *Config) SetConnectTimeout(v int) *Config {
  s.ConnectTimeout = &v
  return s
}

func (s *Config) SetCredential(v credential.Credential) *Config {
  s.Credential = v
  return s
}

func (s *Config) SetEndpoint(v string) *Config {
  s.Endpoint = &v
  return s
}

func (s *Config) SetType(v string) *Config {
  s.Type = &v
  return s
}

func (s *Config) SetUserAgent(v string) *Config {
  s.UserAgent = &v
  return s
}

func (s *Config) SetSuffix(v string) *Config {
  s.Suffix = &v
  return s
}

func (s *Config) SetSignatureVersion(v string) *Config {
  s.SignatureVersion = &v
  return s
}

func (s *Config) SetGlobalParameters(v *GlobalParameters) *Config {
  s.GlobalParameters = v
  return s
}

type Params struct {
  Action *string `json:"action,omitempty" xml:"action,omitempty"`
  Version *string `json:"version,omitempty" xml:"version,omitempty"`
  Protocol *string `json:"protocol,omitempty" xml:"protocol,omitempty"`
  Pathname *string `json:"pathname,omitempty" xml:"pathname,omitempty" require:"true"`
  Method *string `json:"method,omitempty" xml:"method,omitempty" require:"true"`
  AuthType *string `json:"authType,omitempty" xml:"authType,omitempty"`
  BodyType *string `json:"bodyType,omitempty" xml:"bodyType,omitempty"`
  ReqBodyType *string `json:"reqBodyType,omitempty" xml:"reqBodyType,omitempty"`
  Style *string `json:"style,omitempty" xml:"style,omitempty"`
}

func (s Params) String() string {
  return tea.Prettify(s)
}

func (s Params) GoString() string {
  return s.String()
}

func (s *Params) SetAction(v string) *Params {
  s.Action = &v
  return s
}

func (s *Params) SetVersion(v string) *Params {
  s.Version = &v
  return s
}

func (s *Params) SetProtocol(v string) *Params {
  s.Protocol = &v
  return s
}

func (s *Params) SetPathname(v string) *Params {
  s.Pathname = &v
  return s
}

func (s *Params) SetMethod(v string) *Params {
  s.Method = &v
  return s
}

func (s *Params) SetAuthType(v string) *Params {
  s.AuthType = &v
  return s
}

func (s *Params) SetBodyType(v string) *Params {
  s.BodyType = &v
  return s
}

func (s *Params) SetReqBodyType(v string) *Params {
  s.ReqBodyType = &v
  return s
}

func (s *Params) SetStyle(v string) *Params {
  s.Style = &v
  return s
}

type OpenApiRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Query map[string]*string `json:"query,omitempty" xml:"query,omitempty"`
  Body interface{} `json:"body,omitempty" xml:"body,omitempty"`
  Stream io.Reader `json:"stream,omitempty" xml:"stream,omitempty"`
  HostMap map[string]*string `json:"hostMap,omitempty" xml:"hostMap,omitempty"`
  EndpointOverride *string `json:"endpointOverride,omitempty" xml:"endpointOverride,omitempty"`
}

func (s OpenApiRequest) String() string {
  return tea.Prettify(s)
}

func (s OpenApiRequest) GoString() string {
  return s.String()
}

func (s *OpenApiRequest) SetHeaders(v map[string]*string) *OpenApiRequest {
  s.Headers = v
  return s
}

func (s *OpenApiRequest) SetQuery(v map[string]*string) *OpenApiRequest {
  s.Query = v
  return s
}

func (s *OpenApiRequest) SetBody(v interface{}) *OpenApiRequest {
  s.Body = v
  return s
}

func (s *OpenApiRequest) SetStream(v io.Reader) *OpenApiRequest {
  s.Stream = v
  return s
}

func (s *OpenApiRequest) SetHostMap(v map[string]*string) *OpenApiRequest {
  s.HostMap = v
  return s
}

func (s *OpenApiRequest) SetEndpointOverride(v string) *OpenApiRequest {
  s.EndpointOverride = &v
  return s
}

type Client struct {
  Endpoint  *string
  Project  *string
  RegionId  *string
  Protocol  *string
  Method  *string
  UserAgent  *string
  ReadTimeout  *int
  ConnectTimeout  *int
  Credential  credential.Credential
  SignatureVersion  *string
  Headers  map[string]*string
  Suffix  *string
  GlobalParameters  *GlobalParameters
}

/**
 * Init client with Config
 * @param config config contains the necessary information to create a client
 */
func NewClient(config *Config)(*Client, error) {
  client := new(Client)
  err := client.Init(config)
  return client, err
}

func (client *Client)Init(config *Config)(_err error) {
  if tea.BoolValue(util.IsUnset(tea.ToMap(config))) {
    _err = tea.NewSDKError(map[string]interface{}{
      "code": "ParameterMissing",
      "message": "'config' can not be unset",
    })
    return _err
  }

  if !tea.BoolValue(util.Empty(config.AccessKeyId)) && !tea.BoolValue(util.Empty(config.AccessKeySecret)) {
    if !tea.BoolValue(util.Empty(config.SecurityToken)) {
      config.Type = tea.String("sts")
    } else {
      config.Type = tea.String("access_key")
    }

    credentialConfig := &credential.Config{
      AccessKeyId: config.AccessKeyId,
      Type: config.Type,
      AccessKeySecret: config.AccessKeySecret,
    }
    credentialConfig.SecurityToken = config.SecurityToken
    client.Credential, _err = credential.NewCredential(credentialConfig)
    if _err != nil {
      return _err
    }

  } else if !tea.BoolValue(util.Empty(config.BearerToken)) {
    cc := &credential.Config{
      Type: tea.String("bearer"),
      BearerToken: config.BearerToken,
    }
    client.Credential, _err = credential.NewCredential(cc)
    if _err != nil {
      return _err
    }

  } else if !tea.BoolValue(util.IsUnset(config.Credential)) {
    client.Credential = config.Credential
  }

  client.Project = config.Project
  client.Endpoint = config.Endpoint
  client.Protocol = config.Protocol
  client.Method = config.Method
  client.RegionId = config.RegionId
  client.UserAgent = config.UserAgent
  client.ReadTimeout = config.ReadTimeout
  client.ConnectTimeout = config.ConnectTimeout
  client.SignatureVersion = config.SignatureVersion
  client.GlobalParameters = config.GlobalParameters
  client.Suffix = config.Suffix
  return nil
}


/**
 * Encapsulate the request and invoke the network
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
func (client *Client) DoRequest(params *Params, request *OpenApiRequest, runtime *util.RuntimeOptions) (_result map[string]interface{}, _err error) {
  _err = tea.Validate(params)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(util.DefaultNumber(runtime.ReadTimeout, client.ReadTimeout)),
    "connectTimeout": tea.IntValue(util.DefaultNumber(runtime.ConnectTimeout, client.ConnectTimeout)),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := make(map[string]interface{})
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(map[string]interface{}, error){
      request_ := tea.NewRequest()
      request_.Protocol = util.DefaultString(client.Protocol, params.Protocol)
      request_.Method = params.Method
      if !tea.BoolValue(util.IsUnset(client.Suffix)) {
        request_.Pathname = tea.String("/" + tea.StringValue(client.Suffix) + tea.StringValue(params.Pathname))
      } else {
        request_.Pathname = params.Pathname
      }

      globalQueries := make(map[string]*string)
      globalHeaders := make(map[string]*string)
      if !tea.BoolValue(util.IsUnset(tea.ToMap(client.GlobalParameters))) {
        globalParams := client.GlobalParameters
        if !tea.BoolValue(util.IsUnset(globalParams.Queries)) {
          globalQueries = globalParams.Queries
        }

        if !tea.BoolValue(util.IsUnset(globalParams.Headers)) {
          globalHeaders = globalParams.Headers
        }

      }

      extendsHeaders := make(map[string]*string)
      extendsQueries := make(map[string]*string)
      if !tea.BoolValue(util.IsUnset(tea.ToMap(runtime.ExtendsParameters))) {
        extendsParameters := runtime.ExtendsParameters
        if !tea.BoolValue(util.IsUnset(extendsParameters.Headers)) {
          extendsHeaders = extendsParameters.Headers
        }

        if !tea.BoolValue(util.IsUnset(extendsParameters.Queries)) {
          extendsQueries = extendsParameters.Queries
        }

      }

      request_.Query = tea.Merge(map[string]*string{
        "curr_project": client.Project,
        },globalQueries,
        extendsQueries,
        request.Query)
      // endpoint is setted in product client
      request_.Headers = tea.Merge(map[string]*string{
        "host": client.Endpoint,
        "user-agent": client.GetUserAgent(),
        "x-odps-user-agent": client.GetUserAgent(),
        "Date": mcutil.GetApiTimestamp(),
        },globalHeaders,
        extendsHeaders,
        request.Headers)
      if !tea.BoolValue(util.IsUnset(request.Stream)) {
        tmp, _err := util.ReadAsBytes(request.Stream)
        if _err != nil {
          return _result, _err
        }

        request_.Body = tea.ToReader(tmp)
      }

      if !tea.BoolValue(util.IsUnset(request.Body)) {
        jsonObj := util.ToJSONString(request.Body)
        request_.Body = tea.ToReader(jsonObj)
        request_.Headers["content-type"] = tea.String("application/json; charset=utf-8")
      }

      canonicalString := mcutil.BuildCanonicalString(params.Method, params.Pathname, request_.Query, request_.Headers)
      if !tea.BoolValue(util.EqualString(params.AuthType, tea.String("Anonymous"))) {
        if tea.BoolValue(util.IsUnset(client.Credential)) {
          _err = tea.NewSDKError(map[string]interface{}{
            "code": "InvalidCredentials",
            "message": "Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.",
          })
          return _result, _err
        }

        credentialModel, _err := client.Credential.GetCredential()
        if _err != nil {
          return _result, _err
        }

        authType := credentialModel.Type
        if tea.BoolValue(util.EqualString(authType, tea.String("bearer"))) {
          bearerToken := credentialModel.BearerToken
          request_.Headers["x-odps-bearer-token"] = bearerToken
        } else {
          accessKeyId := credentialModel.AccessKeyId
          accessKeySecret := credentialModel.AccessKeySecret
          securityToken := credentialModel.SecurityToken
          request_.Headers["Authorization"] = mcutil.GetSignature(canonicalString, accessKeyId, accessKeySecret)
          if !tea.BoolValue(util.Empty(securityToken)) {
            request_.Headers["authorization-sts-token"] = securityToken
          }

        }

      }

      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(204))) {
        _result = make(map[string]interface{})
        _err = tea.Convert(map[string]map[string]*string{
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if tea.BoolValue(util.Is4xx(response_.StatusCode)) || tea.BoolValue(util.Is5xx(response_.StatusCode)) {
        err := map[string]interface{}{}
        _, tryErr := func()(_r map[string]interface{}, _e error) {
          defer func() {
            if r := tea.Recover(recover()); r != nil {
              _e = r
            }
          }()
          _res, _err := util.ReadAsJSON(response_.Body)
          if _err != nil {
            return _result, _err
          }

          err, _err = util.AssertAsMap(_res)
          if _err != nil {
            return _result, _err
          }


          return nil, nil
        }()

        if tryErr != nil {
          var error = &tea.SDKError{}
          if _t, ok := tryErr.(*tea.SDKError); ok {
            error = _t
          } else {
            error.Message = tea.String(tryErr.Error())
          }
          err["Code"] = tea.String("Unknown")
          err["Message"], _err = util.ReadAsString(response_.Body)
          if _err != nil {
            return _result, _err
          }

        }
        requestId := mcutil.ToString(DefaultAny(response_.Headers["x-odps-request-id"], response_.Headers["X-Odps-Request-Id"]))
        err["statusCode"] = response_.StatusCode
        _err = tea.NewSDKError(map[string]interface{}{
          "code": tea.ToString(DefaultAny(err["Code"], err["code"])),
          "message": "code: " + tea.ToString(tea.IntValue(response_.StatusCode)) + ", " + tea.ToString(DefaultAny(err["Message"], err["message"])) + " request id: " + tea.StringValue(requestId),
          "data": err,
          "description": tea.ToString(DefaultAny(err["Description"], err["description"])),
          "accessDeniedDetail": DefaultAny(err["AccessDeniedDetail"], err["accessDeniedDetail"]),
        })
        return _result, _err
      }

      if tea.BoolValue(util.EqualString(params.BodyType, tea.String("binary"))) {
        resp := map[string]interface{}{
          "body": response_.Body,
          "headers": response_.Headers,
          "statusCode": tea.IntValue(response_.StatusCode),
        }
        _result = resp
        return _result , _err
      } else if tea.BoolValue(util.EqualString(params.BodyType, tea.String("byte"))) {
        byt, _err := util.ReadAsBytes(response_.Body)
        if _err != nil {
          return _result, _err
        }

        _result = make(map[string]interface{})
        _err = tea.Convert(map[string]interface{}{
          "body": byt,
          "headers": response_.Headers,
          "statusCode": tea.IntValue(response_.StatusCode),
        }, &_result)
        return _result, _err
      } else if tea.BoolValue(util.EqualString(params.BodyType, tea.String("string"))) {
        str, _err := util.ReadAsString(response_.Body)
        if _err != nil {
          return _result, _err
        }

        _result = make(map[string]interface{})
        _err = tea.Convert(map[string]interface{}{
          "body": tea.StringValue(str),
          "headers": response_.Headers,
          "statusCode": tea.IntValue(response_.StatusCode),
        }, &_result)
        return _result, _err
      } else if tea.BoolValue(util.EqualString(params.BodyType, tea.String("json"))) {
        obj, _err := util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        res, _err := util.AssertAsMap(obj)
        if _err != nil {
          return _result, _err
        }

        _result = res
        return _result , _err
      } else if tea.BoolValue(util.EqualString(params.BodyType, tea.String("array"))) {
        arr, _err := util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        _result = make(map[string]interface{})
        _err = tea.Convert(map[string]interface{}{
          "body": arr,
          "headers": response_.Headers,
          "statusCode": tea.IntValue(response_.StatusCode),
        }, &_result)
        return _result, _err
      } else {
        anything, _err := util.ReadAsString(response_.Body)
        if _err != nil {
          return _result, _err
        }

        _result = make(map[string]interface{})
        _err = tea.Convert(map[string]interface{}{
          "body": tea.StringValue(anything),
          "headers": response_.Headers,
          "statusCode": tea.IntValue(response_.StatusCode),
        }, &_result)
        return _result, _err
      }

    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}


func (client *Client) RequestWithModel (model interface{}, method *string, path *string, runtime *util.RuntimeOptions) (_result map[string]interface{}, _err error) {
  _err = util.ValidateModel(model)
  if _err != nil {
    return _result, _err
  }
  req := &OpenApiRequest{
    Body: util.ToMap(model),
  }
  openapiParams := &Params{
    Pathname: path,
    Method: method,
    BodyType: tea.String("json"),
  }
  _result = make(map[string]interface{})
  _body, _err := client.CallApi(openapiParams, req, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

func (client *Client) RequestWithoutModel (model interface{}, method *string, path *string, runtime *util.RuntimeOptions) (_result map[string]interface{}, _err error) {
  _err = util.ValidateModel(model)
  if _err != nil {
    return _result, _err
  }
  req := &OpenApiRequest{
    Body: util.ToMap(model),
  }
  openapiParams := &Params{
    Pathname: path,
    Method: method,
    BodyType: tea.String("none"),
  }
  _result = make(map[string]interface{})
  _body, _err := client.CallApi(openapiParams, req, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

func (client *Client) CallApi (params *Params, request *OpenApiRequest, runtime *util.RuntimeOptions) (_result map[string]interface{}, _err error) {
  if tea.BoolValue(util.IsUnset(tea.ToMap(params))) {
    _err = tea.NewSDKError(map[string]interface{}{
      "code": "ParameterMissing",
      "message": "'params' can not be unset",
    })
    return _result, _err
  }

  _result = make(map[string]interface{})
  _body, _err := client.DoRequest(params, request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * Get user agent
 * @return user agent
 */
func (client *Client) GetUserAgent () (_result *string) {
  userAgent := util.GetUserAgent(client.UserAgent)
  _result = userAgent
  return _result
}

/**
 * Get accesskey id by using credential
 * @return accesskey id
 */
func (client *Client) GetAccessKeyId () (_result *string, _err error) {
  if tea.BoolValue(util.IsUnset(client.Credential)) {
    _result = tea.String("")
    return _result, _err
  }

  accessKeyId, _err := client.Credential.GetAccessKeyId()
  if _err != nil {
    return _result, _err
  }

  _result = accessKeyId
  return _result , _err
}

/**
 * Get accesskey secret by using credential
 * @return accesskey secret
 */
func (client *Client) GetAccessKeySecret () (_result *string, _err error) {
  if tea.BoolValue(util.IsUnset(client.Credential)) {
    _result = tea.String("")
    return _result, _err
  }

  secret, _err := client.Credential.GetAccessKeySecret()
  if _err != nil {
    return _result, _err
  }

  _result = secret
  return _result , _err
}

/**
 * Get security token by using credential
 * @return security token
 */
func (client *Client) GetSecurityToken () (_result *string, _err error) {
  if tea.BoolValue(util.IsUnset(client.Credential)) {
    _result = tea.String("")
    return _result, _err
  }

  token, _err := client.Credential.GetSecurityToken()
  if _err != nil {
    return _result, _err
  }

  _result = token
  return _result , _err
}

/**
 * Get bearer token by credential
 * @return bearer token
 */
func (client *Client) GetBearerToken () (_result *string, _err error) {
  if tea.BoolValue(util.IsUnset(client.Credential)) {
    _result = tea.String("")
    return _result, _err
  }

  token := client.Credential.GetBearerToken()
  _result = token
  return _result , _err
}

/**
 * If inputValue is not null, return it or return defaultValue
 * @param inputValue  users input value
 * @param defaultValue default value
 * @return the final result
 */
func DefaultAny (inputValue interface{}, defaultValue interface{}) (_result interface{}) {
  if tea.BoolValue(util.IsUnset(inputValue)) {
    _result = defaultValue
    return _result
  }

  _result = inputValue
  return _result
}

