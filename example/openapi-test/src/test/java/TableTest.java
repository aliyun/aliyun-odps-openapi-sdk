import com.aliyun.credentials.Client;
import com.aliyun.odps.catalog.models.PolicyTag;
import com.aliyun.odps.catalog.models.Table;
import com.aliyun.odps.catalog.models.TableFieldSchema;
import com.aliyun.odps.models.Config;
import com.google.common.collect.ImmutableList;

import java.util.Collections;

/**
 * @author dingxin (zhangdingxin.zdx@alibaba-inc.com)
 */
public class TableTest {
    public static void main(String[] args) throws Exception {
        Config config = new Config();
        //config.setEndpoint("11.158.225.37:12370");
        config.setEndpoint("11.158.243.229:12330");
        config.setAccessKeyId("");
        config.setAccessKeySecret("=");

        com.aliyun.credentials.models.Config credentialConfig = new com.aliyun.credentials.models.Config();
        Client client = new Client(credentialConfig);
        credentialConfig.setRoleArn("xxx");
        config.setCredential(client);

        com.aliyun.odps.catalog.Client catalogClient = new com.aliyun.odps.catalog.Client(config);
        Table table = new Table();
        table.projectId = "odps_test_tunnel_project_orc";
        table.schemaName = "default";
        table.tableName = "dingxin_test_2";

       catalogClient.deleteTable(table); // 500 error if table not exist

        table.description = "For test hh.";
        TableFieldSchema c0 = new TableFieldSchema();
        c0.description = "col comments";
        c0.fieldName = "c0";
        c0.mode = "NULLABLE";
        PolicyTag policyTag = new PolicyTag();
        policyTag.names = Collections.singletonList("namespaces/123/taxonomies/456/policyTags/789");
        c0.policyTags = policyTag;
        c0.typeCategory = "STRING";
        TableFieldSchema tableSchema = new TableFieldSchema();
        tableSchema.fields = ImmutableList.of(c0);
        table.tableSchema = tableSchema;
        table.type = "TABLE";
        Table created = catalogClient.createTable(table);

        TableFieldSchema c1 = new TableFieldSchema();
        c1.description = "col comments";
        c1.fieldName = "c1";
        c1.mode = "NULLABLE";
        c1.typeCategory = "BIGINT";
        created.getTableSchema().getFields().add(c1);

        Table afterUpdate = catalogClient.updateTable(created);
        // sometimes throw 	"Message": "ODPS-0110061: Failed to run ddltask - Clustering type cannot be changed"

        afterUpdate.getTableSchema().getFields().forEach(f ->{
                System.out.println(f.fieldName);
        });
    }
}