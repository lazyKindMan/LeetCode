from random import choice

import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = RandomizedSet()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class RandomizedSet:

    def __init__(self):
        self.ele = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.ele)
        self.ele.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.ele[id] = self.ele[-1]
        self.ele.pop()
        self.indices[self.ele[id]] = id
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.ele)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
