/// 借用与引用 - 不转移所有权的情况下使用值
/// 规则：
/// 1. 任意时刻，要么有一个可变引用，要么有多个不可变引用
/// 2. 引用必须始终有效（不能悬垂）

pub fn demo() {
    // --- 不可变借用 ---
    let s = String::from("hello");
    let len = calculate_length(&s); // 借用 s，不转移所有权
    println!("[不可变借用] '{}' 的长度是 {}", s, len); // s 仍然有效

    // --- 多个不可变借用 ---
    let r1 = &s;
    let r2 = &s;
    println!("[多个不可变借用] r1={}, r2={}", r1, r2);

    // --- 可变借用 ---
    let mut s2 = String::from("hello");
    change(&mut s2);
    println!("[可变借用] 修改后: {}", s2);

    // --- 可变借用的排他性 ---
    let mut s3 = String::from("exclusive");
    {
        let r3 = &mut s3;
        r3.push_str(" access");
        println!("[排他可变借用] r3 = {}", r3);
    } // r3 的作用域结束，可以再次借用
    let r4 = &mut s3;
    r4.push_str("!");
    println!("[再次可变借用] r4 = {}", r4);

    // --- 切片借用 ---
    let sentence = String::from("hello world rust");
    let first = first_word(&sentence);
    println!("[切片借用] 第一个单词: {}", first);
}

fn calculate_length(s: &str) -> usize {
    s.len()
}

fn change(s: &mut String) {
    s.push_str(", world!");
}

fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &byte) in bytes.iter().enumerate() {
        if byte == b' ' {
            return &s[..i];
        }
    }
    s
}
