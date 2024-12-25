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

    # 生成 Java 代码
    echo "Generating Java code..."
    dara codegen java ./java || { echo "Failed to generate Java code in $dir_path."; exit 1; }

    # 进入到生成的 java 目录
    cd java || { echo "Failed to change directory to java in $dir_path."; exit 1; }

    # 使用 Maven 清理和构建项目
    echo "Cleaning and installing the Java project..."
    mvn clean install || { echo "Maven build failed in $dir_path."; exit 1; }

    echo "Java project built successfully in $dir_path."

    cd ../..
}

# 处理每个目录
handle_directory "common"
handle_directory "catalog-api"

echo "All directories processed successfully."