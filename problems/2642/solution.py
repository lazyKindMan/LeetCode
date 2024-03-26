import heapq
from collections import defaultdict
from math import inf

import solution
from typing import *

from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Graph(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(list)
        self.n = n
        for s, e, c in edges:
            self.g[s].append((e, c))

    def addEdge(self, edge: List[int]) -> None:
        s, e, c = edge[0], edge[1], edge[2]
        self.g[s].append((e, c))


    def shortestPath(self, node1: int, node2: int) -> int:
        h = [(0, node1)]
        dp = [inf] * self.n
        dp[node1] = 0
        while h:
            cost, vertex = heapq.heappop(h)
            if cost > dp[vertex]:
                continue
            for neighbor, neighbor_cost in self.g[vertex]:
                if dp[neighbor] > neighbor_cost + cost:
                    dp[neighbor] = neighbor_cost + dp[vertex]
                    heapq.heappush(h, (dp[neighbor], neighbor))
        ans = dp[node2] if dp[node2] != inf else -1
        print(ans)
        return dp[node2] if dp[node2] != inf else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
