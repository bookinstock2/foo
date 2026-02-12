/// 闭包 - Fn、FnMut、FnOnce

pub fn demo() {
    // --- 基本闭包 ---
    let add = |a: i32, b: i32| a + b;
    println!("[闭包] 3 + 5 = {}", add(3, 5));

    // --- 捕获环境变量 ---
    let name = String::from("Rust");
    let greet = || println!("[捕获] Hello, {}!", name); // 不可变借用 name
    greet();
    println!("[捕获后] name 仍可用: {}", name); // name 仍有效

    // --- FnMut：可变借用 ---
    let mut count = 0;
    let mut increment = || {
        count += 1; // 可变借用 count
        count
    };
    println!("[FnMut] count = {}", increment());
    println!("[FnMut] count = {}", increment());
    println!("[FnMut] count = {}", increment());

    // --- FnOnce：消费捕获的变量 ---
    let data = vec![1, 2, 3];
    let consume = move || {
        println!("[FnOnce/move] 消费 data: {:?}", data);
        data // 返回所有权
    };
    let _returned = consume();
    // consume(); // ❌ FnOnce 只能调用一次（如果消费了捕获的值）

    // --- 闭包作为参数 ---
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    let evens: Vec<_> = apply_filter(&numbers, |x| x % 2 == 0);
    println!("[闭包参数] 偶数: {:?}", evens);

    let big: Vec<_> = apply_filter(&numbers, |x| x > 5);
    println!("[闭包参数] >5: {:?}", big);

    // --- 闭包作为返回值 ---
    let doubler = make_multiplier(2);
    let tripler = make_multiplier(3);
    println!("[返回闭包] 5*2={}, 5*3={}", doubler(5), tripler(5));
}

fn apply_filter(nums: &[i32], predicate: impl Fn(i32) -> bool) -> Vec<i32> {
    nums.iter().copied().filter(|&x| predicate(x)).collect()
}

fn make_multiplier(factor: i32) -> Box<dyn Fn(i32) -> i32> {
    Box::new(move |x| x * factor)
}
