# Foo - Rust 核心概念学习项目 🦀

一个覆盖 Rust 核心概念的学习项目，通过可运行的代码示例来理解 Rust 的关键特性。

## 涵盖的核心概念

| 模块 | 概念 |
|------|------|
| `ownership` | 所有权、移动语义、克隆 |
| `borrowing` | 借用、可变引用、生命周期 |
| `structs_enums` | 结构体、枚举、模式匹配 |
| `traits_generics` | Trait、泛型、Trait Bound |
| `error_handling` | Result、Option、`?` 操作符 |
| `collections` | Vec、HashMap、迭代器 |
| `concurrency` | 线程、消息传递、Mutex |
| `closures` | 闭包、Fn/FnMut/FnOnce |
| `smart_pointers` | Box、Rc、RefCell |
| `lifetime` | 生命周期标注、省略规则 |

## 运行

```bash
cargo run
```

每个模块都会输出演示结果，帮助你理解各个概念的行为。

## 学习建议

1. 从 `ownership` 开始，这是 Rust 最独特的概念
2. 理解 `borrowing` 后再看 `lifetime`
3. `traits_generics` 是写出优雅 Rust 代码的关键
4. `error_handling` 是 Rust 的惯用错误处理方式

## 测试

使用 pytest 运行测试：

```bash
pytest
```

运行特定测试文件：

```bash
pytest tests/test_file.py
```

运行详细输出：

```bash
pytest -v
```
