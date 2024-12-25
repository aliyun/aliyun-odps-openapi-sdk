package tech.dingxin;

import com.aliyun.odps.catalog.models.PolicyTag;
import com.aliyun.odps.catalog.models.Table;
import com.aliyun.odps.catalog.models.TableFieldSchema;
import com.aliyun.odps.models.Config;

import java.util.Collections;

/**
 * @author dingxin (zhangdingxin.zdx@alibaba-inc.com)
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Config config = new Config();
        // config.setEndpoint("11.158.225.37:12370");
        config.setEndpoint("11.158.243.229:12330");
        config.setAccessKeyId("");
        config.setAccessKeySecret("");

        com.aliyun.odps.catalog.Client catalogClient = new com.aliyun.odps.catalog.Client(config);

        Table table = new Table();
        table.projectId = "odps_test_tunnel_project_orc";
        // table.schemaName = "default";
        table.tableName = "test";
        //catalogClient.deleteTable(table);

        table.description = "For test.";

        TableFieldSchema c0 = new TableFieldSchema();
        c0.description = "col comments";
        c0.fieldName = "c0";
        c0.mode = "NULLABLE";
        PolicyTag policyTag = new PolicyTag();
        policyTag.names = Collections.singletonList("namespaces/123/taxonomies/456/policyTags/789");
        c0.policyTags = policyTag;
        c0.typeCategory = "STRING";

        TableFieldSchema tableSchema = new TableFieldSchema();
        tableSchema.fields = Collections.singletonList(c0);

        table.tableSchema = tableSchema;
        table.type = "TABLE";

        catalogClient.createTable(table);
    }
}