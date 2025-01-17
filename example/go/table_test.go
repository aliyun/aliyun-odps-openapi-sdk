/*
DISCLAIMER:

This code is provided as an example only to demonstrate the usage of MaxCompute Catalog API.
It is not production-ready and comes with no guarantees of correctness or completeness.

Example usage:

	var config openapi.Config
	config.SetAccessKeyId(accessId)
	config.SetAccessKeySecret(accessKey)
	config.SetEndpoint(endpoint)

	client, err := client.NewClient(&config)
	if err != nil {
	    log.Fatal("get client error: ", err)
	}

Please ensure proper testing and validation before using in production environments.
*/
package _go

import (
	"fmt"
	"strings"
	"testing"

	"github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go/client"
	openapi "github.com/aliyun/aliyun-odps-openapi-sdk/common/go/client"
	"github.com/stretchr/testify/assert"
)

const (
	endpoint  = ""
	accessId  = ""
	accessKey = ""
	project   = ""
	tableName = "test_table"
)

var catalogClient *client.Client
var basicTable *client.Table

func setUp(t *testing.T) {
	var config openapi.Config
	config.SetAccessKeyId(accessId)
	config.SetAccessKeySecret(accessKey)
	config.SetEndpoint(endpoint)

	var err error
	catalogClient, err = client.NewClient(&config)
	if err != nil {
		t.Fatal("get client error: ", err)
	}

	// Create basic table schema
	basicTable = createBasicTable()

	// Try to create table
	_, err = catalogClient.CreateTable(basicTable)
	if err != nil && !strings.Contains(err.Error(), "Table already exist") {
		t.Fatal("create table error: ", err)
	}
}

func createBasicTable() *client.Table {
	// Create columns
	c0 := &client.TableFieldSchema{}
	c0.SetFieldName("col0")
	c0.SetMode("NULLABLE")
	c0.SetTypeCategory("INT")
	c0.SetDescription("InitCol0")

	c1 := &client.TableFieldSchema{}
	c1.SetFieldName("col1")
	c1.SetMode("REQUIRED")
	c1.SetTypeCategory("INT")
	c1.SetDescription("InitCol1")

	c2 := &client.TableFieldSchema{}
	c2.SetFieldName("col2")
	c2.SetMode("NULLABLE")
	c2.SetTypeCategory("STRING")
	c2.SetDescription("Init Update Table")

	// Create nested column
	nestedSubCols := []*client.TableFieldSchema{
		{
			FieldName:    stringPtr("InitNestedSubCol1"),
			TypeCategory: stringPtr("INT"),
		},
		{
			FieldName:    stringPtr("InitNestedSubCol2"),
			TypeCategory: stringPtr("INT"),
		},
		{
			FieldName:    stringPtr("InitNestedSubCol3"),
			TypeCategory: stringPtr("STRING"),
		},
	}

	c3 := &client.TableFieldSchema{}
	c3.SetFieldName("InitNestedCol")
	c3.SetMode("REQUIRED")
	c3.SetTypeCategory("STRUCT")
	c3.SetFields(nestedSubCols)

	// Create table schema
	tableSchema := &client.TableFieldSchema{}
	tableSchema.SetMode("NULLABLE")
	tableSchema.SetFields([]*client.TableFieldSchema{c0, c1, c2, c3})

	// Create table
	table := &client.Table{}
	table.SetProjectId(project)
	table.SetSchemaName("default")
	table.SetType("TABLE")
	table.SetTableName(tableName)
	table.SetTableSchema(tableSchema)
	table.SetDescription("InitDescription")

	return table
}

func TestBasicUpdate(t *testing.T) {
	setUp(t)

	// Update description
	updatedDescription := "Basic Update Table Description."
	basicTable.SetDescription(updatedDescription)

	updated, err := catalogClient.UpdateTable(basicTable)
	assert.NoError(t, err)
	assert.Equal(t, updatedDescription, *updated.Description)

	// Verify through get
	got, err := catalogClient.GetTable(basicTable)
	assert.NoError(t, err)
	assert.Equal(t, updatedDescription, *got.Description)
}

func TestAppendColumn(t *testing.T) {
	setUp(t)

	// Append nullable columns
	newCols := []*client.TableFieldSchema{
		{
			FieldName:    stringPtr("Append1"),
			TypeCategory: stringPtr("INT"),
			Mode:         stringPtr("NULLABLE"),
			Description:  stringPtr("AppendTable1"),
		},
		{
			FieldName:    stringPtr("Append2"),
			TypeCategory: stringPtr("INT"),
			Mode:         stringPtr("NULLABLE"),
			Description:  stringPtr("AppendTable2"),
		},
	}

	schema := basicTable.TableSchema
	fields := schema.Fields
	fields = append(fields, newCols...)
	schema.SetFields(fields)

	updated, err := catalogClient.UpdateTable(basicTable)
	assert.NoError(t, err)

	// Verify new columns
	foundAppend1 := false
	foundAppend2 := false
	for _, field := range updated.TableSchema.Fields {
		if *field.FieldName == "Append1" {
			foundAppend1 = true
		}
		if *field.FieldName == "Append2" {
			foundAppend2 = true
		}
	}
	assert.True(t, foundAppend1)
	assert.True(t, foundAppend2)
}

func TestAppendNestedColumn(t *testing.T) {
	setUp(t)

	// Add new sub column to existing nested column
	schema := basicTable.TableSchema
	nestedCol := schema.Fields[3] // InitNestedCol
	nestedFields := nestedCol.Fields
	nestedFields = append(nestedFields, &client.TableFieldSchema{
		FieldName:    stringPtr("appendinitnestedsubcol4"),
		TypeCategory: stringPtr("STRING"),
	})
	nestedCol.SetFields(nestedFields)

	// Create new nested column
	newNestedSubCol := &client.TableFieldSchema{
		FieldName:    stringPtr("nestedcolnested"),
		TypeCategory: stringPtr("STRUCT"),
		Fields: []*client.TableFieldSchema{
			{
				FieldName:    stringPtr("nestednestedcol1"),
				TypeCategory: stringPtr("STRING"),
			},
		},
	}

	newNestedColumn := &client.TableFieldSchema{
		FieldName:    stringPtr("AppendNestedCol"),
		TypeCategory: stringPtr("STRUCT"),
		Mode:         stringPtr("NULLABLE"),
		Fields: []*client.TableFieldSchema{
			{
				FieldName:    stringPtr("nestedcolcol1"),
				TypeCategory: stringPtr("STRING"),
			},
			{
				FieldName:    stringPtr("nestedcolcol2"),
				TypeCategory: stringPtr("INT"),
			},
			{
				FieldName:    stringPtr("nestedcolcol3"),
				TypeCategory: stringPtr("STRING"),
			},
			newNestedSubCol,
		},
	}

	// Add simple column and nested column
	fields := schema.Fields
	fields = append(fields,
		&client.TableFieldSchema{
			FieldName:    stringPtr("AppendSimpleCol"),
			TypeCategory: stringPtr("INT"),
			Mode:         stringPtr("NULLABLE"),
			Description:  stringPtr("AppendSimpleColumn"),
		},
		newNestedColumn,
	)
	schema.SetFields(fields)

	updated, err := catalogClient.UpdateTable(basicTable)
	assert.NoError(t, err)

	// Verify all new columns exist
	updatedSchema := updated.TableSchema
	schemaStr := fmt.Sprintf("%v", updatedSchema)
	assert.Contains(t, schemaStr, "nestedcolnested")
	assert.Contains(t, schemaStr, "nestednestedcol1")
	assert.Contains(t, schemaStr, "nestedcolcol1")
	assert.Contains(t, schemaStr, "nestedcolcol2")
	assert.Contains(t, schemaStr, "nestedcolcol3")
	assert.Contains(t, schemaStr, "AppendSimpleCol")
}

func TestUpdateComments(t *testing.T) {
	setUp(t)

	basicTable.SetDescription("Updated Table description")
	schema := basicTable.TableSchema
	fields := schema.Fields

	// Update column descriptions
	fields[0].SetDescription("Update col0")
	fields[1].SetDescription("Update col1")
	fields[3].SetDescription("Update nested col1 description")

	_, err := catalogClient.UpdateTable(basicTable)
	assert.NoError(t, err)

	// Verify updates through get
	got, err := catalogClient.GetTable(basicTable)
	assert.NoError(t, err)
	assert.Equal(t, "Updated Table description", *got.Description)

	gotFields := got.TableSchema.Fields
	assert.Equal(t, "Update col0", *gotFields[0].Description)
	assert.Equal(t, "Update col1", *gotFields[1].Description)
	assert.Equal(t, "Update nested col1 description", *gotFields[3].Description)
}

func TestUpdateColumnMode(t *testing.T) {
	setUp(t)

	schema := basicTable.TableSchema
	fields := schema.Fields

	// Test required to nullable
	fields[1].SetMode("NULLABLE") // col1 was REQUIRED
	updated, err := catalogClient.UpdateTable(basicTable)
	assert.NoError(t, err)
	assert.Equal(t, "NULLABLE", *updated.TableSchema.Fields[1].Mode)

	// Test nullable to required (should fail)
	fields[1].SetMode("REQUIRED")
	_, err = catalogClient.UpdateTable(basicTable)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Cannot change column mode from NULLABLE to REQUIRED")

	// Test setting nested column mode (should fail)
	nestedCol := fields[3].Fields[0]
	nestedCol.SetMode("REQUIRED")
	_, err = catalogClient.UpdateTable(basicTable)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Field mode can only be specified for top level fields")
}

func TestTableLifeCycle(t *testing.T) {
	setUp(t)

	expected := int32(1)
	expOptions := &client.ExpirationOptions{
		ExpirationDays: &expected,
	}
	basicTable.SetExpirationOptions(expOptions)

	_, err := catalogClient.UpdateTable(basicTable)
	assert.NoError(t, err)

	got, err := catalogClient.GetTable(basicTable)
	assert.NoError(t, err)
	assert.Equal(t, expected, *got.ExpirationOptions.ExpirationDays)
}

func TestDeleteColumn(t *testing.T) {
	setUp(t)

	schema := basicTable.TableSchema
	fields := schema.Fields

	// Try to delete column (should fail)
	schema.SetFields(fields[1:])
	_, err := catalogClient.UpdateTable(basicTable)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Delete column is not supported")

	// Try to change column type (should fail)
	fields[0].SetTypeCategory("STRING")
	_, err = catalogClient.UpdateTable(basicTable)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Not support change column type")
}

// Helper function to verify column exists in schema
func containsColumn(schema *client.TableFieldSchema, columnName string) bool {
	for _, field := range schema.Fields {
		if *field.FieldName == columnName {
			return true
		}
		// Check nested columns if it's a STRUCT
		if *field.TypeCategory == "STRUCT" && field.Fields != nil {
			if containsColumn(&client.TableFieldSchema{Fields: field.Fields}, columnName) {
				return true
			}
		}
	}
	return false
}

// Helper function to create a basic column
func createBasicColumn(name, desc string) *client.TableFieldSchema {
	return &client.TableFieldSchema{
		FieldName:    stringPtr(name),
		Mode:         stringPtr("NULLABLE"),
		TypeCategory: stringPtr("INT"),
		Description:  stringPtr(desc),
	}
}

// Helper function to create a required column
func createRequiredColumn(name, desc string) *client.TableFieldSchema {
	return &client.TableFieldSchema{
		FieldName:    stringPtr(name),
		Mode:         stringPtr("REQUIRED"),
		TypeCategory: stringPtr("INT"),
		Description:  stringPtr(desc),
	}
}

// Helper function to create string pointer
func stringPtr(s string) *string {
	return &s
}
