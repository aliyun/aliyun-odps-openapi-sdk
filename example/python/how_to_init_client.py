"""
Examples of initializing the Catalog API client.

error 'invalid character '<' looking for beginning of value' may because of wrong endpoint or wrong proxy configured
endpoint should be like 'catalogapi.ap-southeast-5.maxcompute.aliyun.com'
"""
from maxcompute_tea_openapi import models as open_api_models
from pyodps_catalog.client import Client


def way_1():
    """Initialize with catalog endpoint directly."""
    endpoint = ""
    access_key_id = ""
    access_key_secret = ""

    config = open_api_models.Config(
        endpoint=endpoint,
        access_key_id=access_key_id,
        access_key_secret=access_key_secret,
    )
    client = Client(config)
    print(client._endpoint)


def way_2():
    """
    Initialize with ODPS endpoint only.
    The catalog API endpoint is resolved lazily on the first request via the routing API.
    odps_endpoint should be like 'service.cn-shanghai.maxcompute.aliyun.com'
    """
    odps_endpoint = ""
    access_key_id = ""
    access_key_secret = ""

    config = open_api_models.Config(
        odps_endpoint=odps_endpoint,
        protocol="http",
        access_key_id=access_key_id,
        access_key_secret=access_key_secret,
    )
    client = Client(config)
    # Endpoint is empty until the first API call triggers routing resolution.
    print(client._endpoint)


def way_3():
    """Initialize with STS token for temporary credentials."""
    endpoint = ""
    access_key_id = ""
    access_key_secret = ""
    security_token = ""

    config = open_api_models.Config(
        endpoint=endpoint,
        access_key_id=access_key_id,
        access_key_secret=access_key_secret,
        security_token=security_token,
    )
    client = Client(config)
    print(client._endpoint)
