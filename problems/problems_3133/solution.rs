use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_end(n: i32, x: i32) -> i64 {

    }
}

#[cfg(feature = "solution_3133")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let x: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_end(n, x))
}