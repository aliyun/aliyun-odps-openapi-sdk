from alibabacloud_tea_openapi import models as open_api_models
from pyodps_catalog import models as catalog_api_models
from pyodps_catalog.client import Client


if __name__ == '__main__':

    config = open_api_models.Config(
        access_key_id='',
        access_key_secret='=',
        endpoint=''
    )
    client = Client(config)

    project_id = ''
    schema_name = ''
    table_name = ''

    try:
        table = catalog_api_models.Table(
            project_id=project_id,
            schema_name=schema_name,
            table_name=table_name,
        )
        retrieved_table = client.get_table(table)
        print(f"Table: {retrieved_table.to_map()}")

    except Exception as e:
        print(f"Error: {str(e)}")