import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = ThroneInheritance(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.edges = {kingName: list()}
        self.dead = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.edges:
            return
        self.edges[parentName].append(childName)
        self.edges[childName] = list()

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []

        def dfs(parentName: str) -> None:
            nonlocal ans
            if parentName not in self.dead:
                ans.append(parentName)
            for child in self.edges[parentName]:
                dfs(child)
        dfs(self.kingName)
        return ans

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
