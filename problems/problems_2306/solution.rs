use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn distinct_names(ideas: Vec<String>) -> i64 {

    }
}

#[cfg(feature = "solution_2306")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let ideas: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::distinct_names(ideas))
}
