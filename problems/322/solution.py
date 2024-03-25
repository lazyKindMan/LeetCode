import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.coinChange(test_input[0], test_input[1])

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != -1:
                    dp[i] = min(dp[i], dp[i - coin] + 1) if dp[i] != -1 else dp[i - coin] + 1
        return dp[amount]
