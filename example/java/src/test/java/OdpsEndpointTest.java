/*
DISCLAIMER:

Demonstrates initializing the catalog client with only the ODPS endpoint.
The catalog endpoint is resolved lazily via the routing API on first request.

Reads credentials and ODPS endpoint from environment variables:
  ALIBABA_CLOUD_ACCESS_KEY_ID
  ALIBABA_CLOUD_ACCESS_KEY_SECRET
  odps_endpoint    (e.g. http://service.cn-shanghai.maxcompute.aliyun.com/api)
  PROJECT
*/
import com.aliyun.odps.catalog.Client;
import com.aliyun.odps.catalog.models.ListProjectsResponse;
import com.aliyun.odps.catalog.models.Table;
import com.aliyun.odps.models.Config;
import org.junit.Assume;
import org.junit.Test;

import java.net.URL;

import static org.junit.Assert.*;

public class OdpsEndpointTest {

    @Test
    public void testLazyEndpointResolution() throws Exception {
        String akId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID");
        String akSecret = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET");
        String rawOdps = System.getenv("odps_endpoint");
        String projectId = System.getenv("PROJECT");
        String tableName = System.getenv("CATALOG_TABLE_NAME");
        if (tableName == null || tableName.isEmpty()) {
            tableName = "test_table";
        }

        Assume.assumeTrue(
            "set ALIBABA_CLOUD_ACCESS_KEY_ID / ALIBABA_CLOUD_ACCESS_KEY_SECRET / odps_endpoint / PROJECT to run",
            akId != null && akSecret != null && rawOdps != null && projectId != null
        );

        String normalized = rawOdps.contains("://") ? rawOdps : "http://" + rawOdps;
        URL url = new URL(normalized);
        String protocol = url.getProtocol();
        String host = url.getHost();
        System.out.printf("odps endpoint: protocol=%s host=%s%n", protocol, host);

        Config config = new Config();
        config.setOdpsEndpoint(host);
        config.setProtocol(protocol);
        config.setAccessKeyId(akId);
        config.setAccessKeySecret(akSecret);

        Client client = new Client(config);

        assertTrue("endpoint should be empty before first call",
            client._endpoint == null || client._endpoint.isEmpty());
        System.out.printf("endpoint before call: \"%s\"%n", client._endpoint == null ? "" : client._endpoint);

        ListProjectsResponse listResp = client.listProjects(1, null);
        assertNotNull("ListProjects should succeed after lazy endpoint resolution", listResp);

        assertNotNull("endpoint should be populated after first call", client._endpoint);
        assertFalse("endpoint should not be empty", client._endpoint.isEmpty());
        System.out.printf("endpoint after call:  \"%s\"%n", client._endpoint);

        Table table = new Table();
        table.setProjectId(projectId);
        table.setTableName(tableName);
        try {
            Table got = client.getTable(table);
            System.out.printf("got table name: %s%n", got.getTableName());
        } catch (Exception e) {
            System.out.printf("GetTable(%s/%s) returned: %s%n", projectId, tableName, e.getMessage());
        }
    }
}
