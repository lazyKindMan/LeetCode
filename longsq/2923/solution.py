from itertools import count

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findChampion(test_input)

    def findChampion(self, grid: List[List[int]]) -> int:
        maxChampion = 0
        for i in range(1, len(grid)):
            if grid[i][maxChampion] == 1:
                maxChampion = i
        return maxChampion