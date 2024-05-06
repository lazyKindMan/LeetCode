import heapq
import math

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSkips(*test_input)

    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        costs = []
        skip_heap = []
        for dis in dist[:-1]:
            cost = dis / speed
            costs.append(math.ceil(cost))
            if not self.is_integer(cost):
                heapq.heappush(skip_heap, costs[-1] - cost)
        costs.append(costs[-1] / speed)
        no_skip_sum = sum(costs)
        ans = 0
        if no_skip_sum <= hoursBefore:
            return ans
        while skip_heap and no_skip_sum > hoursBefore:
            no_skip_sum -= heapq.heappop(skip_heap)
            ans += 1
        return ans if no_skip_sum <= hoursBefore else -1

    def is_integer(self, num):
        return abs(num - round(num)) < 0.0000001
