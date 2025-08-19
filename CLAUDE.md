# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the Alibaba Cloud MaxCompute OpenAPI SDK, which provides SDKs for multiple languages (Go, Java, Python) for interacting with MaxCompute Catalog API. The project is organized into:

1. `common` - Shared components for authentication, sending/receiving requests across all SDKs
2. `catalog-api` - ODPS Catalog API SDK implementation
3. `example` - Usage examples for each language
4. `utils` - Utility functions

## Build System

The project uses Darabonba, a DSL for defining APIs that can be compiled to multiple programming languages.

### Prerequisites
- Install Darabonba CLI: `npm install @darabonba/cli -g`

### Building
- Run `./build.sh` to build SDKs for all languages
- Build options:
  * `--go`: Build only Go SDK
  * `--java`: Build only Java SDK
  * `--python`: Build only Python SDK

The build process:
1. Cleans previous builds with `dara clean`
2. Installs dependencies with `dara install`
3. Generates code for each language with `dara codegen [language]`
4. Runs language-specific build tools (Maven for Java, go mod tidy for Go)

## Code Structure

### Common Components
- Authentication and request handling in `common/`
- Cross-language utilities and models

### Language-Specific SDKs
- Generated code for each language in respective directories
- Each SDK follows the language's standard conventions

### Key Classes
- `Client`: Main entry point for API interactions
- `Config`: Configuration for client initialization
- `Table`: Model for table operations
- `TableFieldSchema`: Schema definition for table fields

## Testing

Examples of how to use the SDKs are provided in the `example/` directory:
- Java: `example/java/src/test/java/TableTest.java`
- Go: `example/go/table_test.go`
- Python: `example/python/test_table.py`

## Development Workflow

1. Make changes to `.dara` files which define the API
2. Run `./build.sh` to regenerate SDK code for all languages
3. Test changes with example code

Note: Generated files should not be manually edited as they will be overwritten during the build process.