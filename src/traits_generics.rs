/// Trait 与泛型 - Rust 的多态与抽象

use std::fmt;

// --- 定义 Trait ---
trait Summary {
    fn summarize(&self) -> String;

    // 带默认实现的方法
    fn preview(&self) -> String {
        format!("{}...", &self.summarize()[..20.min(self.summarize().len())])
    }
}

// --- 不同类型实现同一 Trait ---
struct Article {
    title: String,
    content: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("《{}》: {}", self.title, self.content)
    }
}

struct Tweet {
    user: String,
    text: String,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("@{}: {}", self.user, self.text)
    }
}

// --- 泛型函数 + Trait Bound ---
fn print_summary<T: Summary>(item: &T) {
    println!("[Trait Bound] {}", item.summarize());
}

// --- where 语法 ---
fn compare_and_print<T>(a: &T, b: &T)
where
    T: Summary + fmt::Debug,
{
    println!("[where] a={}, b={}", a.summarize(), b.summarize());
}

// --- 返回 impl Trait ---
fn create_summarizable() -> impl Summary {
    Tweet {
        user: String::from("rustlang"),
        text: String::from("Rust 1.93 released!"),
    }
}

// --- 泛型结构体 ---
#[derive(Debug)]
struct Pair<T> {
    first: T,
    second: T,
}

impl<T: fmt::Display + PartialOrd> Pair<T> {
    fn larger(&self) -> &T {
        if self.first >= self.second {
            &self.first
        } else {
            &self.second
        }
    }
}

// 为 Tweet 实现 Debug（供 compare_and_print 使用）
impl fmt::Debug for Tweet {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Tweet(@{})", self.user)
    }
}

impl fmt::Debug for Article {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Article({})", self.title)
    }
}

pub fn demo() {
    let article = Article {
        title: String::from("Rust 入门"),
        content: String::from("Rust 是一门系统编程语言"),
    };

    let tweet = Tweet {
        user: String::from("dede"),
        text: String::from("学 Rust 真有意思！"),
    };

    // Trait 方法
    println!("[Trait] {}", article.summarize());
    println!("[Trait] {}", tweet.summarize());

    // 泛型函数
    print_summary(&article);
    print_summary(&tweet);

    // where 子句
    compare_and_print(&tweet, &Tweet {
        user: String::from("sei"),
        text: String::from("确实！🦀"),
    });

    // impl Trait 返回
    let item = create_summarizable();
    println!("[impl Trait] {}", item.summarize());

    // 泛型结构体
    let pair = Pair { first: 10, second: 25 };
    println!("[泛型] 较大值: {}", pair.larger());
}
