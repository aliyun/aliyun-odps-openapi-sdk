# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.exceptions import TeaException, UnretryableException
from Tea.request import TeaRequest
from Tea.core import TeaCore
from Tea.model import TeaModel
from typing import Dict, Any

from alibabacloud_credentials.client import Client as CredentialClient
from maxcompute_tea_openapi import models as openapi_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_credentials import models as credential_models
from alibabacloud_tea_util import models as util_models
from maxcompute_tea_util.client import Client as McUtilClient


class Client:
    _endpoint: str = None
    _project: str = None
    _region_id: str = None
    _protocol: str = None
    _method: str = None
    _user_agent: str = None
    _read_timeout: int = None
    _connect_timeout: int = None
    _credential: CredentialClient = None
    _signature_version: str = None
    _headers: Dict[str, str] = None
    _suffix: str = None
    _global_parameters: openapi_models.GlobalParameters = None

    def __init__(
        self, 
        config: openapi_models.Config,
    ):
        """
        Init client with Config
        @param config: config contains the necessary information to create a client
        """
        if UtilClient.is_unset(config):
            raise TeaException({
                'code': 'ParameterMissing',
                'message': "'config' can not be unset"
            })
        if not UtilClient.empty(config.access_key_id) and not UtilClient.empty(config.access_key_secret):
            if not UtilClient.empty(config.security_token):
                config.type = 'sts'
            else:
                config.type = 'access_key'
            credential_config = credential_models.Config(
                access_key_id=config.access_key_id,
                type=config.type,
                access_key_secret=config.access_key_secret
            )
            credential_config.security_token = config.security_token
            self._credential = CredentialClient(credential_config)
        elif not UtilClient.empty(config.bearer_token):
            cc = credential_models.Config(
                type='bearer',
                bearer_token=config.bearer_token
            )
            self._credential = CredentialClient(cc)
        elif not UtilClient.is_unset(config.credential):
            self._credential = config.credential
        self._project = config.project
        self._endpoint = config.endpoint
        self._protocol = config.protocol
        self._method = config.method
        self._region_id = config.region_id
        self._user_agent = config.user_agent
        self._read_timeout = config.read_timeout
        self._connect_timeout = config.connect_timeout
        self._signature_version = config.signature_version
        self._global_parameters = config.global_parameters
        self._suffix = config.suffix

    def do_request(
        self,
        params: openapi_models.Params,
        request: openapi_models.OpenApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        """
        Encapsulate the request and invoke the network
        @param action: api name
        @param version: product version
        @param protocol: http or https
        @param method: e.g. GET
        @param auth_type: authorization type e.g. AK
        @param body_type: response body type e.g. String
        @param request: object of OpenApiRequest
        @param runtime: which controls some details of call api, such as retry times
        @return: the response
        """
        params.validate()
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': UtilClient.default_number(runtime.read_timeout, self._read_timeout),
            'connectTimeout': UtilClient.default_number(runtime.connect_timeout, self._connect_timeout),
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.protocol = UtilClient.default_string(self._protocol, params.protocol)
                _request.method = params.method
                if not UtilClient.is_unset(self._suffix):
                    _request.pathname = f'/{self._suffix}{params.pathname}'
                else:
                    _request.pathname = params.pathname
                global_queries = {}
                global_headers = {}
                if not UtilClient.is_unset(self._global_parameters):
                    global_params = self._global_parameters
                    if not UtilClient.is_unset(global_params.queries):
                        global_queries = global_params.queries
                    if not UtilClient.is_unset(global_params.headers):
                        global_headers = global_params.headers
                extends_headers = {}
                extends_queries = {}
                if not UtilClient.is_unset(runtime.extends_parameters):
                    extends_parameters = runtime.extends_parameters
                    if not UtilClient.is_unset(extends_parameters.headers):
                        extends_headers = extends_parameters.headers
                    if not UtilClient.is_unset(extends_parameters.queries):
                        extends_queries = extends_parameters.queries
                _request.query = TeaCore.merge(global_queries,
                    extends_queries,
                    request.query)
                # endpoint is setted in product client
                _request.headers = TeaCore.merge({
                    'host': self._endpoint,
                    'user-agent': self.get_user_agent(),
                    'x-odps-user-agent': self.get_user_agent(),
                    'Date': McUtilClient.get_api_timestamp()
                }, global_headers,
                    extends_headers,
                    request.headers)
                if not UtilClient.is_unset(request.stream):
                    tmp = UtilClient.read_as_bytes(request.stream)
                    _request.body = tmp
                if not UtilClient.is_unset(request.body):
                    json_obj = UtilClient.to_jsonstring(request.body)
                    _request.body = json_obj
                    _request.headers['content-type'] = 'application/json; charset=utf-8'
                canonical_string = McUtilClient.build_canonical_string(params.method, params.pathname, _request.query, _request.headers)
                if not UtilClient.equal_string(params.auth_type, 'Anonymous'):
                    if UtilClient.is_unset(self._credential):
                        raise TeaException({
                            'code': f'InvalidCredentials',
                            'message': f'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
                        })
                    credential_model = self._credential.get_credential()
                    auth_type = credential_model.type
                    if UtilClient.equal_string(auth_type, 'bearer'):
                        bearer_token = credential_model.bearer_token
                        _request.headers['x-odps-bearer-token'] = bearer_token
                    else:
                        access_key_id = credential_model.access_key_id
                        access_key_secret = credential_model.access_key_secret
                        security_token = credential_model.security_token
                        _request.headers['Authorization'] = McUtilClient.get_signature(canonical_string, access_key_id, access_key_secret)
                        if not UtilClient.empty(security_token):
                            _request.headers['authorization-sts-token'] = security_token
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                if UtilClient.equal_number(_response.status_code, 204):
                    return {
                        'headers': _response.headers
                    }
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    err = {}
                    response_body = UtilClient.read_as_string(_response.body)
                    try:
                        _res = UtilClient.parse_json(response_body)
                        err = UtilClient.assert_as_map(_res)
                    except Exception as error:
                        err = {}
                        err['Code'] = 'Unknown'
                        err['Message'] = response_body
                    request_id = McUtilClient.to_string(self.default_any(_response.headers.get('x-odps-request-id'), _response.headers.get('X-Odps-Request-Id')))
                    err['statusCode'] = _response.status_code
                    raise TeaException({
                        'code': f"{self.default_any(err.get('Code'), err.get('code'))}",
                        'message': f"code: {_response.status_code}, {self.default_any(err.get('Message'), err.get('message'))} request id: {request_id}",
                        'data': err,
                        'description': f"{self.default_any(err.get('Description'), err.get('description'))}",
                        'accessDeniedDetail': self.default_any(err.get('AccessDeniedDetail'), err.get('accessDeniedDetail'))
                    })
                if UtilClient.equal_string(params.body_type, 'binary'):
                    resp = {
                        'body': _response.body,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
                    return resp
                elif UtilClient.equal_string(params.body_type, 'byte'):
                    byt = UtilClient.read_as_bytes(_response.body)
                    return {
                        'body': byt,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
                elif UtilClient.equal_string(params.body_type, 'string'):
                    str = UtilClient.read_as_string(_response.body)
                    return {
                        'body': str,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
                elif UtilClient.equal_string(params.body_type, 'json'):
                    obj = UtilClient.read_as_json(_response.body)
                    res = UtilClient.assert_as_map(obj)
                    return res
                elif UtilClient.equal_string(params.body_type, 'array'):
                    arr = UtilClient.read_as_json(_response.body)
                    return {
                        'body': arr,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
                else:
                    anything = UtilClient.read_as_string(_response.body)
                    return {
                        'body': anything,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def do_request_async(
        self,
        params: openapi_models.Params,
        request: openapi_models.OpenApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        """
        Encapsulate the request and invoke the network
        @param action: api name
        @param version: product version
        @param protocol: http or https
        @param method: e.g. GET
        @param auth_type: authorization type e.g. AK
        @param body_type: response body type e.g. String
        @param request: object of OpenApiRequest
        @param runtime: which controls some details of call api, such as retry times
        @return: the response
        """
        params.validate()
        request.validate()
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': UtilClient.default_number(runtime.read_timeout, self._read_timeout),
            'connectTimeout': UtilClient.default_number(runtime.connect_timeout, self._connect_timeout),
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.protocol = UtilClient.default_string(self._protocol, params.protocol)
                _request.method = params.method
                if not UtilClient.is_unset(self._suffix):
                    _request.pathname = f'/{self._suffix}{params.pathname}'
                else:
                    _request.pathname = params.pathname
                global_queries = {}
                global_headers = {}
                if not UtilClient.is_unset(self._global_parameters):
                    global_params = self._global_parameters
                    if not UtilClient.is_unset(global_params.queries):
                        global_queries = global_params.queries
                    if not UtilClient.is_unset(global_params.headers):
                        global_headers = global_params.headers
                extends_headers = {}
                extends_queries = {}
                if not UtilClient.is_unset(runtime.extends_parameters):
                    extends_parameters = runtime.extends_parameters
                    if not UtilClient.is_unset(extends_parameters.headers):
                        extends_headers = extends_parameters.headers
                    if not UtilClient.is_unset(extends_parameters.queries):
                        extends_queries = extends_parameters.queries
                _request.query = TeaCore.merge(global_queries,
                    extends_queries,
                    request.query)
                # endpoint is setted in product client
                _request.headers = TeaCore.merge({
                    'host': self._endpoint,
                    'user-agent': self.get_user_agent(),
                    'x-odps-user-agent': self.get_user_agent(),
                    'Date': McUtilClient.get_api_timestamp()
                }, global_headers,
                    extends_headers,
                    request.headers)
                if not UtilClient.is_unset(request.stream):
                    tmp = await UtilClient.read_as_bytes_async(request.stream)
                    _request.body = tmp
                if not UtilClient.is_unset(request.body):
                    json_obj = UtilClient.to_jsonstring(request.body)
                    _request.body = json_obj
                    _request.headers['content-type'] = 'application/json; charset=utf-8'
                canonical_string = McUtilClient.build_canonical_string(params.method, params.pathname, _request.query, _request.headers)
                if not UtilClient.equal_string(params.auth_type, 'Anonymous'):
                    if UtilClient.is_unset(self._credential):
                        raise TeaException({
                            'code': f'InvalidCredentials',
                            'message': f'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
                        })
                    credential_model = await self._credential.get_credential_async()
                    auth_type = credential_model.type
                    if UtilClient.equal_string(auth_type, 'bearer'):
                        bearer_token = credential_model.bearer_token
                        _request.headers['x-odps-bearer-token'] = bearer_token
                    else:
                        access_key_id = credential_model.access_key_id
                        access_key_secret = credential_model.access_key_secret
                        security_token = credential_model.security_token
                        _request.headers['Authorization'] = McUtilClient.get_signature(canonical_string, access_key_id, access_key_secret)
                        if not UtilClient.empty(security_token):
                            _request.headers['authorization-sts-token'] = security_token
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                if UtilClient.equal_number(_response.status_code, 204):
                    return {
                        'headers': _response.headers
                    }
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    err = {}
                    response_body = await UtilClient.read_as_string_async(_response.body)
                    try:
                        _res = UtilClient.parse_json(response_body)
                        err = UtilClient.assert_as_map(_res)
                    except Exception as error:
                        err = {}
                        err['Code'] = 'Unknown'
                        err['Message'] = response_body
                    request_id = McUtilClient.to_string(self.default_any(_response.headers.get('x-odps-request-id'), _response.headers.get('X-Odps-Request-Id')))
                    err['statusCode'] = _response.status_code
                    raise TeaException({
                        'code': f"{self.default_any(err.get('Code'), err.get('code'))}",
                        'message': f"code: {_response.status_code}, {self.default_any(err.get('Message'), err.get('message'))} request id: {request_id}",
                        'data': err,
                        'description': f"{self.default_any(err.get('Description'), err.get('description'))}",
                        'accessDeniedDetail': self.default_any(err.get('AccessDeniedDetail'), err.get('accessDeniedDetail'))
                    })
                if UtilClient.equal_string(params.body_type, 'binary'):
                    resp = {
                        'body': _response.body,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
                    return resp
                elif UtilClient.equal_string(params.body_type, 'byte'):
                    byt = await UtilClient.read_as_bytes_async(_response.body)
                    return {
                        'body': byt,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
                elif UtilClient.equal_string(params.body_type, 'string'):
                    str = await UtilClient.read_as_string_async(_response.body)
                    return {
                        'body': str,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
                elif UtilClient.equal_string(params.body_type, 'json'):
                    obj = await UtilClient.read_as_json_async(_response.body)
                    res = UtilClient.assert_as_map(obj)
                    return res
                elif UtilClient.equal_string(params.body_type, 'array'):
                    arr = await UtilClient.read_as_json_async(_response.body)
                    return {
                        'body': arr,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
                else:
                    anything = await UtilClient.read_as_string_async(_response.body)
                    return {
                        'body': anything,
                        'headers': _response.headers,
                        'statusCode': _response.status_code
                    }
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def request_with_model(
        self,
        model: TeaModel,
        method: str,
        path: str,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        UtilClient.validate_model(model)
        req = openapi_models.OpenApiRequest(
            body=UtilClient.to_map(model)
        )
        openapi_params = openapi_models.Params(
            pathname=path,
            method=method,
            body_type='json'
        )
        return self.call_api(openapi_params, req, runtime)

    async def request_with_model_async(
        self,
        model: TeaModel,
        method: str,
        path: str,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        UtilClient.validate_model(model)
        req = openapi_models.OpenApiRequest(
            body=UtilClient.to_map(model)
        )
        openapi_params = openapi_models.Params(
            pathname=path,
            method=method,
            body_type='json'
        )
        return await self.call_api_async(openapi_params, req, runtime)

    def request_without_model(
        self,
        model: TeaModel,
        method: str,
        path: str,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        UtilClient.validate_model(model)
        req = openapi_models.OpenApiRequest(
            body=UtilClient.to_map(model)
        )
        openapi_params = openapi_models.Params(
            pathname=path,
            method=method,
            body_type='none'
        )
        return self.call_api(openapi_params, req, runtime)

    async def request_without_model_async(
        self,
        model: TeaModel,
        method: str,
        path: str,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        UtilClient.validate_model(model)
        req = openapi_models.OpenApiRequest(
            body=UtilClient.to_map(model)
        )
        openapi_params = openapi_models.Params(
            pathname=path,
            method=method,
            body_type='none'
        )
        return await self.call_api_async(openapi_params, req, runtime)

    def call_api(
        self,
        params: openapi_models.Params,
        request: openapi_models.OpenApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        if UtilClient.is_unset(params):
            raise TeaException({
                'code': 'ParameterMissing',
                'message': "'params' can not be unset"
            })
        return self.do_request(params, request, runtime)

    async def call_api_async(
        self,
        params: openapi_models.Params,
        request: openapi_models.OpenApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        if UtilClient.is_unset(params):
            raise TeaException({
                'code': 'ParameterMissing',
                'message': "'params' can not be unset"
            })
        return await self.do_request_async(params, request, runtime)

    def get_user_agent(self) -> str:
        """
        Get user agent
        @return: user agent
        """
        user_agent = UtilClient.get_user_agent(self._user_agent)
        return user_agent

    def get_access_key_id(self) -> str:
        """
        Get accesskey id by using credential
        @return: accesskey id
        """
        if UtilClient.is_unset(self._credential):
            return ''
        access_key_id = self._credential.get_access_key_id()
        return access_key_id

    async def get_access_key_id_async(self) -> str:
        """
        Get accesskey id by using credential
        @return: accesskey id
        """
        if UtilClient.is_unset(self._credential):
            return ''
        access_key_id = await self._credential.get_access_key_id_async()
        return access_key_id

    def get_access_key_secret(self) -> str:
        """
        Get accesskey secret by using credential
        @return: accesskey secret
        """
        if UtilClient.is_unset(self._credential):
            return ''
        secret = self._credential.get_access_key_secret()
        return secret

    async def get_access_key_secret_async(self) -> str:
        """
        Get accesskey secret by using credential
        @return: accesskey secret
        """
        if UtilClient.is_unset(self._credential):
            return ''
        secret = await self._credential.get_access_key_secret_async()
        return secret

    def get_security_token(self) -> str:
        """
        Get security token by using credential
        @return: security token
        """
        if UtilClient.is_unset(self._credential):
            return ''
        token = self._credential.get_security_token()
        return token

    async def get_security_token_async(self) -> str:
        """
        Get security token by using credential
        @return: security token
        """
        if UtilClient.is_unset(self._credential):
            return ''
        token = await self._credential.get_security_token_async()
        return token

    def get_bearer_token(self) -> str:
        """
        Get bearer token by credential
        @return: bearer token
        """
        if UtilClient.is_unset(self._credential):
            return ''
        token = self._credential.get_bearer_token()
        return token

    async def get_bearer_token_async(self) -> str:
        """
        Get bearer token by credential
        @return: bearer token
        """
        if UtilClient.is_unset(self._credential):
            return ''
        token = self._credential.get_bearer_token()
        return token

    @staticmethod
    def default_any(
        input_value: Any,
        default_value: Any,
    ) -> Any:
        """
        If inputValue is not null, return it or return defaultValue
        @param input_value:  users input value
        @param default_value: default value
        @return: the final result
        """
        if UtilClient.is_unset(input_value):
            return default_value
        return input_value
