/// 所有权 - Rust 最核心的概念
/// 规则：
/// 1. 每个值都有一个所有者
/// 2. 同一时刻只能有一个所有者
/// 3. 所有者离开作用域时，值被丢弃

pub fn demo() {
    // --- 移动语义 (Move) ---
    let s1 = String::from("hello");
    let s2 = s1; // s1 的所有权移动到 s2，s1 不再有效
    // println!("{}", s1); // ❌ 编译错误！s1 已经无效
    println!("[移动] s2 = {}", s2);

    // --- 克隆 (Clone) ---
    let s3 = String::from("world");
    let s4 = s3.clone(); // 深拷贝，s3 仍然有效
    println!("[克隆] s3 = {}, s4 = {}", s3, s4);

    // --- Copy trait：栈上的数据自动拷贝 ---
    let x = 42;
    let y = x; // i32 实现了 Copy，x 仍然有效
    println!("[Copy] x = {}, y = {}", x, y);

    // --- 函数与所有权 ---
    let s5 = String::from("函数所有权");
    takes_ownership(s5); // s5 的所有权移动到函数内
    // println!("{}", s5); // ❌ s5 已经无效

    let s6 = gives_ownership(); // 函数返回值的所有权转移给 s6
    println!("[返回所有权] s6 = {}", s6);

    // --- 作用域与 Drop ---
    {
        let _scoped = String::from("我在作用域内");
        println!("[作用域] _scoped 存在");
    } // _scoped 在这里被 drop
    println!("[作用域] _scoped 已被释放");
}

fn takes_ownership(s: String) {
    println!("[接收所有权] s = {}", s);
} // s 在这里被 drop

fn gives_ownership() -> String {
    String::from("来自函数的字符串")
}
