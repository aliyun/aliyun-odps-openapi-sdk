/*
DISCLAIMER:

This code is provided as an example only to demonstrate the usage of MaxCompute Catalog API.
It is not production-ready and comes with no guarantees of correctness or completeness.

Example usage:
    Config config = new Config();
    config.setEndpoint(endpoint);
    config.setAccessKeyId(accessKeyId);
    config.setAccessKeySecret(accessKeySecret);

    Client catalogClient = new Client(config);

    Table table = new Table()
        .setProjectId(projectId)
        .setSchemaName("default")
        .setTableName("test_table")
        .setTableSchema(tableSchema);

    catalogClient.createTable(table);

Please ensure proper testing and validation before using in production environments.
*/
import com.aliyun.odps.catalog.models.ExpirationOptions;
import com.aliyun.odps.catalog.models.Table;
import com.aliyun.odps.catalog.models.TableFieldSchema;
import com.aliyun.odps.models.Config;
import com.aliyun.teautil.Common;
import com.google.common.collect.ImmutableList;
import org.apache.commons.lang.StringUtils;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class TableTest {
    private static Logger logger = LoggerFactory.getLogger(TableTest.class);
    private static String projectId;
    private static com.aliyun.odps.catalog.Client catalogClient;
    private static Table sBasicTable;
    private static Table mTable;

    @BeforeClass
    public static void SetUp() throws Exception {
        Config config = new Config();
        config.setEndpoint("");
        config.setAccessKeyId("");
        config.setAccessKeySecret("");
        catalogClient = new com.aliyun.odps.catalog.Client(config);

        // create table before update
        String sTableName = "test_table";

        TableFieldSchema c0 =
                new TableFieldSchema().setFieldName("col0").setMode("NULLABLE").setTypeCategory("INT").setDescription(
                        "InitCol0");
        TableFieldSchema c1 = new TableFieldSchema().setFieldName("col1").setMode("REQUIRED").setTypeCategory("INT")
                .setDescription("InitCol1");
        TableFieldSchema c2 =
                new TableFieldSchema().setFieldName("col2").setTypeCategory("STRING").setMode("NULLABLE")
                        .setDescription(
                                "Init Update Table");
        TableFieldSchema c3 = new TableFieldSchema().setFieldName("InitNestedCol").setTypeCategory("STRUCT")
                .setMode("REQUIRED").setFields(ImmutableList.of(
                        new TableFieldSchema().setFieldName("InitNestedSubCol1").setTypeCategory("INT"),
                        new TableFieldSchema().setFieldName("InitNestedSubCol2").setTypeCategory("INT"),
                        new TableFieldSchema().setFieldName("InitNestedSubCol3").setTypeCategory("STRING")
                ));
        TableFieldSchema tableBasicSchema = new TableFieldSchema().setMode("NULLABLE").setFields(Arrays.asList(c0, c1
                , c2, c3));

        Table basicTable = new Table().setProjectId(projectId).setSchemaName("default").setType(
                "TABLE").setTableName(sTableName).setTableSchema(tableBasicSchema).setDescription("InitDescription");
        sBasicTable.setTableName(sTableName);

        try {
            mTable = catalogClient.createTable(basicTable);
            logger.info("create table succ.");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Table already exist"));
            logger.info("create table failed, cause: {}", e.getMessage());
            mTable = catalogClient.getTable(basicTable);
        }

        logger.info("\n------------SetUp End ----------\n");
    }

    @Test
    public void TestBasicUpdate() throws Exception {
        String updatedDescription = "Basic Update Table Description.";
        mTable.setDescription(updatedDescription);
        Table updated = catalogClient.updateTable(mTable);
        Assert.assertTrue(StringUtils.equals(updated.getDescription(), updatedDescription));

        mTable = catalogClient.getTable(mTable);
        Assert.assertTrue(StringUtils.equals(updated.getDescription(), updatedDescription));
    }


    @Test
    public void TestAppendColumn() throws Exception {
        // Append Nullable Column
        TableFieldSchema c0 = getBasicColumn("Append1", "AppendTable1");
        TableFieldSchema c1 = getBasicColumn("Append2", "AppendTable2");
        mTable.tableSchema.fields.addAll(ImmutableList.of(c0, c1));
        Table updated = catalogClient.updateTable(mTable);

        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "AppendTable1"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "AppendTable2"));

        // Append Duplicated Column:
        c1.setDescription("Duplicated Col1");
        updated.tableSchema.fields.add(c1);
        try {
            catalogClient.updateTable(updated);
            Assert.fail("Append Duplicated Column Cannot Succ.");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Duplicated field name"));
        }
        updated.tableSchema.fields.remove(c1);

        // Append Required Column
        TableFieldSchema c2 = getRequiredColumn("AppendRequired", "AppendRequiredCol");
        updated.tableSchema.fields.add(c2);
        try {
            catalogClient.updateTable(updated);
            Assert.fail("Append Required Column Cannot Succ.");
        } catch (Exception e) {
            // ZHIYIN TODO: check
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Adding REQUIRED mode column is not supported"));
        }

    }

    @Test
    public void TestAppendNestedColumn() throws Exception {
        mTable.tableSchema.fields.get(3).fields.add(
                new TableFieldSchema().setFieldName("appendinitnestedsubcol4").setTypeCategory("STRING")
        );

        // Append Nested Column
        TableFieldSchema nestedSubCol =
                new TableFieldSchema().setFieldName("nestedcolnested").setTypeCategory("STRUCT").setFields(
                        ImmutableList.of(
                                new TableFieldSchema().setFieldName("nestednestedcol1").setTypeCategory("STRING")
                        ));
        TableFieldSchema nestedColumn = new TableFieldSchema().setFieldName("AppendNestedCol").setTypeCategory("STRUCT")
                .setMode("NULLABLE").setFields(ImmutableList.of(
                        new TableFieldSchema().setFieldName("nestedcolcol1").setTypeCategory("STRING")
                        , new TableFieldSchema().setFieldName("nestedcolcol2").setTypeCategory("INT")
                        , new TableFieldSchema().setFieldName("nestedcolcol3").setTypeCategory("STRING")
                        , nestedSubCol));
        TableFieldSchema c0 = getBasicColumn("AppendSimpleCol", "AppendSimpleColumn");
        mTable.tableSchema.fields.addAll(ImmutableList.of(c0, nestedColumn));

        Table updated = catalogClient.updateTable(mTable);

        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "nestedcolnested"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "nestednestedcol1"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "nestedcolcol1"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "nestedcolcol2"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "nestedcolcol3"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "AppendSimpleCol"));
    }

    @Test
    public void TestNestedDuplicatedColumn() throws Exception {
        TableFieldSchema c1 = getBasicColumn("InitNestedCol", "SameNameButDiffType");
        mTable.tableSchema.fields.add(c1);
        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Append Duplicated Column.");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Duplicated field name"));
        }
        mTable.tableSchema.fields.remove(c1);

        // Append Duplicated Nested Column
        TableFieldSchema c2 = getBasicColumn("InitNestedSubCol2", "SameNameButNotSameLevel");
        TableFieldSchema c3 = new TableFieldSchema().setFieldName("DupNestedCol").setTypeCategory("STRUCT").setMode(
                "NULLABLE").setDescription("Same nested sub col").setFields(
                ImmutableList.of(
                        new TableFieldSchema().setFieldName("InitNestedSubCol1").setTypeCategory("INT"),
                        new TableFieldSchema().setFieldName("InitNestedSubCol2").setTypeCategory("INT"),
                        new TableFieldSchema().setFieldName("InitNestedSubCol3").setTypeCategory("STRING")
                ));

        mTable.tableSchema.fields.addAll(ImmutableList.of(c2, c3));
        mTable = catalogClient.updateTable(mTable);

        Assert.assertTrue(
                StringUtils.contains(Common.toJSONString(mTable.tableSchema.fields), "SameNameButNotSameLevel"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(mTable.tableSchema.fields), "Same nested sub col"));
        Assert.assertTrue((StringUtils.countMatches(Common.toJSONString(mTable.tableSchema.fields),
                "initnestedsubcol2") == 5));
        Assert.assertTrue((StringUtils.countMatches(Common.toJSONString(mTable.tableSchema.fields),
                "initnestedsubcol1") == 4));
        Assert.assertTrue((StringUtils.countMatches(Common.toJSONString(mTable.tableSchema.fields),
                "initnestedsubcol3") == 4));
    }

    @Test
    public void TestSwapColumn() throws Exception {
        Collections.swap(mTable.tableSchema.fields, 0, 1);
        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Change Column Order");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Not supported column operation"));
        }

        Collections.swap(mTable.tableSchema.fields, 0, 1);
        TableFieldSchema c0 = getBasicColumn("insertCol1", "insertCol");

        mTable.tableSchema.fields.add(0, c0);
        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Insert Table");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Not supported column operation"));
        }
        mTable.tableSchema.fields.remove(c0);

        mTable = catalogClient.updateTable(mTable);
        Collections.swap(mTable.tableSchema.fields.get(mTable.tableSchema.fields.size() - 1).fields, 0, 1);

        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Swap Nested Column");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Struct child name not match"));
        }

    }

    @Test
    public void TestOldEtag() throws Exception {
        TableFieldSchema c0 = getBasicColumn("new1", "InitCol0");
        TableFieldSchema c1 = getBasicColumn("new2", "InitCol1");

        mTable.tableSchema.fields.add(c0);
        catalogClient.updateTable(mTable);
        mTable.tableSchema.fields.add(0, c1);

        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Update With Old eTag");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Conflict with other alter table operation"));
        }

        mTable.etag = "InvalidEtag";
        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Update With Wrong eTag");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Invalid etag"));
        }
    }

    @Test
    public void TestInvalidGet() throws Exception {
        TableFieldSchema c0 = getBasicColumn("notExistCol", "notExistCol");
        mTable.tableSchema.fields.add(c0);
        mTable.etag = "InvalidEtag";

        mTable = catalogClient.getTable(mTable);
        Assert.assertFalse(StringUtils.contains(Common.toJSONString(mTable.tableSchema.fields), "notExistCol"));
    }

    @Test
    public void TestOldEtagGet() throws Exception {
        String oldEtag = mTable.etag;
        mTable.tableSchema.fields.add(getBasicColumn("newEtag", "newEtag"));
        mTable = catalogClient.updateTable(mTable);

        mTable.etag = oldEtag;
        mTable = catalogClient.getTable(mTable);
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(mTable.tableSchema.fields), "newEtag"));
    }

    @Test
    public void TestUpdateComments() throws Exception {
        mTable.description = "Updated Table description";
        mTable.tableSchema.fields.get(0).description = "Update col0";
        mTable.tableSchema.fields.get(1).description = "Update col1";
        mTable.tableSchema.fields.get(3).description = "Update nested col1 description";
        catalogClient.updateTable(mTable);
        Table updated = catalogClient.getTable(sBasicTable);
        Assert.assertTrue(StringUtils.contains(updated.description, "Updated Table description"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields), "Update col0"));
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(updated.tableSchema.fields),
                "Update nested col1 description"));
    }

    @Test
    public void TestUpdateColumnMode() throws Exception {
        // required to nullable, success
        mTable.tableSchema.fields.get(1).setMode("NULLABLE");
        catalogClient.updateTable(mTable);
        mTable = catalogClient.getTable(sBasicTable);
        Assert.assertEquals(mTable.tableSchema.fields.get(1).getMode(), "NULLABLE");

        // nullable to required, failed
        mTable.tableSchema.fields.get(1).setMode("REQUIRED");
        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Update NULLABLE COLUMN TO REQUIRED");
        } catch (Exception e) {
            Assert.assertTrue(
                    StringUtils.contains(e.getMessage(), "Cannot change column mode from NULLABLE to REQUIRED"));
        }
        mTable.tableSchema.fields.get(1).setMode("NULLABLE");

        // cannot set nested column mode
        mTable.tableSchema.fields.get(3).fields.get(0).setMode("REQUIRED");
        try {
            mTable = catalogClient.updateTable(mTable);
            Assert.fail("Cannot Set Mode for Nested Column");
        } catch (Exception e) {
            Assert.assertTrue(
                    StringUtils.contains(e.getMessage(), "Field mode can only be specified for top level fields"));
        }
    }

    @Test
    public void TestDeleteColumn() throws Exception {
        mTable.tableSchema.fields.remove(0);
        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Delete Column");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Delete column is not supported"));
        }

        TableFieldSchema c0 = getBasicColumn("col0", "UpdateCol0");
        mTable.tableSchema.fields.add(0, c0);
        mTable = catalogClient.updateTable(mTable);
        Assert.assertTrue(StringUtils.contains(Common.toJSONString(mTable.tableSchema.fields), "UpdateCol0"));

        mTable.tableSchema.fields.get(0).setTypeCategory("STRING");
        try {
            catalogClient.updateTable(mTable);
            Assert.fail("Cannot Update Column Type");
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Not support change column type"));
        }
    }

    @Test
    public void TestDeleteNestedColumn() throws Exception {
        mTable.tableSchema.fields.get(3).fields.get(2).setFieldName("updateNestedCol1");
        mTable.tableSchema.fields.get(3).fields.add(
                new TableFieldSchema().setFieldName("updatenestedcol4").setTypeCategory("INT")
        );

        try {
            catalogClient.updateTable(mTable);
        } catch (Exception e) {
            Assert.assertTrue(StringUtils.contains(e.getMessage(), "Struct child name not match"));
        }
    }

    @Test
    public void TestUpdateTableWithAllKindsCategory() throws Exception {
        List<String> types = Arrays.asList(
                "TINYINT",
                "SMALLINT",
                "BIGINT",
                "INT",
                "BINARY",
                "FLOAT",
                "DOUBLE",
                "DECIMAL",
                "VARCHAR",
                "CHAR",
                "STRING",
                "DATE",
                "DATETIME",
                "TIMESTAMP",
                "TIMESTAMP_NTZ",
                "BOOLEAN",
                "ARRAY",
                "MAP");
        for (String t : types) {
            TableFieldSchema c = new TableFieldSchema().setTypeCategory(t).setFieldName(t);
            if (StringUtils.equals(t, "DECIMAL")) {
                c.setPrecision("38");
                c.setScale("18");
            }
            if (StringUtils.equals(t, "ARRAY")) {
                c.fields = Collections.singletonList(new TableFieldSchema().setFieldName("element").setTypeCategory(
                        "STRING"));
            }
            if (StringUtils.equals(t, "MAP")) {
                c.fields = Arrays.asList(
                        new TableFieldSchema().setFieldName("key").setTypeCategory(
                                "STRING"),
                        new TableFieldSchema().setFieldName("value").setTypeCategory(
                                "STRING")
                );

            }
            if (StringUtils.equals(t, "VARCHAR") || StringUtils.equals(t, "CHAR")) {
                c.setMaxLength("100");
            }
            mTable.tableSchema.fields.add(c);
            mTable = catalogClient.updateTable(mTable);
        }

        mTable = catalogClient.getTable(sBasicTable);

        String fieldsJson = Common.toJSONString(mTable.tableSchema.fields);
        for (String t : types) {
            Assert.assertTrue(StringUtils.contains(fieldsJson, t));
        }
    }

    @Test
    public void TestTableLifeCycle() throws Exception {
        Integer expected = 1;
        ExpirationOptions exp = new ExpirationOptions().setExpirationDays(expected);
        mTable.setExpirationOptions(exp);
        mTable = catalogClient.updateTable(mTable);

        mTable = catalogClient.getTable(mTable);
        Assert.assertEquals(expected, mTable.getExpirationOptions().getExpirationDays());
    }

    public static TableFieldSchema getBasicColumn(String name, String desc){
        return new TableFieldSchema().setFieldName(name).setMode("NULLABLE").setTypeCategory("INT").setDescription(
                desc);
    }

    public static TableFieldSchema getRequiredColumn(String name, String desc){
        return new TableFieldSchema().setFieldName(name).setMode("REQUIRED").setTypeCategory("INT").setDescription(desc);
    }
}
