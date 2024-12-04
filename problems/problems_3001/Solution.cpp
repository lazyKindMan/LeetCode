//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        
    }
};

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	Solution solution;
	int a = json::parse(inputArray.at(0));
	int b = json::parse(inputArray.at(1));
	int c = json::parse(inputArray.at(2));
	int d = json::parse(inputArray.at(3));
	int e = json::parse(inputArray.at(4));
	int f = json::parse(inputArray.at(5));
	return solution.minMovesToCaptureTheQueen(a, b, c, d, e, f);
}
