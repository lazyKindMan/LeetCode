#include "cpp/common/Solution.h"
#include <iostream>

using namespace std;
using json = nlohmann::json;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        int n = nums.size();
        for (int i = 0; i < n; ++i)
        {
            for (int j = i + 1; j < n; ++j)
            {
                if (nums[i] + nums[j] == target)
                {
                    return {i, j};
                }
            }
        }
        return {};
    }
};

json leetcode::qubh::Solve(string input)
{
    Solution solution;
    vector<string> res;
    int pos = input.find("\n");
    while (pos != string::npos) {
        res.push_back(input.substr(0, pos));
        std::cout << res[0] << std::endl;
        input = input.substr(pos + 1);
        pos = input.find("\n");
    }
    res.push_back(input);
    std::cout << res[1] << std::endl;

    int idx = input.find("\n");
    vector<int> nums = json::parse(res.at(0));
    int target = json::parse(res.at(1));
    json result = solution.twoSum(nums, target);
    return result;
}