### 最简case

1. 安装 darabonba
`npm install @darabonba/cli -g`
2. 生成 common
```
cd common
dara install
dara codegen java ./common
cd common
mvn clean install
```
3. 生成 catalog-api
```
cd common
dara install
dara codegen java ./catalog-api
cd catalog-api
mvn clean install
```

### common 依赖 [com.aliyun.odps.tea-util](https://code.alibaba-inc.com/zhangdingxin.zdx/tea-util), tea-util 目前只有 Java 实现，因此目前只能生成 JavaSDK。and 由于 tea-util 未发布，需要手动 mvn install
