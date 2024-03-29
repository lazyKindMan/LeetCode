import solution
from typing import *

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.firstDayBeenInAllRooms(test_input)

    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        dp[0] = 1
        ans = 0
        mod = 10 ** 9 + 7
        for e in nextVisit[1:]:
            if dp[e] > 0:
                dp[e] += 1
            else:
                dp[e] = 1
                dp[e - 1] += 1
        for d in dp:
            ans = (ans + d) % mod
        return ans
