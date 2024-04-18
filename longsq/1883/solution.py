import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSkips(*test_input)

    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
                pass