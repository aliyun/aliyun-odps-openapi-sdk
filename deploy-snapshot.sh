#!/bin/bash

handle_directory() {
    local dir_path="$1"
    
    echo "Processing directory: $dir_path"
    
    # 进入到指定目录
    cd "$dir_path" || { echo "Failed to change directory to $dir_path."; exit 1; }
    cd "java"

    # 输入文件名
    POM_FILE="pom.xml"

    # 备份原始文件
    cp "$POM_FILE" "${POM_FILE}.bak"

    # 删除 <distributionManagement> 部分
    sed -i '/<distributionManagement>/,/<\/distributionManagement>/d' "$POM_FILE"

    # 添加 <parent> 部分
    sed -i '/<project>/a \
        <parent>\
            <groupId>com.taobao</groupId>\
            <artifactId>parent</artifactId>\
            <version>1.0.2</version>\
        </parent>' "$POM_FILE"

    echo "Modified $POM_FILE. Backup created as ${POM_FILE}.bak"

    mvn clean deploy -DskipTests

}

# 处理每个目录
handle_directory "common"
handle_directory "catalog-api"

echo "All directories processed successfully."