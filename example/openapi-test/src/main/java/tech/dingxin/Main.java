package tech.dingxin;

import com.aliyun.odps.catalog.models.GetTableResponse;
import com.aliyun.odps.catalog.models.Table;
import com.aliyun.odps.catalog.models.TableFieldSchema;
import com.aliyun.odps.models.Config;

import java.util.ArrayList;
import java.util.List;

/**
 * @author dingxin (zhangdingxin.zdx@alibaba-inc.com)
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Config config = new Config();
        config.setEndpoint("11.158.225.37:12370");
        config.setAccessKeyId("");
        config.setAccessKeySecret("");

        com.aliyun.odps.catalog.Client catalogClient = new com.aliyun.odps.catalog.Client(config);

        Table table = new Table();
        table.setName("odps_dailyrunnew.test_table");

        TableFieldSchema column = new TableFieldSchema();
        column.setFieldName("test_column");
        column.setTypeCategory("bigint");

        List<TableFieldSchema> tableFieldSchemas = new ArrayList<>();
        tableFieldSchemas.add(column);
        table.setTableSchema(tableFieldSchemas);

        GetTableResponse response = catalogClient.updateTable(table);
        System.out.println(response.getBody());
    }
}