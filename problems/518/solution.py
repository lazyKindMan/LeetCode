import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.change(test_input[0], test_input[1])

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


        # timeout
        # n = len(coins)
        # end = n - 1
        # ans = 0
        # coins.sort()
        # def get_combine(amount: int, end: int, coins: List[int]):
        #     nonlocal ans
        #     if end < 0 or amount < 0:
        #         return
        #     while amount > 0:
        #         if end > 0:
        #             get_combine(amount, end - 1, coins)
        #         amount -= coins[end]
        #         if amount == 0:
        #             ans += 1
        #             return
        # get_combine(amount, end, coins)
        # return ans






