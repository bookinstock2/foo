/// 生命周期 - 确保引用始终有效

pub fn demo() {
    // --- 基本生命周期 ---
    let string1 = String::from("长字符串");
    let result;
    {
        let string2 = String::from("短");
        result = longest(string1.as_str(), string2.as_str());
        println!("[生命周期] 较长的: {}", result);
    }
    // 注意：result 不能在这里使用，因为 string2 已经离开作用域

    // --- 结构体中的生命周期 ---
    let novel = String::from("在很久很久以前。有一个程序员...");
    let excerpt = ImportantExcerpt::new(&novel);
    println!("[结构体生命周期] {}", excerpt.announce_and_return("注意！"));

    // --- 静态生命周期 ---
    let s: &'static str = "我是静态字符串，存活整个程序"; // 字符串字面量是 'static
    println!("[静态生命周期] {}", s);

    // --- 生命周期省略规则演示 ---
    // 规则1: 每个引用参数有自己的生命周期
    // 规则2: 只有一个输入生命周期参数时，赋给所有输出
    // 规则3: 方法中 &self 的生命周期赋给所有输出
    let word = first_word("hello world");
    println!("[生命周期省略] 第一个词: {}", word);

    // --- 泛型 + Trait Bound + 生命周期 ---
    let a = String::from("abc");
    let b = String::from("defgh");
    let ann = "比较两个字符串";
    let result = longest_with_announcement(a.as_str(), b.as_str(), ann);
    println!("[泛型+生命周期] 较长的: {}", result);
}

// 显式生命周期标注：返回值的生命周期与两个参数中较短的那个相同
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// 结构体持有引用时必须标注生命周期
struct ImportantExcerpt<'a> {
    part: &'a str,
}

impl<'a> ImportantExcerpt<'a> {
    fn new(text: &'a str) -> Self {
        let first_sentence = text.split('。').next().unwrap_or(text);
        ImportantExcerpt { part: first_sentence }
    }

    // 规则3：&self 的生命周期自动赋给返回值
    fn announce_and_return(&self, announcement: &str) -> &str {
        println!("  公告: {}", announcement);
        self.part
    }
}

// 生命周期省略：编译器自动推断
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &byte) in bytes.iter().enumerate() {
        if byte == b' ' {
            return &s[..i];
        }
    }
    s
}

// 泛型 + Trait Bound + 生命周期 一起使用
fn longest_with_announcement<'a, T>(x: &'a str, y: &'a str, ann: T) -> &'a str
where
    T: std::fmt::Display,
{
    println!("  公告: {}", ann);
    if x.len() > y.len() { x } else { y }
}
