import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MyHashMap()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class MyHashMap:

    def __init__(self):
        pass


    def put(self, key: int, value: int) -> None:
            pass


    def get(self, key: int) -> int:
            pass


    def remove(self, key: int) -> None:
            pass



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)