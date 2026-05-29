import com.aliyun.odps.catalog.Client;
import com.aliyun.odps.models.Config;

/**
 * Examples of initializing the Catalog API client.
 *
 * error 'invalid character '<' looking for beginning of value' may because of wrong endpoint or wrong proxy configured
 * endpoint should be like 'catalogapi.ap-southeast-5.maxcompute.aliyun.com'
 */
public class HowToInitClient {

    /**
     * Initialize with catalog endpoint directly.
     */
    static void way1() throws Exception {
        String endpoint = "";
        String accessKeyId = "";
        String accessKeySecret = "";

        Config config = new Config();
        config.setEndpoint(endpoint);
        config.setAccessKeyId(accessKeyId);
        config.setAccessKeySecret(accessKeySecret);

        Client client = new Client(config);
        System.out.println(client._endpoint);
    }

    /**
     * Initialize with ODPS endpoint only.
     * The catalog API endpoint is resolved lazily on the first request via the routing API.
     * odpsEndpoint should be like 'service.cn-shanghai.maxcompute.aliyun.com'
     */
    static void way2() throws Exception {
        String odpsEndpoint = "";
        String accessKeyId = "";
        String accessKeySecret = "";

        Config config = new Config();
        config.setOdpsEndpoint(odpsEndpoint);
        config.setProtocol("http");
        config.setAccessKeyId(accessKeyId);
        config.setAccessKeySecret(accessKeySecret);

        Client client = new Client(config);
        // Endpoint is empty until the first API call triggers routing resolution.
        System.out.println(client._endpoint);
    }

    /**
     * Initialize with STS token for temporary credentials.
     */
    static void way3() throws Exception {
        String endpoint = "";
        String accessKeyId = "";
        String accessKeySecret = "";
        String securityToken = "";

        Config config = new Config();
        config.setEndpoint(endpoint);
        config.setAccessKeyId(accessKeyId);
        config.setAccessKeySecret(accessKeySecret);
        config.setSecurityToken(securityToken);

        Client client = new Client(config);
        System.out.println(client._endpoint);
    }
}
