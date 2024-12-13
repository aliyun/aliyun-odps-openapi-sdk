package tech.dingxin;

import com.aliyun.odps.catalog.models.GetTableRequest;
import com.aliyun.odps.catalog.models.GetTableResponse;
import com.aliyun.odps.models.Config;

/**
 * @author dingxin (zhangdingxin.zdx@alibaba-inc.com)
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Config config = new Config();
        config.setEndpoint("100.69.248.78:8002");
        config.setAccessKeyId("");
        config.setAccessKeySecret("");
        config.setSuffix("odps_dailyrunnew");

        com.aliyun.odps.catalog.Client catalogClient = new com.aliyun.odps.catalog.Client(config);

        GetTableRequest request = new GetTableRequest();
        request.setProjectName("dingxin_volume");
        request.setTableName("auto_pt");

        GetTableResponse response = catalogClient.getTable(request);
        System.out.println(response.getBody());
    }
}