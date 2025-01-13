
import com.aliyun.odps.catalog.models.Table;
import com.aliyun.odps.catalog.models.TableFieldSchema;
import com.aliyun.odps.models.Config;
import com.google.common.collect.ImmutableList;

public class TableTest {
    public static void main(String[] args) throws Exception {
        Config config = new Config();
        config.setEndpoint("");
        config.setAccessKeyId("");
        config.setAccessKeySecret("");

        com.aliyun.odps.catalog.Client catalogClient = new com.aliyun.odps.catalog.Client(config);
        Table table = new Table();
        table.projectId = "project";
        table.schemaName = "default";
        table.tableName = "test";

        TableFieldSchema c0 = new TableFieldSchema();
        c0.fieldName = "c0";
        c0.typeCategory = "STRING";
        TableFieldSchema tableSchema = new TableFieldSchema();
        tableSchema.fields = ImmutableList.of(c0);
        table.tableSchema = tableSchema;
        table.type = "TABLE";
        Table created = catalogClient.createTable(table);

        System.out.println(created.getName());

        TableFieldSchema c1 = new TableFieldSchema();
        c1.description = "col comments";
        c1.fieldName = "c1";
        c1.mode = "NULLABLE";
        c1.typeCategory = "BIGINT";
        created.getTableSchema().getFields().add(c1);

        Table afterUpdate = catalogClient.updateTable(created);
        afterUpdate.getTableSchema().getFields().forEach(f -> {
            System.out.println(f.fieldName);
        });
    }
}