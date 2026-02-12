/// 集合类型 - Vec、HashMap 和迭代器

use std::collections::HashMap;

pub fn demo() {
    // --- Vec ---
    let mut nums = vec![3, 1, 4, 1, 5, 9, 2, 6];
    nums.push(5);
    nums.sort();
    nums.dedup(); // 去除连续重复
    println!("[Vec] 排序去重: {:?}", nums);

    // --- 迭代器链 ---
    let sum: i32 = nums.iter().filter(|&&x| x > 3).sum();
    println!("[迭代器] >3 的元素之和: {}", sum);

    let doubled: Vec<i32> = nums.iter().map(|x| x * 2).collect();
    println!("[map+collect] 翻倍: {:?}", doubled);

    // enumerate
    for (i, val) in nums.iter().enumerate().take(3) {
        println!("[enumerate] index={}, value={}", i, val);
    }

    // fold（类似 reduce）
    let product: i32 = vec![1, 2, 3, 4].iter().fold(1, |acc, x| acc * x);
    println!("[fold] 1*2*3*4 = {}", product);

    // --- HashMap ---
    let mut scores: HashMap<&str, Vec<i32>> = HashMap::new();
    scores.entry("Alice").or_insert_with(Vec::new).push(95);
    scores.entry("Alice").or_insert_with(Vec::new).push(87);
    scores.entry("Bob").or_insert_with(Vec::new).push(76);

    for (name, s) in &scores {
        let avg: f64 = s.iter().sum::<i32>() as f64 / s.len() as f64;
        println!("[HashMap] {} 的平均分: {:.1}", name, avg);
    }

    // --- 字符串也是集合 ---
    let hello = String::from("你好世界 Hello");
    let char_count = hello.chars().count();
    let has_chinese = hello.chars().any(|c| c > '\u{4E00}' && c < '\u{9FFF}');
    println!("[String] '{}' 有 {} 个字符, 包含中文: {}", hello, char_count, has_chinese);

    // zip：合并两个迭代器
    let names = vec!["Rust", "Go", "Python"];
    let years = vec![2010, 2009, 1991];
    let langs: Vec<_> = names.iter().zip(years.iter()).collect();
    println!("[zip] 语言和年份: {:?}", langs);
}
