package _go

import (
	"log"

	"github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/client"
	openapi "github.com/aliyun/aliyun-odps-openapi-sdk/common/go/client"
)

// error 'invalid character '<' looking for beginning of value' may because of wrong endpoint or wrong proxy configured
// endpoint should be like 'catalogapi.ap-southeast-5.maxcompute.aliyun.com'

func way_1() {
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
	println(catalogClient.Endpoint)
}

func way_2() {
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
	println(catalogClient.Endpoint)
}

func way_3() {
	var endpoint = ""
	var accessId = ""
	var accessKey = ""

	catalogClient, err := client.NewClient(&openapi.Config{
		AccessKeyId:     &accessId,
		AccessKeySecret: &accessKey,
		Endpoint:        &endpoint,
	})

	if err != nil {
		log.Fatal("get client error: ", err)
	}
	// do something
	println(catalogClient.Endpoint)
}
