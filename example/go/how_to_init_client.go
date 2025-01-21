package _go

import (
	"log"

	"github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/client"
	openapi "github.com/aliyun/aliyun-odps-openapi-sdk/common/go/client"
)

func right_way_1() {
	var endpoint = ""
	var accessId = ""
	var accessKey = ""

	config := new(openapi.Config).
		SetEndpoint(endpoint).
		SetAccessKeyId(accessId).
		SetAccessKeySecret(accessKey)
	catalogClient, err := client.NewClient(config)

	if err != nil {
		log.Fatal("get client error: ", err)
	}

	// do something
	println(catalogClient.Project)
}

func right_way_2() {
	var endpoint = ""
	var accessId = ""
	var accessKey = ""

	var config openapi.Config
	config.SetAccessKeyId(accessId)
	config.SetAccessKeySecret(accessKey)
	config.SetEndpoint(endpoint)
	catalogClient, err := client.NewClient(&config)

	if err != nil {
		log.Fatal("get client error: ", err)
	}
	// do something
	println(catalogClient.Project)
}

func wrong_way() {
	var endpoint = ""
	var accessId = ""
	var accessKey = ""

	// this may cause error 'invalid character '<' looking for beginning of value'

	catalogClient, err := client.NewClient(&openapi.Config{
		AccessKeyId:     &endpoint,
		AccessKeySecret: &accessId,
		Endpoint:        &accessKey,
	})

	if err != nil {
		log.Fatal("get client error: ", err)
	}
	// do something
	println(catalogClient.Project)
}
