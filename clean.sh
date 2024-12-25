#!/bin/bash

# 函数：处理目录
handle_directory() {
    local dir_path="$1"
    
    echo "Processing directory: $dir_path"
    
    # 进入到指定目录
    cd "$dir_path" || { echo "Failed to change directory to $dir_path."; exit 1; }

    # 删除依赖
    echo "Clean dependencies..."
    dara clean

    # 删除 java 目录
    if [ -d "java" ]; then
        echo "Removing existing java directory..."
        rm -r java || { echo "Failed to remove java directory in $dir_path."; exit 1; }
    fi

    cd ..
}

# 处理每个目录
handle_directory "common"
handle_directory "catalog-api"

echo "All directories processed successfully."