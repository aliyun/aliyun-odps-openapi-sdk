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
        config.setAccessKeyId("63wd3dpztlmb5ocdkj94pxmm");
        config.setAccessKeySecret("oRd30z7sV4hBX9aYtJgii5qnyhg=");

        com.aliyun.odps.catalog.Client catalogClient = new com.aliyun.odps.catalog.Client(config);

        Table table = new Table();
        table.setName("odps_dailyrunnew.test_table");

        TableFieldSchema schema = new TableFieldSchema();
        List<TableFieldSchema> columns = new ArrayList<>();
        TableFieldSchema c1 = new TableFieldSchema();
        c1.setFieldName("test_column");
        c1.setTypeCategory("bigint");
        columns.add(c1);
        schema.setFields(columns);
        table.setTableSchema(schema);

        GetTableResponse response = catalogClient.updateTable(table);
        System.out.println(response.getBody());
    }
}