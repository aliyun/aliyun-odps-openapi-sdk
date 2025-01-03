package _go

import catalog "module/path/client"

func Main() {
	var table catalog.Table
	table.SetTableName("test_table")
	table.SetProjectId("test_project")
	table.SetSchemaName("default")

	catalog.NewClient()

}
