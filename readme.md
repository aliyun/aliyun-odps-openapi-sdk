# aliyun-odps-openapi-sdk

目前尚处于 Alpha 阶段，在正式 Release 之前，不建议用户在生产环境使用

## 目录结构
* `common` - 所有 openapi-sdk 的公共组件，用于鉴权，发送/接受请求
* `catalog-api` - ODPS Catalog API 的 SDK 实现

## 安装方式 (catalog-api)

### Golang
```bash
go get github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go
```

### Java
```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>catalog-api</artifactId>
    <version>0.1.1-SNAPSHOT</version>
</dependency>
```

### Python
```bash
pip install pyodps_catalog
```

## 使用示例 (catalog-api)

### Golang
* 表操作示例：[table_test.go](https://github.com/aliyun/aliyun-odps-openapi-sdk/blob/master/example/go/table_test.go)

### Java
* 表操作示例：[TableTest.java](https://github.com/aliyun/aliyun-odps-openapi-sdk/blob/master/example/java/src/test/java/TableTest.java)

### Python
* 表操作示例：[test_table.py](https://github.com/aliyun/aliyun-odps-openapi-sdk/blob/master/example/python/test_table.py)

## 编译指南

### 前置条件
1. 安装 darabonba CLI
```bash
npm install @darabonba/cli -g
```

### 构建
```bash
./build.sh
```

构建选项：
* `--go`: 仅构建 Go SDK
* `--java`: 仅构建 Java SDK
* `--python`: 仅构建 Python SDK
* 不带参数则同时构建以上语言 SDK

## 注意事项

1. 本项目目前处于 Alpha 阶段，API 可能会发生变更
2. 使用前请确保已安装所需的依赖工具
3. 如遇到问题，请通过 Issues 反馈

## 许可证

[Apache License 2.0](LICENSE)