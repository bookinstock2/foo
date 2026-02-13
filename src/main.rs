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

pub fn farewell(name: &str) -> String {
    format!("Goodbye, {}! See you next time!", name)
}

pub fn lucky_number(name: &str) -> u32 {
    let sum: u32 = name.bytes().map(|b| b as u32).sum();
    sum % 100
}

pub fn reverse_name(name: &str) -> String {
    name.chars().rev().collect()
}

pub fn count_vowels(s: &str) -> usize {
    s.chars()
        .filter(|c| matches!(c.to_ascii_lowercase(), 'a' | 'e' | 'i' | 'o' | 'u'))
        .count()
}

pub fn fizzbuzz(n: u32) -> String {
    match (n % 3, n % 5) {
        (0, 0) => String::from("FizzBuzz"),
        (0, _) => String::from("Fizz"),
        (_, 0) => String::from("Buzz"),
        _ => n.to_string(),
    }
}

pub fn is_palindrome(s: &str) -> bool {
    let lower: String = s.to_lowercase();
    let chars: Vec<char> = lower.chars().collect();
    let len = chars.len();
    for i in 0..len / 2 {
        if chars[i] != chars[len - 1 - i] {
            return false;
        }
    }
    true
}

fn main() {
    println!("{}", hello("Rust"));
    println!("{}", greet("Rust"));
    println!("{}", farewell("Rust"));
    let n = lucky_number("Rust");
    println!("Your lucky number is: {n}");
    let reversed = reverse_name("Rust");
    println!("Reversed: {reversed}");
    let vowels = count_vowels("Hello Rust");
    println!("Vowels in 'Hello Rust': {vowels}");
    let palindrome = is_palindrome("Racecar");
    println!("Is 'Racecar' a palindrome? {palindrome}");
    println!();
    println!("FizzBuzz (1-15):");
    for i in 1..=15 {
        println!("  {i}: {}", fizzbuzz(i));
    }
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

    #[test]
    fn test_farewell_with_name() {
        assert_eq!(farewell("World"), "Goodbye, World! See you next time!");
    }

    #[test]
    fn test_farewell_with_empty_name() {
        assert_eq!(farewell(""), "Goodbye, ! See you next time!");
    }

    #[test]
    fn test_farewell_with_chinese_name() {
        assert_eq!(farewell("Rust学习者"), "Goodbye, Rust学习者! See you next time!");
    }

    #[test]
    fn test_lucky_number_with_name() {
        // R(82) + u(117) + s(115) + t(116) = 430, 430 % 100 = 30
        assert_eq!(lucky_number("Rust"), 30);
    }

    #[test]
    fn test_lucky_number_with_empty_name() {
        assert_eq!(lucky_number(""), 0);
    }

    #[test]
    fn test_lucky_number_range() {
        let n = lucky_number("anything");
        assert!(n < 100);
    }

    #[test]
    fn test_lucky_number_single_char() {
        // 'A' = 65, 65 % 100 = 65
        assert_eq!(lucky_number("A"), 65);
    }

    #[test]
    fn test_reverse_name() {
        assert_eq!(reverse_name("Rust"), "tsuR");
    }

    #[test]
    fn test_reverse_name_empty() {
        assert_eq!(reverse_name(""), "");
    }

    #[test]
    fn test_reverse_name_chinese() {
        assert_eq!(reverse_name("你好世界"), "界世好你");
    }

    #[test]
    fn test_count_vowels_basic() {
        assert_eq!(count_vowels("hello"), 2);
    }

    #[test]
    fn test_count_vowels_uppercase() {
        assert_eq!(count_vowels("AEIOU"), 5);
    }

    #[test]
    fn test_count_vowels_mixed_case() {
        assert_eq!(count_vowels("Hello Rust"), 3);
    }

    #[test]
    fn test_count_vowels_no_vowels() {
        assert_eq!(count_vowels("bcdfg"), 0);
    }

    #[test]
    fn test_count_vowels_empty() {
        assert_eq!(count_vowels(""), 0);
    }

    #[test]
    fn test_count_vowels_all_vowels() {
        assert_eq!(count_vowels("aEiOu"), 5);
    }

    #[test]
    fn test_is_palindrome_basic() {
        assert!(is_palindrome("racecar"));
    }

    #[test]
    fn test_is_palindrome_ignore_case() {
        assert!(is_palindrome("Racecar"));
    }

    #[test]
    fn test_is_palindrome_single_char() {
        assert!(is_palindrome("a"));
    }

    #[test]
    fn test_is_palindrome_empty() {
        assert!(is_palindrome(""));
    }

    #[test]
    fn test_is_palindrome_not_palindrome() {
        assert!(!is_palindrome("hello"));
    }

    #[test]
    fn test_is_palindrome_even_length() {
        assert!(is_palindrome("abba"));
    }

    #[test]
    fn test_is_palindrome_mixed_case() {
        assert!(is_palindrome("MadAm"));
    }

    #[test]
    fn test_fizzbuzz_fizz() {
        assert_eq!(fizzbuzz(3), "Fizz");
        assert_eq!(fizzbuzz(6), "Fizz");
        assert_eq!(fizzbuzz(9), "Fizz");
    }

    #[test]
    fn test_fizzbuzz_buzz() {
        assert_eq!(fizzbuzz(5), "Buzz");
        assert_eq!(fizzbuzz(10), "Buzz");
        assert_eq!(fizzbuzz(20), "Buzz");
    }

    #[test]
    fn test_fizzbuzz_fizzbuzz() {
        assert_eq!(fizzbuzz(15), "FizzBuzz");
        assert_eq!(fizzbuzz(30), "FizzBuzz");
        assert_eq!(fizzbuzz(45), "FizzBuzz");
    }

    #[test]
    fn test_fizzbuzz_number() {
        assert_eq!(fizzbuzz(1), "1");
        assert_eq!(fizzbuzz(2), "2");
        assert_eq!(fizzbuzz(4), "4");
        assert_eq!(fizzbuzz(7), "7");
    }
}
