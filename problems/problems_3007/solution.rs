use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_maximum_number(k: i64, x: i32) -> i64 {

    }
}

#[cfg(feature = "solution_3007")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let k: i64 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let x: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_maximum_number(k, x))
}
