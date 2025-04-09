# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from maxcompute_tea_openapi.client import Client as OpenApiClient
from maxcompute_tea_openapi import models as open_api_models
from pyodps_catalog import models as catalog_api_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


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
            self.request_with_model(table, 'PUT', self.get_table_path(table), runtime)
        )

    async def update_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_with_model_async(table, 'PUT', self.get_table_path(table), runtime)
        )

    def delete_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            self.request_without_model(table, 'DELETE', self.get_table_path(table), runtime)
        )

    async def delete_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.HttpResponse:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.HttpResponse(),
            await self.request_without_model_async(table, 'DELETE', self.get_table_path(table), runtime)
        )

    def create_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            self.request_with_model(table, 'POST', self.get_tables_path(table), runtime)
        )

    async def create_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_with_model_async(table, 'POST', self.get_tables_path(table), runtime)
        )

    def get_table(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            self.request_with_model(table, 'GET', self.get_table_path(table), runtime)
        )

    async def get_table_async(
        self,
        table: catalog_api_models.Table,
    ) -> catalog_api_models.Table:
        runtime = util_models.RuntimeOptions()
        return TeaCore.from_map(
            catalog_api_models.Table(),
            await self.request_with_model_async(table, 'GET', self.get_table_path(table), runtime)
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
