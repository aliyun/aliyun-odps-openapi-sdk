# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from maxcompute_tea_openapi.client import Client as OpenApiClient
from maxcompute_tea_openapi import models as open_api_models
from pyodps_catalog import models as catalog_api_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from maxcompute_tea_util.client import Client as McUtilClient


class Client(OpenApiClient):
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)

    def update_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            self.request_with_model(table, 'PUT', self.get_table_path(table), None, runtime)
        )

    async def update_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_with_model_async(table, 'PUT', self.get_table_path(table), None, runtime)
        )

    def delete_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', self.get_table_path(table), None, runtime)
        )

    async def delete_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', self.get_table_path(table), None, runtime)
        )

    def create_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            self.request_with_model(table, 'POST', self.get_tables_path(table), None, runtime)
        )

    async def create_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_with_model_async(table, 'POST', self.get_tables_path(table), None, runtime)
        )

    def get_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            self.request('GET', self.get_table_path(table), None, runtime)
        )

    async def get_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_async('GET', self.get_table_path(table), None, runtime)
        )

    def list_tables(
        self,
        project_id: str,
        schema_name: str,
        page_size: int,
        page_token: str,
        view: str,
        query: str,
    ) -> catalog_api_models.ListTablesResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/tables'
        param = {}
        if not UtilClient.is_unset(page_size):
            param['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            param['pageToken'] = page_token
        if not UtilClient.is_unset(view):
            param['view'] = view
            if not UtilClient.equal_string(view, 'BASIC'):
                param['apiScope'] = 'inner'
        if not UtilClient.is_unset(query):
            param['query'] = query
        return TeaCore.from_map(
            catalog_api_models.ListTablesResponse(),
            self.request('GET', path, param, runtime)
        )

    async def list_tables_async(
        self,
        project_id: str,
        schema_name: str,
        page_size: int,
        page_token: str,
        view: str,
        query: str,
    ) -> catalog_api_models.ListTablesResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/tables'
        param = {}
        if not UtilClient.is_unset(page_size):
            param['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            param['pageToken'] = page_token
        if not UtilClient.is_unset(view):
            param['view'] = view
            if not UtilClient.equal_string(view, 'BASIC'):
                param['apiScope'] = 'inner'
        if not UtilClient.is_unset(query):
            param['query'] = query
        return TeaCore.from_map(
            catalog_api_models.ListTablesResponse(),
            await self.request_async('GET', path, param, runtime)
        )

    def set_table_policy(
        self,
        table: catalog_api_models.Table,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_table_path(table)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_table_policy_async(
        self,
        table: catalog_api_models.Table,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_table_path(table)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )

    def get_table_policy(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_table_path(table)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request('POST', path, query, runtime)
        )

    async def get_table_policy_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_table_path(table)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_async('POST', path, query, runtime)
        )

    def get_table_path(
        self,
        table: catalog_api_models.Table,
    ) -> str:
        if UtilClient.is_unset(table.schema_name):
            return f'/api/catalog/v1alpha/projects/{table.project_id}/schemas/default/tables/{table.table_name}'
        else:
            return f'/api/catalog/v1alpha/projects/{table.project_id}/schemas/{table.schema_name}/tables/{table.table_name}'

    def get_tables_path(
        self,
        table: catalog_api_models.Table,
    ) -> str:
        if UtilClient.is_unset(table.schema_name):
            return f'/api/catalog/v1alpha/projects/{table.project_id}/schemas/default/tables'
        else:
            return f'/api/catalog/v1alpha/projects/{table.project_id}/schemas/{table.schema_name}/tables'

    def create_connection(
        self,
        namespace: str,
        connection: catalog_api_models.Connection,
    ) -> catalog_api_models.Connection:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/connections'
        return TeaCore.from_map(
            catalog_api_models.Connection(),
            self.request_with_model(connection, 'POST', path, None, runtime)
        )

    async def create_connection_async(
        self,
        namespace: str,
        connection: catalog_api_models.Connection,
    ) -> catalog_api_models.Connection:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/connections'
        return TeaCore.from_map(
            catalog_api_models.Connection(),
            await self.request_with_model_async(connection, 'POST', path, None, runtime)
        )

    def list_connections(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListConnectionsResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/connections'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListConnectionsResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_connections_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListConnectionsResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/connections'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListConnectionsResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def get_connection(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.Connection:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        return TeaCore.from_map(
            catalog_api_models.Connection(),
            self.request('GET', path, None, runtime)
        )

    async def get_connection_async(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.Connection:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        return TeaCore.from_map(
            catalog_api_models.Connection(),
            await self.request_async('GET', path, None, runtime)
        )

    def update_connection(
        self,
        namespace: str,
        connection_name: str,
        connection: catalog_api_models.Connection,
        update_mask: str,
    ) -> catalog_api_models.Connection:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        query = {}
        query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Connection(),
            self.request_with_model(connection, 'PATCH', path, query, runtime)
        )

    async def update_connection_async(
        self,
        namespace: str,
        connection_name: str,
        connection: catalog_api_models.Connection,
        update_mask: str,
    ) -> catalog_api_models.Connection:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        query = {}
        query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Connection(),
            await self.request_with_model_async(connection, 'PATCH', path, query, runtime)
        )

    def delete_connection(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', path, None, runtime)
        )

    async def delete_connection_async(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', path, None, runtime)
        )

    def set_connection_policy(
        self,
        namespace: str,
        connection_name: str,
        request: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_connection_path(namespace, connection_name)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(request, 'POST', path, query, runtime)
        )

    async def set_connection_policy_async(
        self,
        namespace: str,
        connection_name: str,
        request: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_connection_path(namespace, connection_name)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(request, 'POST', path, query, runtime)
        )

    def get_connection_policy(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_connection_path(namespace, connection_name)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request('POST', path, query, runtime)
        )

    async def get_connection_policy_async(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_connection_path(namespace, connection_name)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_async('POST', path, query, runtime)
        )

    def get_connection_path(
        self,
        namespace: str,
        connection_name: str,
    ) -> str:
        return f'/api/catalog/v1alpha/namespaces/{namespace}/connections/{connection_name}'

    def get_role_path(
        self,
        namespace: str,
        role_name: str,
    ) -> str:
        """
        Path generation helper
        """
        return f'/api/catalog/v1alpha/namespaces/{namespace}/roles/{role_name}'

    def create_role(
        self,
        namespace: str,
        role: catalog_api_models.Role,
    ) -> catalog_api_models.Role:
        """
        Create role
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/roles'
        return TeaCore.from_map(
            catalog_api_models.Role(),
            self.request_with_model(role, 'POST', path, None, runtime)
        )

    async def create_role_async(
        self,
        namespace: str,
        role: catalog_api_models.Role,
    ) -> catalog_api_models.Role:
        """
        Create role
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/roles'
        return TeaCore.from_map(
            catalog_api_models.Role(),
            await self.request_with_model_async(role, 'POST', path, None, runtime)
        )

    def delete_role(
        self,
        namespace: str,
        role_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        Delete role
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', path, None, runtime)
        )

    async def delete_role_async(
        self,
        namespace: str,
        role_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        Delete role
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', path, None, runtime)
        )

    def get_role(
        self,
        namespace: str,
        role_name: str,
    ) -> catalog_api_models.Role:
        """
        Get role
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        return TeaCore.from_map(
            catalog_api_models.Role(),
            self.request('GET', path, None, runtime)
        )

    async def get_role_async(
        self,
        namespace: str,
        role_name: str,
    ) -> catalog_api_models.Role:
        """
        Get role
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        return TeaCore.from_map(
            catalog_api_models.Role(),
            await self.request_async('GET', path, None, runtime)
        )

    def list_roles(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
        view: str,
        show_deleted: bool,
    ) -> catalog_api_models.ListRolesResponse:
        """
        List roles
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/roles'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        if not UtilClient.is_unset(view):
            query['view'] = view
        if not UtilClient.is_unset(show_deleted):
            query['showDeleted'] = McUtilClient.to_string(show_deleted)
        return TeaCore.from_map(
            catalog_api_models.ListRolesResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_roles_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
        view: str,
        show_deleted: bool,
    ) -> catalog_api_models.ListRolesResponse:
        """
        List roles
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/roles'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        if not UtilClient.is_unset(view):
            query['view'] = view
        if not UtilClient.is_unset(show_deleted):
            query['showDeleted'] = McUtilClient.to_string(show_deleted)
        return TeaCore.from_map(
            catalog_api_models.ListRolesResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def update_role(
        self,
        namespace: str,
        role_name: str,
        role: catalog_api_models.Role,
        update_mask: str,
    ) -> catalog_api_models.Role:
        """
        Update role
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        query = {}
        if not UtilClient.is_unset(update_mask):
            query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Role(),
            self.request_with_model(role, 'PATCH', path, query, runtime)
        )

    async def update_role_async(
        self,
        namespace: str,
        role_name: str,
        role: catalog_api_models.Role,
        update_mask: str,
    ) -> catalog_api_models.Role:
        """
        Update role
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        query = {}
        if not UtilClient.is_unset(update_mask):
            query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Role(),
            await self.request_with_model_async(role, 'PATCH', path, query, runtime)
        )

    def set_role_policy(
        self,
        namespace: str,
        role_name: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        Set role policy
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_role_path(namespace, role_name)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_role_policy_async(
        self,
        namespace: str,
        role_name: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        Set role policy
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_role_path(namespace, role_name)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )

    def get_role_policy(
        self,
        namespace: str,
        role_name: str,
    ) -> catalog_api_models.Policy:
        """
        Get role policy
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_role_path(namespace, role_name)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request('POST', path, query, runtime)
        )

    async def get_role_policy_async(
        self,
        namespace: str,
        role_name: str,
    ) -> catalog_api_models.Policy:
        """
        Get role policy
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_role_path(namespace, role_name)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_async('POST', path, query, runtime)
        )

    def get_taxonomy_path(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> str:
        """
        Path generation helpers
        """
        return f'/api/catalog/v1alpha/namespaces/{namespace}/taxonomies/{taxonomy_id}'

    def get_policy_tag_path(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> str:
        return f'{self.get_taxonomy_path(namespace, taxonomy_id)}/policyTags/{policy_tag_id}'

    def create_taxonomy(
        self,
        namespace: str,
        taxonomy: catalog_api_models.Taxonomy,
    ) -> catalog_api_models.Taxonomy:
        """
        Taxonomy operations
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/taxonomies'
        return TeaCore.from_map(
            catalog_api_models.Taxonomy(),
            self.request_with_model(taxonomy, 'POST', path, None, runtime)
        )

    async def create_taxonomy_async(
        self,
        namespace: str,
        taxonomy: catalog_api_models.Taxonomy,
    ) -> catalog_api_models.Taxonomy:
        """
        Taxonomy operations
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/taxonomies'
        return TeaCore.from_map(
            catalog_api_models.Taxonomy(),
            await self.request_with_model_async(taxonomy, 'POST', path, None, runtime)
        )

    def delete_taxonomy(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', path, None, runtime)
        )

    async def delete_taxonomy_async(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', path, None, runtime)
        )

    def get_taxonomy(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.Taxonomy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        return TeaCore.from_map(
            catalog_api_models.Taxonomy(),
            self.request('GET', path, None, runtime)
        )

    async def get_taxonomy_async(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.Taxonomy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        return TeaCore.from_map(
            catalog_api_models.Taxonomy(),
            await self.request_async('GET', path, None, runtime)
        )

    def list_taxonomies(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListTaxonomiesResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/taxonomies'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListTaxonomiesResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_taxonomies_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListTaxonomiesResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/taxonomies'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListTaxonomiesResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def update_taxonomy(
        self,
        namespace: str,
        taxonomy_id: str,
        taxonomy: catalog_api_models.Taxonomy,
        update_mask: str,
    ) -> catalog_api_models.Taxonomy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        query = {}
        if not UtilClient.is_unset(update_mask):
            query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Taxonomy(),
            self.request_with_model(taxonomy, 'PATCH', path, query, runtime)
        )

    async def update_taxonomy_async(
        self,
        namespace: str,
        taxonomy_id: str,
        taxonomy: catalog_api_models.Taxonomy,
        update_mask: str,
    ) -> catalog_api_models.Taxonomy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        query = {}
        if not UtilClient.is_unset(update_mask):
            query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Taxonomy(),
            await self.request_with_model_async(taxonomy, 'PATCH', path, query, runtime)
        )

    def set_taxonomy_policy(
        self,
        namespace: str,
        taxonomy_id: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}:setPolicy'
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_taxonomy_policy_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}:setPolicy'
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )

    def get_taxonomy_policy(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request('POST', path, query, runtime)
        )

    async def get_taxonomy_policy_async(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_async('POST', path, query, runtime)
        )

    def create_policy_tag(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag: catalog_api_models.PolicyTag,
    ) -> catalog_api_models.PolicyTag:
        """
        PolicyTag operations
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}/policyTags'
        return TeaCore.from_map(
            catalog_api_models.PolicyTag(),
            self.request_with_model(policy_tag, 'POST', path, None, runtime)
        )

    async def create_policy_tag_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag: catalog_api_models.PolicyTag,
    ) -> catalog_api_models.PolicyTag:
        """
        PolicyTag operations
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}/policyTags'
        return TeaCore.from_map(
            catalog_api_models.PolicyTag(),
            await self.request_with_model_async(policy_tag, 'POST', path, None, runtime)
        )

    def delete_policy_tag(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', path, None, runtime)
        )

    async def delete_policy_tag_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', path, None, runtime)
        )

    def get_policy_tag(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.PolicyTag:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        return TeaCore.from_map(
            catalog_api_models.PolicyTag(),
            self.request('GET', path, None, runtime)
        )

    async def get_policy_tag_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.PolicyTag:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        return TeaCore.from_map(
            catalog_api_models.PolicyTag(),
            await self.request_async('GET', path, None, runtime)
        )

    def list_policy_tags(
        self,
        namespace: str,
        taxonomy_id: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListPolicyTagsResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}/policyTags'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListPolicyTagsResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_policy_tags_async(
        self,
        namespace: str,
        taxonomy_id: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListPolicyTagsResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}/policyTags'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListPolicyTagsResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def update_policy_tag(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
        policy_tag: catalog_api_models.PolicyTag,
        update_mask: str,
    ) -> catalog_api_models.PolicyTag:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        query = {}
        if not UtilClient.is_unset(update_mask):
            query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.PolicyTag(),
            self.request_with_model(policy_tag, 'PATCH', path, query, runtime)
        )

    async def update_policy_tag_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
        policy_tag: catalog_api_models.PolicyTag,
        update_mask: str,
    ) -> catalog_api_models.PolicyTag:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        query = {}
        if not UtilClient.is_unset(update_mask):
            query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.PolicyTag(),
            await self.request_with_model_async(policy_tag, 'PATCH', path, query, runtime)
        )

    def set_policy_tag_policy(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_policy_tag_policy_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )

    def get_policy_tag_policy(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request('POST', path, query, runtime)
        )

    async def get_policy_tag_policy_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_async('POST', path, query, runtime)
        )

    def create_data_policy(
        self,
        namespace: str,
        data_policy: catalog_api_models.DataPolicy,
    ) -> catalog_api_models.DataPolicy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policies_path(namespace)
        return TeaCore.from_map(
            catalog_api_models.DataPolicy(),
            self.request_with_model(data_policy, 'POST', path, None, runtime)
        )

    async def create_data_policy_async(
        self,
        namespace: str,
        data_policy: catalog_api_models.DataPolicy,
    ) -> catalog_api_models.DataPolicy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policies_path(namespace)
        return TeaCore.from_map(
            catalog_api_models.DataPolicy(),
            await self.request_with_model_async(data_policy, 'POST', path, None, runtime)
        )

    def delete_data_policy(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', path, None, runtime)
        )

    async def delete_data_policy_async(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', path, None, runtime)
        )

    def get_data_policy(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.DataPolicy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        return TeaCore.from_map(
            catalog_api_models.DataPolicy(),
            self.request('GET', path, None, runtime)
        )

    async def get_data_policy_async(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.DataPolicy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        return TeaCore.from_map(
            catalog_api_models.DataPolicy(),
            await self.request_async('GET', path, None, runtime)
        )

    def list_data_policies(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataPoliciesResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policies_path(namespace)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataPoliciesResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_data_policies_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataPoliciesResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policies_path(namespace)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataPoliciesResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def set_data_policy_policy(
        self,
        namespace: str,
        data_policy_name: str,
        request: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_data_policy_path(namespace, data_policy_name)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(request, 'POST', path, query, runtime)
        )

    async def set_data_policy_policy_async(
        self,
        namespace: str,
        data_policy_name: str,
        request: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_data_policy_path(namespace, data_policy_name)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(request, 'POST', path, query, runtime)
        )

    def get_data_policy_policy(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_data_policy_path(namespace, data_policy_name)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request('POST', path, query, runtime)
        )

    async def get_data_policy_policy_async(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_data_policy_path(namespace, data_policy_name)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_async('POST', path, query, runtime)
        )

    def get_data_policy_path(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> str:
        return f'/api/catalog/v1alpha/namespaces/{namespace}/dataPolicies/{data_policy_name}'

    def get_data_policies_path(
        self,
        namespace: str,
    ) -> str:
        return f'/api/catalog/v1alpha/namespaces/{namespace}/dataPolicies'

    def get_project_path(
        self,
        project_id: str,
    ) -> str:
        """
        Paths
        """
        return f'/api/catalog/v1alpha/projects/{project_id}'

    def get_schema_path(
        self,
        project_id: str,
        schema_name: str,
    ) -> str:
        return f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}'

    def list_projects(
        self,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListProjectsResponse:
        """
        Methods
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListProjectsResponse(),
            self.request('GET', '/api/catalog/v1alpha/projects', query, runtime)
        )

    async def list_projects_async(
        self,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListProjectsResponse:
        """
        Methods
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListProjectsResponse(),
            await self.request_async('GET', '/api/catalog/v1alpha/projects', query, runtime)
        )

    def get_project(
        self,
        project_id: str,
        view: str,
    ) -> catalog_api_models.Project:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        query = {}
        if not UtilClient.is_unset(view):
            query['view'] = view
            if not UtilClient.equal_string(view, 'BASIC'):
                query['apiScope'] = 'inner'
        return TeaCore.from_map(
            catalog_api_models.Project(),
            self.request('GET', self.get_project_path(project_id), query, runtime)
        )

    async def get_project_async(
        self,
        project_id: str,
        view: str,
    ) -> catalog_api_models.Project:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        query = {}
        if not UtilClient.is_unset(view):
            query['view'] = view
            if not UtilClient.equal_string(view, 'BASIC'):
                query['apiScope'] = 'inner'
        return TeaCore.from_map(
            catalog_api_models.Project(),
            await self.request_async('GET', self.get_project_path(project_id), query, runtime)
        )

    def create_schema(
        self,
        project_id: str,
        schema: catalog_api_models.Schema,
    ) -> catalog_api_models.Schema:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas'
        return TeaCore.from_map(
            catalog_api_models.Schema(),
            self.request_with_model(schema, 'POST', path, None, runtime)
        )

    async def create_schema_async(
        self,
        project_id: str,
        schema: catalog_api_models.Schema,
    ) -> catalog_api_models.Schema:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas'
        return TeaCore.from_map(
            catalog_api_models.Schema(),
            await self.request_with_model_async(schema, 'POST', path, None, runtime)
        )

    def list_schemas(
        self,
        project_id: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListSchemasResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListSchemasResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_schemas_async(
        self,
        project_id: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListSchemasResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListSchemasResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def get_schema(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.Schema:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Schema(),
            self.request('GET', self.get_schema_path(project_id, schema_name), None, runtime)
        )

    async def get_schema_async(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.Schema:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Schema(),
            await self.request_async('GET', self.get_schema_path(project_id, schema_name), None, runtime)
        )

    def update_schema(
        self,
        project_id: str,
        schema_name: str,
        update_mask: str,
        schema: catalog_api_models.Schema,
    ) -> catalog_api_models.Schema:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        query = {}
        query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Schema(),
            self.request_with_model(schema, 'PATCH', path, query, runtime)
        )

    async def update_schema_async(
        self,
        project_id: str,
        schema_name: str,
        update_mask: str,
        schema: catalog_api_models.Schema,
    ) -> catalog_api_models.Schema:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        query = {}
        query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Schema(),
            await self.request_with_model_async(schema, 'PATCH', path, query, runtime)
        )

    def delete_schema(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', path, None, runtime)
        )

    async def delete_schema_async(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', path, None, runtime)
        )

    def set_schema_policy(
        self,
        project_id: str,
        schema_name: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_schema_path(project_id, schema_name)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_schema_policy_async(
        self,
        project_id: str,
        schema_name: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_schema_path(project_id, schema_name)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )

    def get_schema_policy(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_schema_path(project_id, schema_name)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request('POST', path, query, runtime)
        )

    async def get_schema_policy_async(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.Policy:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_schema_path(project_id, schema_name)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_async('POST', path, query, runtime)
        )

    def get_table_partitions_path(
        self,
        project_id: str,
        schema_name: str,
        table_name: str,
    ) -> str:
        """
        Path Functions
        """
        return f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/tables/{table_name}/partitions'

    def list_partitions(
        self,
        project_id: str,
        schema_name: str,
        table_name: str,
        page_size: int,
        page_token: str,
        query: str,
        view: str,
    ) -> catalog_api_models.ListPartitionsResponse:
        """
        Methods
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_table_partitions_path(project_id, schema_name, table_name)
        params = {}
        if not UtilClient.is_unset(page_size):
            params['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            params['pageToken'] = page_token
        if not UtilClient.is_unset(query):
            params['query'] = query
        if not UtilClient.is_unset(view):
            params['view'] = view
            if not UtilClient.equal_string(view, 'BASIC'):
                params['apiScope'] = 'inner'
        return TeaCore.from_map(
            catalog_api_models.ListPartitionsResponse(),
            self.request('GET', path, params, runtime)
        )

    async def list_partitions_async(
        self,
        project_id: str,
        schema_name: str,
        table_name: str,
        page_size: int,
        page_token: str,
        query: str,
        view: str,
    ) -> catalog_api_models.ListPartitionsResponse:
        """
        Methods
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_table_partitions_path(project_id, schema_name, table_name)
        params = {}
        if not UtilClient.is_unset(page_size):
            params['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            params['pageToken'] = page_token
        if not UtilClient.is_unset(query):
            params['query'] = query
        if not UtilClient.is_unset(view):
            params['view'] = view
            if not UtilClient.equal_string(view, 'BASIC'):
                params['apiScope'] = 'inner'
        return TeaCore.from_map(
            catalog_api_models.ListPartitionsResponse(),
            await self.request_async('GET', path, params, runtime)
        )

    def get_data_scan_path(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> str:
        return f'/api/catalog/v1alpha/namespaces/{namespace}/dataScans/{data_scan_name}'

    def get_data_scans_path(
        self,
        namespace: str,
    ) -> str:
        return f'/api/catalog/v1alpha/namespaces/{namespace}/dataScans'

    def get_trigger_data_scan_path(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> str:
        return f'/api/catalog/v1alpha/namespaces/{namespace}/dataScans/{data_scan_name}:trigger'

    def trigger_data_scan(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('POST', self.get_trigger_data_scan_path(namespace, data_scan_name), None, util_models.RuntimeOptions())
        )

    async def trigger_data_scan_async(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('POST', self.get_trigger_data_scan_path(namespace, data_scan_name), None, util_models.RuntimeOptions())
        )

    def update_data_scan(
        self,
        namespace: str,
        data_scan: catalog_api_models.DataScan,
        update_mask: str,
    ) -> catalog_api_models.DataScan:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        query = {}
        query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.DataScan(),
            self.request_with_model(data_scan, 'PATCH', self.get_data_scan_path(namespace, data_scan.scan_name), query, runtime)
        )

    async def update_data_scan_async(
        self,
        namespace: str,
        data_scan: catalog_api_models.DataScan,
        update_mask: str,
    ) -> catalog_api_models.DataScan:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        query = {}
        query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.DataScan(),
            await self.request_with_model_async(data_scan, 'PATCH', self.get_data_scan_path(namespace, data_scan.scan_name), query, runtime)
        )

    def delete_data_scan(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', self.get_data_scan_path(namespace, data_scan_name), None, runtime)
        )

    async def delete_data_scan_async(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', self.get_data_scan_path(namespace, data_scan_name), None, runtime)
        )

    def create_data_scan(
        self,
        namespace: str,
        data_scan: catalog_api_models.DataScan,
    ) -> catalog_api_models.DataScan:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.DataScan(),
            self.request_with_model(data_scan, 'POST', self.get_data_scans_path(namespace), None, runtime)
        )

    async def create_data_scan_async(
        self,
        namespace: str,
        data_scan: catalog_api_models.DataScan,
    ) -> catalog_api_models.DataScan:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.DataScan(),
            await self.request_with_model_async(data_scan, 'POST', self.get_data_scans_path(namespace), None, runtime)
        )

    def get_data_scan(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.DataScan:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.DataScan(),
            self.request('GET', self.get_data_scan_path(namespace, data_scan_name), None, runtime)
        )

    async def get_data_scan_async(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.DataScan:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.DataScan(),
            await self.request_async('GET', self.get_data_scan_path(namespace, data_scan_name), None, runtime)
        )

    def list_data_scans(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataScansResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_scans_path(namespace)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataScansResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_data_scans_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataScansResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_scans_path(namespace)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataScansResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def get_data_scan_jobs_path(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> str:
        return f'/api/catalog/v1alpha/namespaces/{namespace}/dataScans/{data_scan_name}/scanJobs'

    def list_data_scan_jobs(
        self,
        namespace: str,
        data_scan_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataScanJobsResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_scan_jobs_path(namespace, data_scan_name)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataScanJobsResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_data_scan_jobs_async(
        self,
        namespace: str,
        data_scan_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataScanJobsResponse:
        """
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_data_scan_jobs_path(namespace, data_scan_name)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataScanJobsResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def get_model_path(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        version_name: str,
    ) -> str:
        """
        路径生成函数
        """
        if UtilClient.is_unset(version_name):
            return f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}'
        else:
            return f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}@{version_name}'

    def create_model(
        self,
        project_id: str,
        schema_name: str,
        model: catalog_api_models.Model,
    ) -> catalog_api_models.Model:
        """
        创建模型
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models'
        return TeaCore.from_map(
            catalog_api_models.Model(),
            self.request_with_model(model, 'POST', path, None, runtime)
        )

    async def create_model_async(
        self,
        project_id: str,
        schema_name: str,
        model: catalog_api_models.Model,
    ) -> catalog_api_models.Model:
        """
        创建模型
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models'
        return TeaCore.from_map(
            catalog_api_models.Model(),
            await self.request_with_model_async(model, 'POST', path, None, runtime)
        )

    def list_models(
        self,
        project_id: str,
        schema_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListModelsResponse:
        """
        列出模型
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListModelsResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_models_async(
        self,
        project_id: str,
        schema_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListModelsResponse:
        """
        列出模型
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListModelsResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def get_model(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        version_name: str,
    ) -> catalog_api_models.Model:
        """
        获取模型
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, version_name)
        return TeaCore.from_map(
            catalog_api_models.Model(),
            self.request('GET', path, None, runtime)
        )

    async def get_model_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        version_name: str,
    ) -> catalog_api_models.Model:
        """
        获取模型
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, version_name)
        return TeaCore.from_map(
            catalog_api_models.Model(),
            await self.request_async('GET', path, None, runtime)
        )

    def update_model(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        model: catalog_api_models.Model,
        update_mask: str,
        version_name: str,
    ) -> catalog_api_models.Model:
        """
        更新模型
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, version_name)
        query = {}
        if not UtilClient.is_unset(update_mask):
            query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Model(),
            self.request_with_model(model, 'PATCH', path, query, runtime)
        )

    async def update_model_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        model: catalog_api_models.Model,
        update_mask: str,
        version_name: str,
    ) -> catalog_api_models.Model:
        """
        更新模型
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, version_name)
        query = {}
        if not UtilClient.is_unset(update_mask):
            query['updateMask'] = update_mask
        return TeaCore.from_map(
            catalog_api_models.Model(),
            await self.request_with_model_async(model, 'PATCH', path, query, runtime)
        )

    def delete_model(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        删除模型
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, None)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', path, None, runtime)
        )

    async def delete_model_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        删除模型
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, None)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', path, None, runtime)
        )

    def create_model_version(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        model: catalog_api_models.Model,
    ) -> catalog_api_models.Model:
        """
        创建模型版本
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}:createVersion'
        return TeaCore.from_map(
            catalog_api_models.Model(),
            self.request_with_model(model, 'POST', path, None, runtime)
        )

    async def create_model_version_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        model: catalog_api_models.Model,
    ) -> catalog_api_models.Model:
        """
        创建模型版本
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}:createVersion'
        return TeaCore.from_map(
            catalog_api_models.Model(),
            await self.request_with_model_async(model, 'POST', path, None, runtime)
        )

    def delete_model_version(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        version_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        删除模型版本
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}@{version_name}:deleteVersion'
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_void('DELETE', path, None, runtime)
        )

    async def delete_model_version_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        version_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        删除模型版本
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}@{version_name}:deleteVersion'
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_void_async('DELETE', path, None, runtime)
        )

    def list_model_versions(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListModelVersionsResponse:
        """
        列出模型版本
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}:listVersions'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListModelVersionsResponse(),
            self.request('GET', path, query, runtime)
        )

    async def list_model_versions_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListModelVersionsResponse:
        """
        列出模型版本
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}:listVersions'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListModelVersionsResponse(),
            await self.request_async('GET', path, query, runtime)
        )

    def get_model_policy(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
    ) -> catalog_api_models.Policy:
        """
        获取模型策略
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_model_path(project_id, schema_name, model_name, None)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request('POST', path, query, runtime)
        )

    async def get_model_policy_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
    ) -> catalog_api_models.Policy:
        """
        获取模型策略
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_model_path(project_id, schema_name, model_name, None)}:getPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_async('POST', path, query, runtime)
        )

    def set_model_policy(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        设置模型策略
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_model_path(project_id, schema_name, model_name, None)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_model_policy_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        policy: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        """
        设置模型策略
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_model_path(project_id, schema_name, model_name, None)}:setPolicy'
        query = {}
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )

    def search(
        self,
        namespace_id: str,
        query: str,
        page_size: int,
        page_token: str,
        order_by: str,
    ) -> catalog_api_models.SearchResponse:
        """
        搜索指定 namespace 下的各种实体。
        @param namespace_id: 主账号ID，在该主账号范围内执行搜索。
        @param query: 搜索查询串，多个条件用逗号分隔。语法示例：name:foo,type=TABLE,region=cn-hangzhou。条件：name:foo（子串匹配名称）；description:bar（子串匹配描述）；type=TABLE（必选，支持 TABLE/RESOURCE/SCHEMA）；project=proj（单 project，需要 SearchProject 权限）；project=(proj1|proj2|proj3)（多 project，最多 512 个，需要权限）；region=region_id（按 region 搜索）。约束：type 必选；单 project 与多 project 互斥；region 与 project 互斥。
        @param page_size: 每页返回结果条数。必须大于 0，最大 100。
        @param page_token: 翻页 token；用于从上一次响应的 token 继续获取下一页。
        @param order_by: 结果排序方式。可取值：default（内部存储顺序，默认）；create_time asc/desc（创建时间正/倒序）；last_modified_time asc/desc（最近修改时间正/倒序）。
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace_id}:search'
        params = {}
        if not UtilClient.is_unset(page_size):
            params['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            params['pageToken'] = page_token
        if not UtilClient.is_unset(query):
            params['query'] = McUtilClient.to_string(query)
        if not UtilClient.is_unset(order_by):
            params['orderBy'] = McUtilClient.to_string(order_by)
        return TeaCore.from_map(
            catalog_api_models.SearchResponse(),
            self.request('POST', path, params, runtime)
        )

    async def search_async(
        self,
        namespace_id: str,
        query: str,
        page_size: int,
        page_token: str,
        order_by: str,
    ) -> catalog_api_models.SearchResponse:
        """
        搜索指定 namespace 下的各种实体。
        @param namespace_id: 主账号ID，在该主账号范围内执行搜索。
        @param query: 搜索查询串，多个条件用逗号分隔。语法示例：name:foo,type=TABLE,region=cn-hangzhou。条件：name:foo（子串匹配名称）；description:bar（子串匹配描述）；type=TABLE（必选，支持 TABLE/RESOURCE/SCHEMA）；project=proj（单 project，需要 SearchProject 权限）；project=(proj1|proj2|proj3)（多 project，最多 512 个，需要权限）；region=region_id（按 region 搜索）。约束：type 必选；单 project 与多 project 互斥；region 与 project 互斥。
        @param page_size: 每页返回结果条数。必须大于 0，最大 100。
        @param page_token: 翻页 token；用于从上一次响应的 token 继续获取下一页。
        @param order_by: 结果排序方式。可取值：default（内部存储顺序，默认）；create_time asc/desc（创建时间正/倒序）；last_modified_time asc/desc（最近修改时间正/倒序）。
        限流：每用户每秒最多 10 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace_id}:search'
        params = {}
        if not UtilClient.is_unset(page_size):
            params['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            params['pageToken'] = page_token
        if not UtilClient.is_unset(query):
            params['query'] = McUtilClient.to_string(query)
        if not UtilClient.is_unset(order_by):
            params['orderBy'] = McUtilClient.to_string(order_by)
        return TeaCore.from_map(
            catalog_api_models.SearchResponse(),
            await self.request_async('POST', path, params, runtime)
        )

    def get_data_token(
        self,
        table: catalog_api_models.Table,
        duration: int,
    ) -> catalog_api_models.DataToken:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_table_path(table)
        full_path = f'{path}:getDataToken'
        params = {}
        if not UtilClient.is_unset(duration):
            params['duration'] = McUtilClient.to_string(duration)
        return TeaCore.from_map(
            catalog_api_models.DataToken(),
            self.request('POST', full_path, params, runtime)
        )

    async def get_data_token_async(
        self,
        table: catalog_api_models.Table,
        duration: int,
    ) -> catalog_api_models.DataToken:
        """
        限流：每用户每秒最多 100 次请求
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_table_path(table)
        full_path = f'{path}:getDataToken'
        params = {}
        if not UtilClient.is_unset(duration):
            params['duration'] = McUtilClient.to_string(duration)
        return TeaCore.from_map(
            catalog_api_models.DataToken(),
            await self.request_async('POST', full_path, params, runtime)
        )
