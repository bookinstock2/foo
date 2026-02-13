# 变更日志

所有本项目的重要变化都会被记录在这个文件中。

## [未发布]

### 新增功能

### 改进

### 修复

## [2026-02-13]

### 文档
- **docs: 添加测试章节说明如何使用pytest运行测试** (300df80)
  - 添加了测试章节的文档说明
  - 说明如何使用 pytest 运行项目测试

### 测试
- **test: 添加项目测试文件和 hello 模块** (3b1db96)
  - 创建 hello.py 模块，包含 hello() 问候函数
  - 创建 tests/ 目录和 tests/__init__.py
  - 创建 tests/test_hello.py，包含 hello 函数的 pytest 测试
  - 创建 tests/test_utils.py，包含 format_date 和 is_palindrome 函数的全面测试用例

### 新增功能
- **feat: 添加工具函数 format_date 和 is_palindrome** (4d01e56)
  - 添加日期格式化工具函数
  - 添加回文检测工具函数

### 测试
- **test: 添加简单的计算器类** (96a129e)
  - 实现基础的计算器类

## [2026-02-12]

### 新增功能
- **feat: Rust 核心概念学习项目** (39821a2)
  - 涵盖10个核心模块：
    - 所有权 (Ownership) 与移动语义
    - 借用与引用 (Borrowing)
    - 结构体与枚举 (Structs & Enums)
    - Trait 与泛型 (Traits & Generics)
    - 错误处理 (Error Handling)
    - 集合与迭代器 (Collections)
    - 并发 (Concurrency)
    - 闭包 (Closures)
    - 智能指针 (Smart Pointers)
    - 生命周期 (Lifetimes)

---

本项目遵循 [Semantic Versioning](https://semver.org/) 版本控制规范。
