from collections import defaultdict
from math import gcd

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getCoprimes(*test_input)

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # todo: sovle it at Apr 13
        gcds = defaultdict(set)
        for i in range(1, 51):
            gcds[i] = set()
            for key in gcds.keys():
                if key != i:
                    value = gcds[key]
                    if gcd(i, key) == 1:
                        value.add(i)



        print(gcds)