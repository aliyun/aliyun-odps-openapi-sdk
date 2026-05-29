"""
Demonstrates initializing the catalog client with only the ODPS endpoint.
The catalog endpoint is resolved lazily via the routing API on first request.

Reads credentials and ODPS endpoint from environment variables:
  ALIBABA_CLOUD_ACCESS_KEY_ID
  ALIBABA_CLOUD_ACCESS_KEY_SECRET
  odps_endpoint    (e.g. http://service.cn-shanghai.maxcompute.aliyun.com/api)
  PROJECT
"""
import os
from urllib.parse import urlparse

from maxcompute_tea_openapi import models as open_api_models
from pyodps_catalog import models as catalog_api_models
from pyodps_catalog.client import Client


def test_lazy_endpoint_resolution():
    ak_id = os.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")
    ak_secret = os.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
    raw_odps = os.getenv("odps_endpoint")
    project_id = os.getenv("PROJECT")
    table_name = os.getenv("CATALOG_TABLE_NAME") or "test_table"

    if not all([ak_id, ak_secret, raw_odps, project_id]):
        print("SKIP: set ALIBABA_CLOUD_ACCESS_KEY_ID / ALIBABA_CLOUD_ACCESS_KEY_SECRET / odps_endpoint / PROJECT")
        return

    normalized = raw_odps if "://" in raw_odps else f"http://{raw_odps}"
    parsed = urlparse(normalized)
    protocol = parsed.scheme
    host = parsed.hostname
    print(f"odps endpoint: protocol={protocol} host={host}")

    config = open_api_models.Config(
        odps_endpoint=host,
        protocol=protocol,
        access_key_id=ak_id,
        access_key_secret=ak_secret,
    )
    client = Client(config)

    assert not client._endpoint, "endpoint should be empty before first call"
    print(f'endpoint before call: "{client._endpoint or ""}"')

    list_resp = client.list_projects(1, None)
    assert list_resp is not None, "list_projects should succeed after lazy endpoint resolution"

    assert client._endpoint, "endpoint should be populated after first call"
    print(f'endpoint after call:  "{client._endpoint}"')

    try:
        table = catalog_api_models.Table(project_id=project_id, table_name=table_name)
        got = client.get_table(table)
        print(f"got table name: {got.table_name}")
    except Exception as e:
        print(f"get_table({project_id}/{table_name}) returned: {e}")


if __name__ == "__main__":
    test_lazy_endpoint_resolution()
