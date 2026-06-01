/*
Comprehensive integration tests for Catalog API.
Covers all GET (body-less) operations to verify the request/requestVoid refactoring.

Reads credentials from environment variables:
  ALIBABA_CLOUD_ACCESS_KEY_ID
  ALIBABA_CLOUD_ACCESS_KEY_SECRET
  odps_endpoint    (e.g. http://service.cn-shanghai.maxcompute.aliyun.com/api)
  PROJECT          (e.g. dingxin)
*/
import com.aliyun.odps.catalog.Client;
import com.aliyun.odps.catalog.models.*;
import com.aliyun.odps.models.Config;
import org.junit.Assume;
import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;

import java.net.URL;
import java.util.List;

import static org.junit.Assert.*;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class CatalogApiTest {

    private static Client client;
    private static String projectId;

    @BeforeClass
    public static void setup() throws Exception {
        String akId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID");
        String akSecret = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET");
        String rawOdps = System.getenv("odps_endpoint");
        projectId = System.getenv("PROJECT");
        if (projectId == null || projectId.isEmpty()) {
            projectId = "dingxin";
        }

        Assume.assumeTrue(
            "set ALIBABA_CLOUD_ACCESS_KEY_ID / ALIBABA_CLOUD_ACCESS_KEY_SECRET / odps_endpoint to run",
            akId != null && akSecret != null && rawOdps != null
        );

        String normalized = rawOdps.contains("://") ? rawOdps : "http://" + rawOdps;
        URL url = new URL(normalized);

        Config config = new Config();
        config.setOdpsEndpoint(url.getHost());
        config.setProtocol(url.getProtocol());
        config.setAccessKeyId(akId);
        config.setAccessKeySecret(akSecret);

        client = new Client(config);
    }

    @Test
    public void test01_listProjects() throws Exception {
        ListProjectsResponse resp = client.listProjects(2, null);
        assertNotNull(resp);
        assertNotNull(resp.getProjects());
        assertTrue(resp.getProjects().size() > 0);
        System.out.printf("listProjects: got %d projects, first=%s%n",
            resp.getProjects().size(), resp.getProjects().get(0).getProjectId());

        // Test pagination
        if (resp.getNextPageToken() != null) {
            ListProjectsResponse page2 = client.listProjects(2, resp.getNextPageToken());
            assertNotNull(page2);
            System.out.printf("listProjects page2: got %d projects%n", page2.getProjects().size());
        }
    }

    @Test
    public void test02_getProject() throws Exception {
        Project proj = client.getProject(projectId, null);
        assertNotNull(proj);
        assertEquals(projectId, proj.getProjectId());
        assertNotNull(proj.getOwner());
        System.out.printf("getProject: id=%s, owner=%s, region=%s%n",
            proj.getProjectId(), proj.getOwner(), proj.getRegion());

        // Test with FULL view
        Project projFull = client.getProject(projectId, "FULL");
        assertNotNull(projFull);
        System.out.printf("getProject FULL: schema_enabled=%s%n", projFull.getSchemaEnabled());
    }

    @Test
    public void test03_listSchemas() throws Exception {
        ListSchemasResponse resp = client.listSchemas(projectId, 5, null);
        assertNotNull(resp);
        assertNotNull(resp.getSchemas());
        assertTrue(resp.getSchemas().size() > 0);
        System.out.printf("listSchemas: got %d schemas%n", resp.getSchemas().size());
        for (Schema s : resp.getSchemas()) {
            System.out.printf("  %s (type=%s)%n", s.getSchemaName(), s.getType());
        }
    }

    @Test
    public void test04_getSchema() throws Exception {
        Schema schema = client.getSchema(projectId, "default");
        assertNotNull(schema);
        assertEquals("default", schema.getSchemaName());
        System.out.printf("getSchema: name=%s, type=%s, owner=%s%n",
            schema.getSchemaName(), schema.getType(), schema.getOwner());
    }

    @Test
    public void test05_listTables() throws Exception {
        ListTablesResponse resp = client.listTables(projectId, "default", 3, null, null, null);
        assertNotNull(resp);
        assertNotNull(resp.getTables());
        assertTrue(resp.getTables().size() > 0);
        System.out.printf("listTables: got %d tables%n", resp.getTables().size());
        for (Table t : resp.getTables()) {
            System.out.printf("  %s (type=%s)%n", t.getTableName(), t.getType());
        }

        // Test pagination
        if (resp.getNextPageToken() != null) {
            ListTablesResponse page2 = client.listTables(projectId, "default", 3, resp.getNextPageToken(), null, null);
            assertNotNull(page2);
            System.out.printf("listTables page2: got %d tables%n", page2.getTables().size());
        }
    }

    @Test
    public void test06_listTablesWithView() throws Exception {
        ListTablesResponse resp = client.listTables(projectId, "default", 2, null, "FULL", null);
        assertNotNull(resp);
        assertNotNull(resp.getTables());
        Table t = resp.getTables().get(0);
        assertNotNull(t.getCreateTime());
        System.out.printf("listTables FULL: %s, create_time=%s, storage=%s%n",
            t.getTableName(), t.getCreateTime(), t.getNumTotalStorageBytes());
    }

    @Test
    public void test07_getTable() throws Exception {
        // First get a table name from list
        ListTablesResponse listResp = client.listTables(projectId, "default", 1, null, null, null);
        String tableName = listResp.getTables().get(0).getTableName();

        Table req = new Table();
        req.setProjectId(projectId);
        req.setSchemaName("default");
        req.setTableName(tableName);

        Table got = client.getTable(req);
        assertNotNull(got);
        assertEquals(tableName, got.getTableName());
        assertEquals(projectId, got.getProjectId());
        System.out.printf("getTable: name=%s, type=%s%n", got.getTableName(), got.getType());
    }

    @Test
    public void test08_listPartitions() throws Exception {
        // Find a partitioned table or skip
        ListTablesResponse listResp = client.listTables(projectId, "default", 50, null, "FULL", null);
        String partitionedTable = null;
        for (Table t : listResp.getTables()) {
            if (t.getPartitionDefinition() != null) {
                partitionedTable = t.getTableName();
                break;
            }
        }

        if (partitionedTable == null) {
            System.out.println("listPartitions: no partitioned table found, skipping");
            return;
        }

        ListPartitionsResponse resp = client.listPartitions(
            projectId, "default", partitionedTable, 5, null, null, null);
        assertNotNull(resp);
        int count = resp.getPartitions() != null ? resp.getPartitions().size() : 0;
        System.out.printf("listPartitions(%s): got %d partitions%n", partitionedTable, count);
        if (resp.getPartitions() != null) {
            for (Partition p : resp.getPartitions()) {
                System.out.printf("  %s%n", p.getSpec());
            }
        }
    }

    @Test
    public void test09_getTablePolicy() throws Exception {
        // Body-less POST operation
        ListTablesResponse listResp = client.listTables(projectId, "default", 1, null, null, null);
        String tableName = listResp.getTables().get(0).getTableName();

        Table req = new Table();
        req.setProjectId(projectId);
        req.setSchemaName("default");
        req.setTableName(tableName);

        try {
            Policy policy = client.getTablePolicy(req);
            assertNotNull(policy);
            int bindings = policy.getBindings() != null ? policy.getBindings().size() : 0;
            System.out.printf("getTablePolicy: etag=%s, bindings=%d%n", policy.getEtag(), bindings);
        } catch (Exception e) {
            if (e.getMessage() != null && e.getMessage().contains("403")) {
                System.out.printf("getTablePolicy: no permission, skipping%n");
            } else {
                throw e;
            }
        }
    }

    @Test
    public void test10_getSchemaPolicy() throws Exception {
        // Another body-less POST
        try {
            Policy policy = client.getSchemaPolicy(projectId, "default");
            assertNotNull(policy);
            int bindings = policy.getBindings() != null ? policy.getBindings().size() : 0;
            System.out.printf("getSchemaPolicy: etag=%s, bindings=%d%n", policy.getEtag(), bindings);
        } catch (Exception e) {
            if (e.getMessage() != null && e.getMessage().contains("403")) {
                System.out.printf("getSchemaPolicy: no permission, skipping%n");
            } else {
                throw e;
            }
        }
    }

    @Test
    public void test11_search() throws Exception {
        // Body-less POST search operation
        try {
            SearchResponse resp = client.search(projectId, "type=TABLE", 3, null, null);
            assertNotNull(resp);
            int count = resp.getEntries() != null ? resp.getEntries().size() : 0;
            System.out.printf("search: got %d entries%n", count);
            if (resp.getEntries() != null) {
                for (SearchResultEntry e : resp.getEntries()) {
                    System.out.printf("  %s (%s)%n", e.getDisplayName(), e.getType());
                }
            }
        } catch (Exception e) {
            if (e.getMessage() != null && (e.getMessage().contains("403") || e.getMessage().contains("400"))) {
                System.out.printf("search: not available, skipping: %s%n",
                    e.getMessage().substring(0, Math.min(100, e.getMessage().length())));
            } else {
                throw e;
            }
        }
    }
}
