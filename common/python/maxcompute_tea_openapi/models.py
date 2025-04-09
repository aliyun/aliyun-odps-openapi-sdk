# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, BinaryIO

from alibabacloud_credentials.client import Client as CredentialClient


class GlobalParameters(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        queries: Dict[str, str] = None,
    ):
        self.headers = headers
        self.queries = queries

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.queries is not None:
            result['queries'] = self.queries
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('queries') is not None:
            self.queries = m.get('queries')
        return self


class Config(TeaModel):
    """
    Model for initing client
    """
    def __init__(
        self,
        project: str = None,
        access_key_id: str = None,
        access_key_secret: str = None,
        security_token: str = None,
        bearer_token: str = None,
        protocol: str = None,
        method: str = None,
        region_id: str = None,
        read_timeout: int = None,
        connect_timeout: int = None,
        credential: CredentialClient = None,
        endpoint: str = None,
        type: str = None,
        user_agent: str = None,
        suffix: str = None,
        signature_version: str = None,
        global_parameters: GlobalParameters = None,
    ):
        # project
        self.project = project
        # accesskey id
        self.access_key_id = access_key_id
        # accesskey secret
        self.access_key_secret = access_key_secret
        # security token
        self.security_token = security_token
        # bearer token
        self.bearer_token = bearer_token
        # http protocol
        self.protocol = protocol
        # http method
        self.method = method
        # region id
        self.region_id = region_id
        # read timeout
        self.read_timeout = read_timeout
        # connect timeout
        self.connect_timeout = connect_timeout
        # credential
        self.credential = credential
        # endpoint
        self.endpoint = endpoint
        # credential type
        self.type = type
        # user agent
        self.user_agent = user_agent
        # suffix for endpoint
        self.suffix = suffix
        # Signature Version
        self.signature_version = signature_version
        # Global Parameters
        self.global_parameters = global_parameters

    def validate(self):
        if self.global_parameters:
            self.global_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        if self.bearer_token is not None:
            result['bearerToken'] = self.bearer_token
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.method is not None:
            result['method'] = self.method
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.read_timeout is not None:
            result['readTimeout'] = self.read_timeout
        if self.connect_timeout is not None:
            result['connectTimeout'] = self.connect_timeout
        if self.credential is not None:
            result['credential'] = self.credential
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.type is not None:
            result['type'] = self.type
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.signature_version is not None:
            result['signatureVersion'] = self.signature_version
        if self.global_parameters is not None:
            result['globalParameters'] = self.global_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        if m.get('bearerToken') is not None:
            self.bearer_token = m.get('bearerToken')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('readTimeout') is not None:
            self.read_timeout = m.get('readTimeout')
        if m.get('connectTimeout') is not None:
            self.connect_timeout = m.get('connectTimeout')
        if m.get('credential') is not None:
            self.credential = m.get('credential')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('signatureVersion') is not None:
            self.signature_version = m.get('signatureVersion')
        if m.get('globalParameters') is not None:
            temp_model = GlobalParameters()
            self.global_parameters = temp_model.from_map(m['globalParameters'])
        return self


class Params(TeaModel):
    def __init__(
        self,
        action: str = None,
        version: str = None,
        protocol: str = None,
        pathname: str = None,
        method: str = None,
        auth_type: str = None,
        body_type: str = None,
        req_body_type: str = None,
        style: str = None,
    ):
        self.action = action
        self.version = version
        self.protocol = protocol
        self.pathname = pathname
        self.method = method
        self.auth_type = auth_type
        self.body_type = body_type
        self.req_body_type = req_body_type
        self.style = style

    def validate(self):
        self.validate_required(self.pathname, 'pathname')
        self.validate_required(self.method, 'method')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.version is not None:
            result['version'] = self.version
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.pathname is not None:
            result['pathname'] = self.pathname
        if self.method is not None:
            result['method'] = self.method
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.body_type is not None:
            result['bodyType'] = self.body_type
        if self.req_body_type is not None:
            result['reqBodyType'] = self.req_body_type
        if self.style is not None:
            result['style'] = self.style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('pathname') is not None:
            self.pathname = m.get('pathname')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('bodyType') is not None:
            self.body_type = m.get('bodyType')
        if m.get('reqBodyType') is not None:
            self.req_body_type = m.get('reqBodyType')
        if m.get('style') is not None:
            self.style = m.get('style')
        return self


class OpenApiRequest(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        query: Dict[str, str] = None,
        body: Any = None,
        stream: BinaryIO = None,
        host_map: Dict[str, str] = None,
        endpoint_override: str = None,
    ):
        self.headers = headers
        self.query = query
        self.body = body
        self.stream = stream
        self.host_map = host_map
        self.endpoint_override = endpoint_override

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.query is not None:
            result['query'] = self.query
        if self.body is not None:
            result['body'] = self.body
        if self.stream is not None:
            result['stream'] = self.stream
        if self.host_map is not None:
            result['hostMap'] = self.host_map
        if self.endpoint_override is not None:
            result['endpointOverride'] = self.endpoint_override
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('hostMap') is not None:
            self.host_map = m.get('hostMap')
        if m.get('endpointOverride') is not None:
            self.endpoint_override = m.get('endpointOverride')
        return self


