// Foo - Rust 核心概念学习项目
// 通过可运行的代码示例来理解 Rust 的关键特性

mod ownership;
mod borrowing;
mod structs_enums;
mod traits_generics;
mod error_handling;
mod collections;
mod concurrency;
mod closures;
mod smart_pointers;
mod lifetime;

pub fn hello(name: &str) -> String {
    format!("Hello, {}!", name)
}

pub fn greet(name: &str) -> String {
    format!("Hey, {}! Welcome!", name)
}

fn main() {
    println!("{}", hello("Rust"));
    println!("{}", greet("Rust"));
    println!();
    println!("🦀 Rust 核心概念学习项目\n");

    println!("═══════════════════════════════════");
    println!("1. 所有权 (Ownership)");
    println!("═══════════════════════════════════");
    ownership::demo();

    println!("\n═══════════════════════════════════");
    println!("2. 借用与引用 (Borrowing)");
    println!("═══════════════════════════════════");
    borrowing::demo();

    println!("\n═══════════════════════════════════");
    println!("3. 结构体与枚举 (Structs & Enums)");
    println!("═══════════════════════════════════");
    structs_enums::demo();

    println!("\n═══════════════════════════════════");
    println!("4. Trait 与泛型 (Traits & Generics)");
    println!("═══════════════════════════════════");
    traits_generics::demo();

    println!("\n═══════════════════════════════════");
    println!("5. 错误处理 (Error Handling)");
    println!("═══════════════════════════════════");
    error_handling::demo();

    println!("\n═══════════════════════════════════");
    println!("6. 集合 (Collections)");
    println!("═══════════════════════════════════");
    collections::demo();

    println!("\n═══════════════════════════════════");
    println!("7. 并发 (Concurrency)");
    println!("═══════════════════════════════════");
    concurrency::demo();

    println!("\n═══════════════════════════════════");
    println!("8. 闭包 (Closures)");
    println!("═══════════════════════════════════");
    closures::demo();

    println!("\n═══════════════════════════════════");
    println!("9. 智能指针 (Smart Pointers)");
    println!("═══════════════════════════════════");
    smart_pointers::demo();

    println!("\n═══════════════════════════════════");
    println!("10. 生命周期 (Lifetimes)");
    println!("═══════════════════════════════════");
    lifetime::demo();

    println!("\n🎉 所有示例运行完毕！");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_hello_with_name() {
        assert_eq!(hello("World"), "Hello, World!");
    }

    #[test]
    fn test_hello_with_empty_name() {
        assert_eq!(hello(""), "Hello, !");
    }

    #[test]
    fn test_hello_with_chinese_name() {
        assert_eq!(hello("Rust学习者"), "Hello, Rust学习者!");
    }

    #[test]
    fn test_greet_with_name() {
        assert_eq!(greet("World"), "Hey, World! Welcome!");
    }

    #[test]
    fn test_greet_with_empty_name() {
        assert_eq!(greet(""), "Hey, ! Welcome!");
    }

    #[test]
    fn test_greet_with_chinese_name() {
        assert_eq!(greet("Rust学习者"), "Hey, Rust学习者! Welcome!");
    }
}
