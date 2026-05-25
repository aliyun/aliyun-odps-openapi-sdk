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
package _go

import (
	"fmt"
	"net/url"
	"os"
	"strings"
	"testing"

	"github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/client"
	openapi "github.com/aliyun/aliyun-odps-openapi-sdk/common/go/client"
	"github.com/stretchr/testify/assert"
)

// splitOdpsEndpoint parses values like
//   http://service.cn-shanghai.maxcompute.aliyun.com/api
// into ("http", "service.cn-shanghai.maxcompute.aliyun.com"). The trailing
// "/api" path is the standard ODPS prefix and is added by the SDK internally.
func splitOdpsEndpoint(raw string) (protocol, host string, err error) {
	if !strings.Contains(raw, "://") {
		raw = "http://" + raw
	}
	u, err := url.Parse(raw)
	if err != nil {
		return "", "", err
	}
	return u.Scheme, u.Host, nil
}

func TestGetTableWithOdpsEndpoint(t *testing.T) {
	akId := os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")
	akSecret := os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
	rawOdps := os.Getenv("odps_endpoint")
	projectId := os.Getenv("PROJECT")
	tableName := os.Getenv("CATALOG_TABLE_NAME")
	if tableName == "" {
		tableName = "test_table"
	}

	if akId == "" || akSecret == "" || rawOdps == "" || projectId == "" {
		t.Skip("set ALIBABA_CLOUD_ACCESS_KEY_ID / ALIBABA_CLOUD_ACCESS_KEY_SECRET / odps_endpoint / PROJECT to run this test")
	}

	protocol, host, err := splitOdpsEndpoint(rawOdps)
	assert.NoError(t, err)
	fmt.Printf("odps endpoint: protocol=%s host=%s\n", protocol, host)

	config := new(openapi.Config).
		SetOdpsEndpoint(host).
		SetProtocol(protocol).
		SetAccessKeyId(akId).
		SetAccessKeySecret(akSecret)

	c, err := client.NewClient(config)
	assert.NoError(t, err)

	// Before any request, Endpoint is empty — routing has not been called yet.
	assert.True(t, c.Endpoint == nil || *c.Endpoint == "", "endpoint should be empty before first call")
	fmt.Printf("endpoint before call: %q\n", strDeref(c.Endpoint))

	// First real call — the SDK should call the routing API to fill in Endpoint,
	// then send the actual request to the resolved catalog host.
	pageSize := 1
	listResp, err := c.ListProjects(&pageSize, nil)
	assert.NoError(t, err, "ListProjects should succeed after lazy endpoint resolution")
	assert.NotNil(t, listResp)

	assert.NotNil(t, c.Endpoint, "endpoint should be populated after first call")
	assert.NotEmpty(t, strDeref(c.Endpoint))
	fmt.Printf("endpoint after call:  %q\n", strDeref(c.Endpoint))

	// Optional: try GetTable for the configured project. Failures here are
	// environment data, not SDK bugs, so just log them.
	table := &client.Table{}
	table.SetProjectId(projectId)
	table.SetTableName(tableName)
	got, err := c.GetTable(table)
	if err != nil {
		fmt.Printf("GetTable(%s/%s) returned: %v\n", projectId, tableName, err)
	} else {
		fmt.Printf("got table name: %s\n", strDeref(got.TableName))
	}
}

func strDeref(s *string) string {
	if s == nil {
		return ""
	}
	return *s
}
