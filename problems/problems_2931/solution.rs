use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_spending(values: Vec<Vec<i32>>) -> i64 {
        
    }
}

#[cfg(feature = "solution_2931")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let values: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::max_spending(values))
}