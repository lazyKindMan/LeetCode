import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MyHashSet()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class MyHashSet:

    def __init__(self):
        pass


    def add(self, key: int) -> None:
            pass


    def remove(self, key: int) -> None:
            pass


    def contains(self, key: int) -> bool:
            pass



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)