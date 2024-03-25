import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
       return self.minSubArrayLen(test_input[0], test_input[1])

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, sum_num, ans, n = 0, 0, 0, int(1e5) + 1, len(nums)
        while end < n:
            sum_num += nums[end]
            while sum_num >= target:
                ans = min(ans, end - start + 1)
                sum_num -= nums[start]
                start += 1
            end += 1
        return ans if ans != (int(1e5) + 1) else 0




