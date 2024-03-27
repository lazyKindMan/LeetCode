import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countWays(test_input)

    def countWays(self, ranges: List[List[int]]) -> int:
        # Especially when the goal is to solve a counting problem, it is not necessary to consider the specific details; just focus on the counting aspect
        ranges.sort()
        cnt = 0
        right = -1
        for st, ed in ranges:
            if st > right:
                cnt += 1
            right = max(ed, right)
        mod = 10 ** 9 + 7
        return pow(2, cnt, mod)
