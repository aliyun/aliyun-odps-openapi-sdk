package _go

import (
	"log"
	"testing"

	"github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/client"
	openapi "github.com/aliyun/aliyun-odps-openapi-sdk/common/go/client"
)

const endpoint = ""
const accessId = ""
const accessKey = ""
const project = ""

func Test_CreateTable(t *testing.T) {
	var config openapi.Config
	config.SetAccessKeyId(accessId)
	config.SetAccessKeySecret(accessKey)
	config.SetEndpoint(endpoint)

	newClient, err := client.NewClient(&config)
	if err != nil {
		log.Fatal("get client error: ", err)
	}

	var table client.Table
	table.SetType("TABLE")
	table.SetProjectId(project)
	table.SetSchemaName("default")
	table.SetTableName("test")

	var tableSchema client.TableFieldSchema
	var column0 client.TableFieldSchema
	column0.SetTypeCategory("STRING")
	column0.SetFieldName("c0")
	tableSchema.SetFields([]*client.TableFieldSchema{&column0})
	table.SetTableSchema(&tableSchema)

	tableRef, err := newClient.CreateTable(&table)
	if err != nil {
		log.Fatal("create table error: ", err)
	}
	println(*tableRef.Name)
}

func Test_GetTable(t *testing.T) {
	var config openapi.Config
	config.SetAccessKeyId(accessId)
	config.SetAccessKeySecret(accessKey)
	config.SetEndpoint(endpoint)

	newClient, err := client.NewClient(&config)
	if err != nil {
		log.Fatal("get client error: ", err)
	}

	var table client.Table
	table.SetProjectId(project)
	table.SetSchemaName("default")
	table.SetTableName("test")

	tableRef, err := newClient.GetTable(&table)
	if err != nil {
		log.Fatal("get table error: ", err)
	}
	println(*tableRef.Name)
}
