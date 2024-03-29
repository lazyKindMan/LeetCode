import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSum(test_input)

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
        self.indices[self.ele[id]] = id
        self.ele.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.ele)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()