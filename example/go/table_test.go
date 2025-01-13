package _go

import (
	"log"
	"testing"

	"github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/client"
	openapi "github.com/aliyun/aliyun-odps-openapi-sdk/common/go/client"
)

func Test_GetTable(t *testing.T) {
	var config openapi.Config
	config.SetAccessKeyId("")
	config.SetAccessKeySecret("")
	config.SetEndpoint("")

	newClient, err := client.NewClient(&config)
	if err != nil {
		log.Fatal("get client error: ", err)
	}

	var table *client.Table
	table.SetProjectId("")
	table.SetSchemaName("")
	table.SetTableName("")

	table, err = newClient.GetTable(table)
	if err != nil {
		log.Fatal("get table error: ", err)
	}

	println(table.Name)
}
