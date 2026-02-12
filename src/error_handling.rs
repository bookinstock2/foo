/// 错误处理 - Result、Option 和 ? 操作符

use std::num::ParseIntError;
use std::fmt;

// --- 自定义错误类型 ---
#[derive(Debug)]
enum AppError {
    ParseError(ParseIntError),
    ValidationError(String),
    NotFound(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            AppError::ParseError(e) => write!(f, "解析错误: {}", e),
            AppError::ValidationError(msg) => write!(f, "验证错误: {}", msg),
            AppError::NotFound(item) => write!(f, "未找到: {}", item),
        }
    }
}

impl From<ParseIntError> for AppError {
    fn from(e: ParseIntError) -> Self {
        AppError::ParseError(e)
    }
}

// --- 使用 Result ---
fn parse_age(input: &str) -> Result<u32, AppError> {
    let age: u32 = input.parse()?; // ? 自动转换错误类型（通过 From trait）
    if age > 150 {
        Err(AppError::ValidationError("年龄不能超过150".into()))
    } else {
        Ok(age)
    }
}

// --- 链式错误处理 ---
fn process_user_input(name: &str, age_str: &str) -> Result<String, AppError> {
    if name.is_empty() {
        return Err(AppError::NotFound("用户名为空".into()));
    }
    let age = parse_age(age_str)?; // ? 向上传播错误
    Ok(format!("{} 今年 {} 岁", name, age))
}

// --- Option 的常用方法 ---
fn demo_option() {
    let numbers = vec![1, 2, 3, 4, 5];

    // unwrap_or：提供默认值
    let sixth = numbers.get(5).unwrap_or(&0);
    println!("[unwrap_or] 第6个元素: {}", sixth);

    // map：转换 Option 内的值
    let first_doubled = numbers.first().map(|x| x * 2);
    println!("[map] 第一个元素翻倍: {:?}", first_doubled);

    // and_then：链式 Option
    let result = numbers.first()
        .and_then(|x| if *x > 0 { Some(x * 10) } else { None });
    println!("[and_then] 链式结果: {:?}", result);

    // filter
    let even_first = numbers.first().filter(|x| *x % 2 == 0);
    println!("[filter] 第一个偶数: {:?}", even_first);
}

pub fn demo() {
    // 成功的情况
    match process_user_input("Dede", "25") {
        Ok(msg) => println!("[Ok] {}", msg),
        Err(e) => println!("[Err] {}", e),
    }

    // 解析错误
    match process_user_input("Dede", "abc") {
        Ok(msg) => println!("[Ok] {}", msg),
        Err(e) => println!("[Err] {}", e),
    }

    // 验证错误
    match process_user_input("Dede", "200") {
        Ok(msg) => println!("[Ok] {}", msg),
        Err(e) => println!("[Err] {}", e),
    }

    // 未找到错误
    match process_user_input("", "25") {
        Ok(msg) => println!("[Ok] {}", msg),
        Err(e) => println!("[Err] {}", e),
    }

    // Option 演示
    demo_option();
}
