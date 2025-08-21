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
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            self.request_with_model(table, 'PUT', self.get_table_path(table), None, runtime)
        )

    async def update_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_with_model_async(table, 'PUT', self.get_table_path(table), None, runtime)
        )

    def delete_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(table, 'DELETE', self.get_table_path(table), None, runtime)
        )

    async def delete_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(table, 'DELETE', self.get_table_path(table), None, runtime)
        )

    def create_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            self.request_with_model(table, 'POST', self.get_tables_path(table), None, runtime)
        )

    async def create_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_with_model_async(table, 'POST', self.get_tables_path(table), None, runtime)
        )

    def get_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            self.request_with_model(table, 'GET', self.get_table_path(table), None, runtime)
        )

    async def get_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_with_model_async(table, 'GET', self.get_table_path(table), None, runtime)
        )

    def list_tables(
        self,
        project_id: str,
        schema_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListTablesResponse:
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/tables'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListTablesResponse(),
            self.request_with_model(catalog_api_models.ListTablesResponse(), 'GET', path, query, runtime)
        )

    async def list_tables_async(
        self,
        project_id: str,
        schema_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListTablesResponse:
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/tables'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListTablesResponse(),
            await self.request_with_model_async(catalog_api_models.ListTablesResponse(), 'GET', path, query, runtime)
        )

    def set_table_policy(
        self,
        table: catalog_api_models.Table,
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_table_path(table)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_table_policy_async(
        self,
        table: catalog_api_models.Table,
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_table_path(table)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )

    def get_table_policy(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_table_path(table)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    async def get_table_policy_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_table_path(table)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(catalog_api_models.Policy(), 'POST', path, query, runtime)
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
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/connections'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListConnectionsResponse(),
            self.request_with_model(catalog_api_models.ListConnectionsResponse(), 'GET', path, query, runtime)
        )

    async def list_connections_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/connections'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListConnectionsResponse(),
            await self.request_with_model_async(catalog_api_models.ListConnectionsResponse(), 'GET', path, query, runtime)
        )

    def get_connection(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.Connection:
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        return TeaCore.from_map(
            catalog_api_models.Connection(),
            self.request_with_model(catalog_api_models.Connection(), 'GET', path, None, runtime)
        )

    async def get_connection_async(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.Connection:
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        return TeaCore.from_map(
            catalog_api_models.Connection(),
            await self.request_with_model_async(catalog_api_models.Connection(), 'GET', path, None, runtime)
        )

    def update_connection(
        self,
        namespace: str,
        connection_name: str,
        connection: catalog_api_models.Connection,
        update_mask: str,
    ) -> catalog_api_models.Connection:
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
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(catalog_api_models.Connection(), 'DELETE', path, None, runtime)
        )

    async def delete_connection_async(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(catalog_api_models.Connection(), 'DELETE', path, None, runtime)
        )

    def set_connection_policy(
        self,
        namespace: str,
        connection_name: str,
        request: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        query = {}
        query['method'] = 'setPolicy'
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
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(request, 'POST', path, query, runtime)
        )

    def get_connection_policy(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    async def get_connection_policy_async(
        self,
        namespace: str,
        connection_name: str,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_connection_path(namespace, connection_name)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(catalog_api_models.Policy(), 'POST', path, query, runtime)
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
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(catalog_api_models.Role(), 'DELETE', path, None, runtime)
        )

    async def delete_role_async(
        self,
        namespace: str,
        role_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        Delete role
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(catalog_api_models.Role(), 'DELETE', path, None, runtime)
        )

    def get_role(
        self,
        namespace: str,
        role_name: str,
        view: str,
    ) -> catalog_api_models.Role:
        """
        Get role
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        query = {}
        if not UtilClient.is_unset(view):
            query['view'] = view
        return TeaCore.from_map(
            catalog_api_models.Role(),
            self.request_with_model(catalog_api_models.Role(), 'GET', path, query, runtime)
        )

    async def get_role_async(
        self,
        namespace: str,
        role_name: str,
        view: str,
    ) -> catalog_api_models.Role:
        """
        Get role
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        query = {}
        if not UtilClient.is_unset(view):
            query['view'] = view
        return TeaCore.from_map(
            catalog_api_models.Role(),
            await self.request_with_model_async(catalog_api_models.Role(), 'GET', path, query, runtime)
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
            self.request_with_model(catalog_api_models.ListRolesResponse(), 'GET', path, query, runtime)
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
            await self.request_with_model_async(catalog_api_models.ListRolesResponse(), 'GET', path, query, runtime)
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
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        """
        Set role policy
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_role_policy_async(
        self,
        namespace: str,
        role_name: str,
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        """
        Set role policy
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        query = {}
        query['method'] = 'setPolicy'
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
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    async def get_role_policy_async(
        self,
        namespace: str,
        role_name: str,
    ) -> catalog_api_models.Policy:
        """
        Get role policy
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_role_path(namespace, role_name)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(catalog_api_models.Policy(), 'POST', path, query, runtime)
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
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(catalog_api_models.Taxonomy(), 'DELETE', path, None, runtime)
        )

    async def delete_taxonomy_async(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(catalog_api_models.Taxonomy(), 'DELETE', path, None, runtime)
        )

    def get_taxonomy(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.Taxonomy:
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        return TeaCore.from_map(
            catalog_api_models.Taxonomy(),
            self.request_with_model(catalog_api_models.Taxonomy(), 'GET', path, None, runtime)
        )

    async def get_taxonomy_async(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.Taxonomy:
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        return TeaCore.from_map(
            catalog_api_models.Taxonomy(),
            await self.request_with_model_async(catalog_api_models.Taxonomy(), 'GET', path, None, runtime)
        )

    def list_taxonomies(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListTaxonomiesResponse:
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/taxonomies'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListTaxonomiesResponse(),
            self.request_with_model(catalog_api_models.ListTaxonomiesResponse(), 'GET', path, query, runtime)
        )

    async def list_taxonomies_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListTaxonomiesResponse:
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/namespaces/{namespace}/taxonomies'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListTaxonomiesResponse(),
            await self.request_with_model_async(catalog_api_models.ListTaxonomiesResponse(), 'GET', path, query, runtime)
        )

    def update_taxonomy(
        self,
        namespace: str,
        taxonomy_id: str,
        taxonomy: catalog_api_models.Taxonomy,
        update_mask: str,
    ) -> catalog_api_models.Taxonomy:
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
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
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
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
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
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    async def get_taxonomy_policy_async(
        self,
        namespace: str,
        taxonomy_id: str,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_taxonomy_path(namespace, taxonomy_id)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    def create_policy_tag(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag: catalog_api_models.PolicyTag,
    ) -> catalog_api_models.PolicyTag:
        """
        PolicyTag operations
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
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(catalog_api_models.PolicyTag(), 'DELETE', path, None, runtime)
        )

    async def delete_policy_tag_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(catalog_api_models.PolicyTag(), 'DELETE', path, None, runtime)
        )

    def get_policy_tag(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.PolicyTag:
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        return TeaCore.from_map(
            catalog_api_models.PolicyTag(),
            self.request_with_model(catalog_api_models.PolicyTag(), 'GET', path, None, runtime)
        )

    async def get_policy_tag_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.PolicyTag:
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        return TeaCore.from_map(
            catalog_api_models.PolicyTag(),
            await self.request_with_model_async(catalog_api_models.PolicyTag(), 'GET', path, None, runtime)
        )

    def list_policy_tags(
        self,
        namespace: str,
        taxonomy_id: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListPolicyTagsResponse:
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}/policyTags'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListPolicyTagsResponse(),
            self.request_with_model(catalog_api_models.ListPolicyTagsResponse(), 'GET', path, query, runtime)
        )

    async def list_policy_tags_async(
        self,
        namespace: str,
        taxonomy_id: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListPolicyTagsResponse:
        runtime = util_models.RuntimeOptions()
        path = f'{self.get_taxonomy_path(namespace, taxonomy_id)}/policyTags'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListPolicyTagsResponse(),
            await self.request_with_model_async(catalog_api_models.ListPolicyTagsResponse(), 'GET', path, query, runtime)
        )

    def update_policy_tag(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
        policy_tag: catalog_api_models.PolicyTag,
        update_mask: str,
    ) -> catalog_api_models.PolicyTag:
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
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_policy_tag_policy_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        query = {}
        query['method'] = 'setPolicy'
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
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    async def get_policy_tag_policy_async(
        self,
        namespace: str,
        taxonomy_id: str,
        policy_tag_id: str,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_policy_tag_path(namespace, taxonomy_id, policy_tag_id)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    def create_data_policy(
        self,
        namespace: str,
        data_policy: catalog_api_models.DataPolicy,
    ) -> catalog_api_models.DataPolicy:
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
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(catalog_api_models.DataPolicy(), 'DELETE', path, None, runtime)
        )

    async def delete_data_policy_async(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(catalog_api_models.DataPolicy(), 'DELETE', path, None, runtime)
        )

    def get_data_policy(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.DataPolicy:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        return TeaCore.from_map(
            catalog_api_models.DataPolicy(),
            self.request_with_model(catalog_api_models.DataPolicy(), 'GET', path, None, runtime)
        )

    async def get_data_policy_async(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.DataPolicy:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        return TeaCore.from_map(
            catalog_api_models.DataPolicy(),
            await self.request_with_model_async(catalog_api_models.DataPolicy(), 'GET', path, None, runtime)
        )

    def list_data_policies(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policies_path(namespace)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataPoliciesResponse(),
            self.request_with_model(catalog_api_models.ListDataPoliciesResponse(), 'GET', path, query, runtime)
        )

    async def list_data_policies_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policies_path(namespace)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataPoliciesResponse(),
            await self.request_with_model_async(catalog_api_models.ListDataPoliciesResponse(), 'GET', path, query, runtime)
        )

    def set_data_policy_policy(
        self,
        namespace: str,
        data_policy_name: str,
        request: catalog_api_models.SetPolicyRequest,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        query = {}
        query['method'] = 'setPolicy'
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
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(request, 'POST', path, query, runtime)
        )

    def get_data_policy_policy(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    async def get_data_policy_policy_async(
        self,
        namespace: str,
        data_policy_name: str,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_policy_path(namespace, data_policy_name)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(catalog_api_models.Policy(), 'POST', path, query, runtime)
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
        """
        runtime = util_models.RuntimeOptions()
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListProjectsResponse(),
            self.request_with_model(catalog_api_models.ListProjectsResponse(), 'GET', '/api/catalog/v1alpha/projects', query, runtime)
        )

    async def list_projects_async(
        self,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListProjectsResponse:
        """
        Methods
        """
        runtime = util_models.RuntimeOptions()
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListProjectsResponse(),
            await self.request_with_model_async(catalog_api_models.ListProjectsResponse(), 'GET', '/api/catalog/v1alpha/projects', query, runtime)
        )

    def get_project(
        self,
        project_id: str,
    ) -> catalog_api_models.Project:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Project(),
            self.request_with_model(catalog_api_models.Project(), 'GET', self.get_project_path(project_id), None, runtime)
        )

    async def get_project_async(
        self,
        project_id: str,
    ) -> catalog_api_models.Project:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Project(),
            await self.request_with_model_async(catalog_api_models.Project(), 'GET', self.get_project_path(project_id), None, runtime)
        )

    def create_schema(
        self,
        project_id: str,
        schema: catalog_api_models.Schema,
    ) -> catalog_api_models.Schema:
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
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListSchemasResponse(),
            self.request_with_model(catalog_api_models.ListSchemasResponse(), 'GET', path, query, runtime)
        )

    async def list_schemas_async(
        self,
        project_id: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListSchemasResponse:
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas'
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListSchemasResponse(),
            await self.request_with_model_async(catalog_api_models.ListSchemasResponse(), 'GET', path, query, runtime)
        )

    def get_schema(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.Schema:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Schema(),
            self.request_with_model(catalog_api_models.Schema(), 'GET', self.get_schema_path(project_id, schema_name), None, runtime)
        )

    async def get_schema_async(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.Schema:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Schema(),
            await self.request_with_model_async(catalog_api_models.Schema(), 'GET', self.get_schema_path(project_id, schema_name), None, runtime)
        )

    def update_schema(
        self,
        project_id: str,
        schema_name: str,
        update_mask: str,
        schema: catalog_api_models.Schema,
    ) -> catalog_api_models.Schema:
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
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(catalog_api_models.Schema(), 'DELETE', path, None, runtime)
        )

    async def delete_schema_async(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(catalog_api_models.Schema(), 'DELETE', path, None, runtime)
        )

    def set_schema_policy(
        self,
        project_id: str,
        schema_name: str,
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_schema_policy_async(
        self,
        project_id: str,
        schema_name: str,
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )

    def get_schema_policy(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    async def get_schema_policy_async(
        self,
        project_id: str,
        schema_name: str,
    ) -> catalog_api_models.Policy:
        runtime = util_models.RuntimeOptions()
        path = self.get_schema_path(project_id, schema_name)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(catalog_api_models.Policy(), 'POST', path, query, runtime)
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
    ) -> catalog_api_models.ListPartitionsResponse:
        """
        Methods
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_table_partitions_path(project_id, schema_name, table_name)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListPartitionsResponse(),
            self.request_with_model(catalog_api_models.ListPartitionsResponse(), 'GET', path, query, runtime)
        )

    async def list_partitions_async(
        self,
        project_id: str,
        schema_name: str,
        table_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListPartitionsResponse:
        """
        Methods
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_table_partitions_path(project_id, schema_name, table_name)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListPartitionsResponse(),
            await self.request_with_model_async(catalog_api_models.ListPartitionsResponse(), 'GET', path, query, runtime)
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
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(catalog_api_models.ScanJob(), 'POST', self.get_trigger_data_scan_path(namespace, data_scan_name), None, util_models.RuntimeOptions())
        )

    async def trigger_data_scan_async(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.HttpResponse:
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(catalog_api_models.ScanJob(), 'POST', self.get_trigger_data_scan_path(namespace, data_scan_name), None, util_models.RuntimeOptions())
        )

    def update_data_scan(
        self,
        namespace: str,
        data_scan: catalog_api_models.DataScan,
        update_mask: str,
    ) -> catalog_api_models.DataScan:
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
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(catalog_api_models.DataScan(), 'DELETE', self.get_data_scan_path(namespace, data_scan_name), None, runtime)
        )

    async def delete_data_scan_async(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(catalog_api_models.DataScan(), 'DELETE', self.get_data_scan_path(namespace, data_scan_name), None, runtime)
        )

    def create_data_scan(
        self,
        namespace: str,
        data_scan: catalog_api_models.DataScan,
    ) -> catalog_api_models.DataScan:
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
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.DataScan(),
            self.request_with_model(catalog_api_models.DataScan(), 'GET', self.get_data_scan_path(namespace, data_scan_name), None, runtime)
        )

    async def get_data_scan_async(
        self,
        namespace: str,
        data_scan_name: str,
    ) -> catalog_api_models.DataScan:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.DataScan(),
            await self.request_with_model_async(catalog_api_models.DataScan(), 'GET', self.get_data_scan_path(namespace, data_scan_name), None, runtime)
        )

    def list_data_scans(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataScansResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_scans_path(namespace)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataScansResponse(),
            self.request_with_model(catalog_api_models.ListDataScansResponse(), 'GET', path, query, runtime)
        )

    async def list_data_scans_async(
        self,
        namespace: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataScansResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_scans_path(namespace)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataScansResponse(),
            await self.request_with_model_async(catalog_api_models.ListDataScansResponse(), 'GET', path, query, runtime)
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
        runtime = util_models.RuntimeOptions()
        path = self.get_data_scan_jobs_path(namespace, data_scan_name)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataScanJobsResponse(),
            self.request_with_model(catalog_api_models.ListDataScanJobsResponse(), 'GET', path, query, runtime)
        )

    async def list_data_scan_jobs_async(
        self,
        namespace: str,
        data_scan_name: str,
        page_size: int,
        page_token: str,
    ) -> catalog_api_models.ListDataScanJobsResponse:
        runtime = util_models.RuntimeOptions()
        path = self.get_data_scan_jobs_path(namespace, data_scan_name)
        query = {}
        if not UtilClient.is_unset(page_size):
            query['pageSize'] = McUtilClient.to_string(page_size)
        if not UtilClient.is_unset(page_token):
            query['pageToken'] = page_token
        return TeaCore.from_map(
            catalog_api_models.ListDataScanJobsResponse(),
            await self.request_with_model_async(catalog_api_models.ListDataScanJobsResponse(), 'GET', path, query, runtime)
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
            self.request_with_model(catalog_api_models.ListModelsResponse(), 'GET', path, query, runtime)
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
            await self.request_with_model_async(catalog_api_models.ListModelsResponse(), 'GET', path, query, runtime)
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
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, version_name)
        return TeaCore.from_map(
            catalog_api_models.Model(),
            self.request_with_model(catalog_api_models.Model(), 'GET', path, None, runtime)
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
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, version_name)
        return TeaCore.from_map(
            catalog_api_models.Model(),
            await self.request_with_model_async(catalog_api_models.Model(), 'GET', path, None, runtime)
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
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, None)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(None, 'DELETE', path, None, runtime)
        )

    async def delete_model_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
    ) -> catalog_api_models.HttpResponse:
        """
        删除模型
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, None)
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(None, 'DELETE', path, None, runtime)
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
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}@{version_name}:deleteVersion'
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(None, 'DELETE', path, None, runtime)
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
        """
        runtime = util_models.RuntimeOptions()
        path = f'/api/catalog/v1alpha/projects/{project_id}/schemas/{schema_name}/models/{model_name}@{version_name}:deleteVersion'
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(None, 'DELETE', path, None, runtime)
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
            self.request_with_model(catalog_api_models.ListModelVersionsResponse(), 'GET', path, query, runtime)
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
            await self.request_with_model_async(catalog_api_models.ListModelVersionsResponse(), 'GET', path, query, runtime)
        )

    def get_model_policy(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
    ) -> catalog_api_models.Policy:
        """
        获取模型策略
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, None)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    async def get_model_policy_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
    ) -> catalog_api_models.Policy:
        """
        获取模型策略
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, None)
        query = {}
        query['method'] = 'getPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(catalog_api_models.Policy(), 'POST', path, query, runtime)
        )

    def set_model_policy(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        """
        设置模型策略
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, None)
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            self.request_with_model(policy, 'POST', path, query, runtime)
        )

    async def set_model_policy_async(
        self,
        project_id: str,
        schema_name: str,
        model_name: str,
        policy: catalog_api_models.Policy,
    ) -> catalog_api_models.Policy:
        """
        设置模型策略
        """
        runtime = util_models.RuntimeOptions()
        path = self.get_model_path(project_id, schema_name, model_name, None)
        query = {}
        query['method'] = 'setPolicy'
        return TeaCore.from_map(
            catalog_api_models.Policy(),
            await self.request_with_model_async(policy, 'POST', path, query, runtime)
        )
