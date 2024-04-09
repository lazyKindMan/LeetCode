import array

import solution
from typing import *

'''
This problem can be solved by the Sliding Window.
The key problem is that you should find a baseline interval which can contains the most number of elements in given array 
So you can use sliding window to find this baseline interval. 
'''


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, nums: List[int]) -> int:
            n = len(nums)
            a = sorted(set(nums))
            ans = left = 0
            for i, x in enumerate(a):
                while a[left] < x - n + 1:
                    left += 1
                ans = max(ans, i - left + 1)
            return n - ans

