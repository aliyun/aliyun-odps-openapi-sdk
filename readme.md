# aliyun-odps-openapi-sdk

本仓库是 MaxCompute OpenAPI 的多语言 SDK（由 Darabonba 从同一份接口定义生成）。

**已发布版本**：`catalog-api 0.4.0`（2026-06-01）

| 语言 | 引入方式 | 当前已发布版本 |
| --- | --- | --- |
| Go | `go get github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go` | `v0.4.0`（tag `catalog-api/go/v0.4.0`，可 `@v0.4.0` 锁定） |
| Java | Maven Central `com.aliyun.odps:catalog-api` | `0.4.0` |
| Python | PyPI `pyodps_catalog` | `0.4.0` |

版本仍处于 `0.x` 阶段，接口与请求行为可能在次要版本之间调整（变更记录见 [catalog-api/CHANGELOG.md](catalog-api/CHANGELOG.md)）。生产使用请锁定具体版本，并在升级前跑一遍自己的回归用例。

## 目录结构
* `common` - 所有 openapi-sdk 的公共组件，用于鉴权，发送/接受请求
* `catalog-api` - ODPS Catalog API 的 SDK 实现

## 安装方式 (catalog-api)

### Golang
```bash
go get github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go          # 取最新已发布版本
go get github.com/aliyun/aliyun-odps-openapi-sdk/catalog-api/go@v0.4.0  # 或锁定版本
```

需要 Go 1.23 及以上：`catalog-api/go/go.mod` 声明 `go 1.23.2`，低版本工具链会直接报 `go.mod requires go >= 1.23`。

### Java
```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>catalog-api</artifactId>
    <version>0.4.0</version>
</dependency>
```

`<version>` 请填 Maven Central 上已发布的 release 版本号；`-SNAPSHOT` 后缀的构建不会发布到中央仓库，直接复制会解析失败。

### Python
```bash
pip install pyodps_catalog          # 安装最新可发布版本
pip install pyodps_catalog==0.4.0   # 或锁定版本
```

## 使用示例 (catalog-api)

### Golang
* 表操作示例：[table_test.go](example/go/table_test.go)

### Java
* 表操作示例：[TableTest.java](example/java/src/test/java/TableTest.java)

### Python
* 表操作示例：[test_table.py](example/python/test_table.py)

## 编译指南

### 前置条件
1. 安装 darabonba CLI
```bash
npm install @darabonba/cli -g
```

### 依赖 `common`（仅从源码构建时需要）

`catalog-api` 依赖同仓库的 `common` 模块：Java 坐标 `com.aliyun.odps:openapi`、Go 模块 `common/go`、Python 包 `maxcompute_tea_openapi`。源码分支里声明的 `common` 版本可能还没发布到中央仓库（截至 2026-10，`develop` 的 Java 声明为 `1.3.2`，Maven Central 最新为 `1.3.1`），此时单独构建 `catalog-api/java` 或 `example/java` 会因依赖解析失败而报错。

先安装 `common`，再构建 `catalog-api`：

```bash
cd common/java && mvn clean install -DskipTests && cd ../..
```

或直接执行根目录的 `./build.sh`：它会先处理 `common` 再处理 `catalog-api`，把 `common` 装进本地仓库。注意该脚本会删除并重新生成各语言的输出目录（`go` 全量重建，`java`/`python` 保留 `pom.xml`/`setup.py`）。

`./build.sh` 里从 `Darafile` 同步版本号的两行用的是 BSD 形态的 `sed -i ''`：在 GNU sed（多数 Linux 发行版）上这两步会以 rc=2 失败且不会中止脚本，`java/pom.xml` 与 Python `__version__` 可能停留在 codegen 写下的默认值。跨平台构建建议按上面的方式显式安装 `common`，再构建 `catalog-api`。

两个 Java 模块的 `maven-compiler-plugin` 配置的是 `source/target 7`：JDK 8 / 11 / 17 可编译，JDK 21 及以上会失败（`Target option 7 is no longer supported. Use 8 or later.`）。

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

1. 版本仍处于 `0.x` 阶段，API 与请求行为可能变更；依赖请锁定到已发布的具体版本，升级前做回归验证
2. 使用前请确保已安装所需的依赖工具
3. 如遇到问题，请通过 Issues 反馈

## 许可证

[Apache License 2.0](LICENSE)