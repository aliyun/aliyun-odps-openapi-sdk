// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog;

import com.aliyun.tea.*;
import com.aliyun.odps.catalog.models.*;

public class Client extends com.aliyun.odps.Client {

    public Client(com.aliyun.odps.models.Config config) throws Exception {
        super(config);
    }


    public Table updateTableWithOptions(Table table, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        return TeaModel.toModel(this.requestWithModel(table, "PUT", this.getTablePath(table), runtime), new Table());
    }

    public Table updateTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return this.updateTableWithOptions(table, runtime);
    }

    public HttpResponse deleteTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithoutModel(table, "DELETE", this.getTablePath(table), runtime), new HttpResponse());
    }

    public Table createTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(table, "POST", this.getTablesPath(table), runtime), new Table());
    }

    public Table getTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(table, "GET", this.getTablePath(table), runtime), new Table());
    }

    public String getTablePath(Table table) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(table.schemaName)) {
            return "/api/catalog/v1alpha/projects/" + table.projectId + "/schemas/default/tables/" + table.tableName + "";
        } else {
            return "/api/catalog/v1alpha/projects/" + table.projectId + "/schemas/" + table.schemaName + "/tables/" + table.tableName + "";
        }

    }

    public String getTablesPath(Table table) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(table.schemaName)) {
            return "/api/catalog/v1alpha/projects/" + table.projectId + "/schemas/default/tables";
        } else {
            return "/api/catalog/v1alpha/projects/" + table.projectId + "/schemas/" + table.schemaName + "/tables";
        }

    }
}
