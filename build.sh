#!/bin/bash

# 默认值：都编译
build_go=true
build_java=true
build_python=true

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --go)
            build_go=true
            build_java=false
            build_python=false
            shift
            ;;
        --java)
            build_go=false
            build_java=true
            build_python=false
            shift
            ;;
        --python)
            build_go=false
            build_java=false
            build_python=true
            shift
            ;;
        *)
            echo "Unknown parameter: $1"
            echo "Usage: $0 [--go] [--java] [--python]"
            exit 1
            ;;
    esac
done

# sed -i 的参数形态在 GNU sed 和 BSD/macOS sed 下不一样：
#   GNU:  sed -i 's/.../.../' file
#   BSD:  sed -i '' 's/.../.../' file
# 写死任意一种，换到另一种 sed 上都会失败：GNU sed 会把 BSD 形态里的空串当成脚本文件名，
# 报 "can't read <空串>: No such file or directory" 并以 rc=2 退出，目标文件不被改动。
# 这里探测一次（BSD sed 不认识 --version），下面两处版本号回写统一用 "${SED_INPLACE[@]}"。
if sed --version >/dev/null 2>&1; then
    SED_INPLACE=(-i)
else
    SED_INPLACE=(-i '')
fi

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

    # 如果构建 Java
    if [ "$build_java" = true ]; then
        # 清理旧生成物，但保留 pom.xml（含 javadoc/source 等插件配置）
        if [ -d "java" ]; then
            echo "Cleaning generated java sources (preserving pom.xml)..."
            find java -mindepth 1 -maxdepth 1 -not -name 'pom.xml' -exec rm -rf {} + || { echo "Failed to clean java directory in $dir_path."; exit 1; }
        fi

        # 生成 Java 代码
        echo "Generating Java code..."
        dara codegen java ./java || { echo "Failed to generate Java code in $dir_path."; exit 1; }

        # 从 Darafile 读取版本号，修正 pom.xml 中的项目 version（2空格缩进的那行）
        # 这几步失败都要显式报错退出：静默跳过会让 pom.xml 停在 codegen 的默认版本，
        # 用户看到的是下游依赖解析失败，很难联想到这一步。
        local java_version
        java_version=$(grep '"version"' Darafile | head -1 | sed -E 's/.*"version": "v?([^"]+)".*/\1/')
        if [ -z "$java_version" ]; then
            echo "Failed to read version from Darafile in $dir_path."; exit 1
        fi
        if [ ! -f "java/pom.xml" ]; then
            echo "java/pom.xml not found after codegen in $dir_path."; exit 1
        fi
        sed "${SED_INPLACE[@]}" "s|^  <version>[^<]*</version>|  <version>${java_version}</version>|" java/pom.xml \
            || { echo "Failed to set Java version in java/pom.xml in $dir_path."; exit 1; }
        grep -q "  <version>${java_version}</version>" java/pom.xml \
            || { echo "Java version ${java_version} missing in java/pom.xml after rewrite in $dir_path."; exit 1; }
        echo "Set Java version to $java_version"

        # 进入到生成的 java 目录
        cd java || { echo "Failed to change directory to java in $dir_path."; exit 1; }

        # 使用 Maven 清理和构建项目
        echo "Cleaning and installing the Java project..."
        mvn clean install -Dgpg.skip || { echo "Maven build failed in $dir_path."; exit 1; }

        cd .. || exit 1
    fi

    # 如果构建 Go
    if [ "$build_go" = true ]; then
        # 删除旧的 go 目录
        if [ -d "go" ]; then
            echo "Removing existing go directory..."
            rm -r go || { echo "Failed to remove go directory in $dir_path."; exit 1; }
        fi

        # 生成 Go 代码
        echo "Generating Go code..."
        dara codegen go ./go || { echo "Failed to generate Go code in $dir_path."; exit 1; }

        # 进入到生成的 go 目录
        cd go || { echo "Failed to change directory to go in $dir_path."; exit 1; }

        # go mod tidy
        echo "Cleaning and installing the Go project..."
        go mod tidy || { echo "Go build failed in $dir_path."; exit 1; }

        cd .. || exit 1
    fi

    # 如果构建 Python
    if [ "$build_python" = true ]; then
        # 清理旧生成物，但保留 setup.py
        if [ -d "python" ]; then
            echo "Cleaning generated python sources (preserving setup.py)..."
            find python -mindepth 1 -maxdepth 1 -not -name 'setup.py' -exec rm -rf {} + || { echo "Failed to clean python directory in $dir_path."; exit 1; }
        fi

        # 生成 python 代码
        echo "Generating python code..."
        dara codegen python ./python || { echo "Failed to generate python code in $dir_path."; exit 1; }

        # 从 Darafile 读取版本号，修正 codegen 生成的 __version__
        local py_version
        py_version=$(grep '"version"' Darafile | head -1 | sed -E 's/.*"version": "v?([^"]+)".*/\1/')
        if [ -z "$py_version" ]; then
            echo "Failed to read version from Darafile in $dir_path."; exit 1
        fi
        local init_file
        init_file=$(find python -name '__init__.py' -path '*/__init__.py' | head -1)
        if [ -z "$init_file" ]; then
            echo "No __init__.py found under python in $dir_path."; exit 1
        fi
        sed "${SED_INPLACE[@]}" "s/__version__ = .*/__version__ = \"$py_version\"/" "$init_file" \
            || { echo "Failed to set Python version in $init_file in $dir_path."; exit 1; }
        grep -q "__version__ = \"$py_version\"" "$init_file" \
            || { echo "Python version ${py_version} missing in $init_file after rewrite in $dir_path."; exit 1; }
        echo "Set Python __version__ to $py_version"
        # Python 分支不进 ./python 目录：codegen 产物就地生成、没有构建步骤，
        # 因此这里不配 cd ..，退出模块目录由函数末尾那句统一负责。
    fi

    echo "Project built successfully in $dir_path."

    cd ..
}

# 打印构建配置
echo "Build configuration:"
echo "Building Go: $build_go"
echo "Building Java: $build_java"
echo "Building Python: $build_python"

# 处理每个目录
handle_directory "common"
handle_directory "catalog-api"

echo "All directories processed successfully."