module _go

go 1.16

require (
    module/path v1.2.3
    gitlab.alibaba-inc.com/odps/opensdk/common/go/client v0.0.0
)

replace module/path => ../../catalog-api/go
replace gitlab.alibaba-inc.com/odps/opensdk/common/go/client => ../../common/go
