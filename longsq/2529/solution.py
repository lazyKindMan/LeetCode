import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumCount(test_input)

    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        def find_zero(target: int) -> int:
            l, r = 0, n -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            return l
        pos = n - find_zero(1)
        neg = find_zero(0)
        print(find_zero(1), neg)
        return max(neg, pos)
