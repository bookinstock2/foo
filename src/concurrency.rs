/// 并发 - 线程、消息传递、共享状态

use std::sync::{Arc, Mutex};
use std::thread;
use std::sync::mpsc;

pub fn demo() {
    // --- 基本线程 ---
    let handle = thread::spawn(|| {
        let mut sum = 0;
        for i in 1..=100 {
            sum += i;
        }
        sum
    });
    let result = handle.join().unwrap();
    println!("[线程] 1+2+...+100 = {}", result);

    // --- move 闭包捕获所有权 ---
    let data = vec![1, 2, 3];
    let handle = thread::spawn(move || {
        // data 的所有权被 move 到线程中
        let sum: i32 = data.iter().sum();
        sum
    });
    // println!("{:?}", data); // ❌ data 已被 move
    println!("[move] 线程内求和: {}", handle.join().unwrap());

    // --- 消息传递 (mpsc channel) ---
    let (tx, rx) = mpsc::channel();
    let tx2 = tx.clone(); // 多个发送者

    thread::spawn(move || {
        tx.send("来自线程1的消息").unwrap();
    });

    thread::spawn(move || {
        tx2.send("来自线程2的消息").unwrap();
    });

    for _ in 0..2 {
        let msg = rx.recv().unwrap();
        println!("[channel] 收到: {}", msg);
    }

    // --- 共享状态 (Arc + Mutex) ---
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..5 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
    println!("[Arc+Mutex] 计数器: {}", *counter.lock().unwrap());
}
