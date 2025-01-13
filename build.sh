#!/bin/bash

# 函数：处理目录
handle_directory() {
    local dir_path="$1"
    
    echo "Processing directory: $dir_path"
    
    # 进入到指定目录
    cd "$dir_path" || { echo "Failed to change directory to $dir_path."; exit 1; }

    # 安装依赖
    dara clean
    echo "Installing dependencies..."
    dara install || { echo "Failed to install dependencies in $dir_path."; exit 1; }

    # 删除旧的 java 目录
    if [ -d "java" ]; then
        echo "Removing existing java directory..."
        rm -r java || { echo "Failed to remove java directory in $dir_path."; exit 1; }
    fi

    # 删除旧的 go 目录
    if [ -d "go" ]; then
        echo "Removing existing go directory..."
        rm -r go || { echo "Failed to remove go directory in $dir_path."; exit 1; }
    fi

    # 生成 Java 代码
    echo "Generating Java code..."
    dara codegen java ./java || { echo "Failed to generate Java code in $dir_path."; exit 1; }

    # 生成 Go 代码
    echo "Generating Go code..."
    dara codegen go ./go || { echo "Failed to generate Go code in $dir_path."; exit 1; }

    # 进入到生成的 java 目录
    cd java || { echo "Failed to change directory to java in $dir_path."; exit 1; }

    # 使用 Maven 清理和构建项目
    echo "Cleaning and installing the Java project..."
    mvn clean install -Dgpg.skip || { echo "Maven build failed in $dir_path."; exit 1; }

    # 进入到生成的 go 目录
    cd ../go || { echo "Failed to change directory to go in $dir_path."; exit 1; }

    # go mod tidy
    echo "Cleaning and installing the Go project..."
    go mod tidy || { echo "Go build failed in $dir_path."; exit 1; }

    echo "Project built successfully in $dir_path."

    cd ../..
}

# 处理每个目录
handle_directory "common"
handle_directory "catalog-api"

echo "All directories processed successfully."