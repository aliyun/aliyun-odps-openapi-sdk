"""
Comprehensive integration tests for Catalog API.
Covers all GET (body-less) operations to verify the request/requestVoid refactoring.

Reads credentials from environment variables:
  ALIBABA_CLOUD_ACCESS_KEY_ID
  ALIBABA_CLOUD_ACCESS_KEY_SECRET
  odps_endpoint    (e.g. http://service.cn-shanghai.maxcompute.aliyun.com/api)
  PROJECT          (e.g. dingxin)
"""
import os
import sys
from urllib.parse import urlparse

from maxcompute_tea_openapi import models as open_api_models
from pyodps_catalog import models as catalog_api_models
from pyodps_catalog.client import Client


def create_client():
    ak_id = os.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")
    ak_secret = os.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
    raw_odps = os.getenv("odps_endpoint")

    if not all([ak_id, ak_secret, raw_odps]):
        print("SKIP: set ALIBABA_CLOUD_ACCESS_KEY_ID / ALIBABA_CLOUD_ACCESS_KEY_SECRET / odps_endpoint")
        sys.exit(0)

    normalized = raw_odps if "://" in raw_odps else f"http://{raw_odps}"
    parsed = urlparse(normalized)

    config = open_api_models.Config(
        odps_endpoint=parsed.hostname,
        protocol=parsed.scheme,
        access_key_id=ak_id,
        access_key_secret=ak_secret,
    )
    return Client(config)


def test_list_projects(client):
    """GET /projects — list projects with pagination."""
    print("=== test_list_projects ===")
    resp = client.list_projects(2, None)
    assert resp is not None
    assert resp.projects is not None
    assert len(resp.projects) > 0
    print(f"  got {len(resp.projects)} projects, first: {resp.projects[0].project_id}")

    if resp.next_page_token:
        resp2 = client.list_projects(2, resp.next_page_token)
        assert resp2 is not None
        print(f"  page 2: got {len(resp2.projects)} projects")
    print("  PASSED")


def test_get_project(client, project_id):
    """GET /projects/{projectId} — get project details."""
    print("=== test_get_project ===")
    proj = client.get_project(project_id, None)
    assert proj is not None
    assert proj.project_id == project_id
    assert proj.owner is not None
    print(f"  project={proj.project_id}, owner={proj.owner}, region={proj.region}")

    proj_full = client.get_project(project_id, "FULL")
    assert proj_full is not None
    print(f"  FULL view: schema_enabled={proj_full.schema_enabled}")
    print("  PASSED")


def test_list_schemas(client, project_id):
    """GET /projects/{projectId}/schemas — list schemas."""
    print("=== test_list_schemas ===")
    resp = client.list_schemas(project_id, 5, None)
    assert resp is not None
    assert resp.schemas is not None
    assert len(resp.schemas) > 0
    print(f"  got {len(resp.schemas)} schemas:")
    for s in resp.schemas[:3]:
        print(f"    {s.schema_name} (type={s.type})")
    print("  PASSED")
    return resp.schemas[0].schema_name


def test_get_schema(client, project_id, schema_name):
    """GET /projects/{projectId}/schemas/{schemaName} — get schema details."""
    print("=== test_get_schema ===")
    schema = client.get_schema(project_id, schema_name)
    assert schema is not None
    assert schema.schema_name == schema_name
    print(f"  schema={schema.schema_name}, type={schema.type}, owner={schema.owner}")
    print("  PASSED")


def test_list_tables(client, project_id, schema_name):
    """GET /projects/{projectId}/schemas/{schemaName}/tables — list tables."""
    print("=== test_list_tables ===")
    resp = client.list_tables(project_id, schema_name, 3, None, None, None)
    assert resp is not None
    assert resp.tables is not None
    assert len(resp.tables) > 0
    print(f"  got {len(resp.tables)} tables:")
    for t in resp.tables:
        print(f"    {t.table_name} (type={t.type})")

    if resp.next_page_token:
        resp2 = client.list_tables(project_id, schema_name, 3, resp.next_page_token, None, None)
        print(f"  page 2: {len(resp2.tables)} tables")

    print("  PASSED")
    return resp.tables[0].table_name


def test_list_tables_with_view(client, project_id, schema_name):
    """GET /projects/{projectId}/schemas/{schemaName}/tables?view=FULL — with query params."""
    print("=== test_list_tables_with_view ===")
    resp = client.list_tables(project_id, schema_name, 2, None, "FULL", None)
    assert resp is not None
    assert resp.tables is not None
    t = resp.tables[0]
    print(f"  FULL view: {t.table_name}, create_time={t.create_time}, storage={t.num_total_storage_bytes}")
    print("  PASSED")


def test_get_table(client, project_id, schema_name, table_name):
    """GET /projects/{projectId}/schemas/{schemaName}/tables/{tableName} — get table."""
    print("=== test_get_table ===")
    table = catalog_api_models.Table(
        project_id=project_id,
        schema_name=schema_name,
        table_name=table_name,
    )
    got = client.get_table(table)
    assert got is not None
    assert got.table_name == table_name
    assert got.project_id == project_id
    print(f"  table={got.table_name}, type={got.type}")
    if got.table_schema:
        print(f"  schema fields: field_name={got.table_schema.field_name}, type={got.table_schema.sql_type_definition}")
    print("  PASSED")
    return got


def test_list_partitions(client, project_id, schema_name, table_name):
    """GET .../tables/{tableName}/partitions — list partitions."""
    print("=== test_list_partitions ===")
    try:
        resp = client.list_partitions(project_id, schema_name, table_name, 5, None, None, None)
        assert resp is not None
        count = len(resp.partitions) if resp.partitions else 0
        print(f"  got {count} partitions")
        if resp.partitions:
            for p in resp.partitions[:3]:
                print(f"    {p.spec}")
        print("  PASSED")
    except Exception as e:
        if "404" in str(e) or "not partitioned" in str(e).lower():
            print(f"  table is not partitioned or has no partitions, skipping: {str(e)[:80]}")
            print("  SKIPPED")
        else:
            raise


def test_get_table_policy(client, project_id, schema_name, table_name):
    """POST .../tables/{tableName}:getPolicy — body-less POST read operation."""
    print("=== test_get_table_policy ===")
    table = catalog_api_models.Table(
        project_id=project_id,
        schema_name=schema_name,
        table_name=table_name,
    )
    try:
        policy = client.get_table_policy(table)
        assert policy is not None
        bindings_count = len(policy.bindings) if policy.bindings else 0
        print(f"  policy etag={policy.etag}, bindings={bindings_count}")
        print("  PASSED")
    except Exception as e:
        if "403" in str(e):
            print(f"  no permission to get policy, skipping: {str(e)[:80]}")
            print("  SKIPPED")
        else:
            raise


def test_search(client, namespace):
    """POST .../namespaces/{ns}:search — body-less POST search."""
    print("=== test_search ===")
    try:
        resp = client.search(namespace, "type=TABLE", 3, None, None)
        assert resp is not None
        count = len(resp.entries) if resp.entries else 0
        print(f"  search results: {count}")
        if resp.entries:
            for e in resp.entries[:3]:
                print(f"    {e.display_name} ({e.type})")
        print("  PASSED")
    except Exception as e:
        if "403" in str(e) or "400" in str(e):
            print(f"  search not available: {str(e)[:100]}")
            print("  SKIPPED")
        else:
            raise


def main():
    project_id = os.getenv("PROJECT", "dingxin")
    namespace = os.getenv("NAMESPACE")

    client = create_client()
    print(f"Testing with project={project_id}\n")

    # Project-level GET operations
    test_list_projects(client)
    test_get_project(client, project_id)

    # Schema-level GET operations
    schema_name = test_list_schemas(client, project_id)
    test_get_schema(client, project_id, schema_name)

    # Table-level GET operations
    table_name = test_list_tables(client, project_id, "default")
    test_list_tables_with_view(client, project_id, "default")
    test_get_table(client, project_id, "default", table_name)

    # Partition GET
    test_list_partitions(client, project_id, "default", table_name)

    # Body-less POST operations
    test_get_table_policy(client, project_id, "default", table_name)

    if namespace:
        test_search(client, namespace)
    else:
        print("\n=== test_search ===")
        print("  SKIPPED (set NAMESPACE env var to test)")

    print(f"\n{'='*50}")
    print("All tests completed successfully!")


if __name__ == "__main__":
    main()
