/// 智能指针 - Box、Rc、RefCell

use std::cell::RefCell;
use std::rc::Rc;

// --- Box：堆上分配 ---
// 常用于递归类型
#[derive(Debug)]
enum List {
    Cons(i32, Box<List>),
    Nil,
}

// --- Rc + RefCell：共享可变性 ---
#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}

pub fn demo() {
    // --- Box：在堆上存储数据 ---
    let b = Box::new(42);
    println!("[Box] 值: {}", b);

    // Box 递归类型：链表
    let list = List::Cons(1,
        Box::new(List::Cons(2,
            Box::new(List::Cons(3,
                Box::new(List::Nil))))));
    println!("[Box 链表] {:?}", list);

    // --- Rc：引用计数共享所有权 ---
    let shared = Rc::new(String::from("共享数据"));
    let r1 = Rc::clone(&shared);
    let r2 = Rc::clone(&shared);
    println!("[Rc] 引用计数: {}", Rc::strong_count(&shared));
    println!("[Rc] r1={}, r2={}", r1, r2);
    drop(r1);
    println!("[Rc] drop r1 后引用计数: {}", Rc::strong_count(&shared));

    // --- RefCell：运行时借用检查 ---
    let data = RefCell::new(vec![1, 2, 3]);
    // 运行时可变借用
    data.borrow_mut().push(4);
    println!("[RefCell] {:?}", data.borrow());

    // --- Rc + RefCell 组合：共享可变数据 ---
    let parent = Rc::new(Node {
        value: 1,
        children: RefCell::new(vec![]),
    });

    let child1 = Rc::new(Node {
        value: 2,
        children: RefCell::new(vec![]),
    });

    let child2 = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    // 通过 RefCell 在运行时修改 children
    parent.children.borrow_mut().push(Rc::clone(&child1));
    parent.children.borrow_mut().push(Rc::clone(&child2));

    println!("[Rc+RefCell] 父节点: {}, 子节点数: {}",
        parent.value,
        parent.children.borrow().len());

    for child in parent.children.borrow().iter() {
        println!("[Rc+RefCell]   子节点: {}", child.value);
    }
}
