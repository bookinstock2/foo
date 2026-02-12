/// 结构体与枚举 - Rust 的自定义类型系统

// --- 结构体 ---
#[derive(Debug)]
struct User {
    name: String,
    age: u32,
    active: bool,
}

impl User {
    // 关联函数（类似构造器）
    fn new(name: &str, age: u32) -> Self {
        User {
            name: String::from(name),
            age,
            active: true,
        }
    }

    // 方法（&self 不可变借用）
    fn info(&self) -> String {
        format!("{}, {}岁, {}", self.name, self.age,
            if self.active { "活跃" } else { "不活跃" })
    }

    // 方法（&mut self 可变借用）
    fn deactivate(&mut self) {
        self.active = false;
    }
}

// --- 枚举 ---
#[derive(Debug)]
enum Shape {
    Circle(f64),              // 圆：半径
    Rectangle(f64, f64),      // 矩形：宽、高
    Triangle { base: f64, height: f64 }, // 三角形：命名字段
}

impl Shape {
    fn area(&self) -> f64 {
        match self {
            Shape::Circle(r) => std::f64::consts::PI * r * r,
            Shape::Rectangle(w, h) => w * h,
            Shape::Triangle { base, height } => 0.5 * base * height,
        }
    }

    fn name(&self) -> &str {
        match self {
            Shape::Circle(_) => "圆",
            Shape::Rectangle(_, _) => "矩形",
            Shape::Triangle { .. } => "三角形",
        }
    }
}

// --- Option 枚举的使用 ---
fn find_user(name: &str) -> Option<User> {
    match name {
        "alice" => Some(User::new("Alice", 30)),
        _ => None,
    }
}

pub fn demo() {
    // 结构体
    let mut user = User::new("Dede", 25);
    println!("[结构体] {}", user.info());
    user.deactivate();
    println!("[方法修改] {}", user.info());
    println!("[Debug] {:?}", user);

    // 枚举与模式匹配
    let shapes = vec![
        Shape::Circle(5.0),
        Shape::Rectangle(4.0, 6.0),
        Shape::Triangle { base: 3.0, height: 8.0 },
    ];

    for shape in &shapes {
        println!("[枚举] {} 的面积 = {:.2}", shape.name(), shape.area());
    }

    // if let 语法糖
    if let Some(user) = find_user("alice") {
        println!("[Option + if let] 找到用户: {}", user.info());
    }
    if let None = find_user("bob") {
        println!("[Option + if let] 未找到用户 bob");
    }
}
