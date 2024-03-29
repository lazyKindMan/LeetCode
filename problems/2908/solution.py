import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSum(test_input)

    def minimumSum(self, nums: List[int]) -> int:
        # O(n^2)
        ans, n = -1, len(nums)
        # min_i = nums[0]
        # for j in range(1, n - 1):
        #     if min_i < nums[j]:
        #         for k in range(j + 1, n):
        #             if nums[k] < nums[j]:
        #                 temp = nums[k] + nums[j] + min_i
        #                 ans = temp if ans == -1 or temp < ans else ans
        #     min_i = min(min_i, nums[j])
        #
        # Maintain a minimal suffix, and then scan from front to back. Time complexity O(n)
        suf = [0] * (n - 1) + [nums[n - 1]]
        min_i = nums[0]
        for k in range(n - 2, 0, -1):
            suf[k] = min(nums[k], suf[k + 1])
        for j in range(1, n - 1):
            if min_i < nums[j] and nums[j] > suf[j]:
                temp = nums[j] + suf[j] + min_i
                ans = temp if ans == -1 or temp < ans else ans
            min_i = min(min_i, nums[j])
        return ans

