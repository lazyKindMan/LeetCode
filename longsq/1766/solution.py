from collections import defaultdict
from math import gcd

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getCoprimes(*test_input)

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        graph = defaultdict(list)
        ans = [-1] * n
        for a, b in edges:
            graph[a].append(b)
        def dfs(root: int, parent_path: list) -> None:
            for x in range(len(parent_path) - 1, -1, -1):
                node, value = parent_path[x]
                if gcd(nums[root], value) == 1:
                    ans[root] = node
                    break
            if root in graph.keys():
                parent_path.append((root, nums[root]))
            for child in graph[root]:
                dfs(child, parent_path)
        dfs(0, list())
        return ans
