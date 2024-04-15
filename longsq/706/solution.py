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
        self.base = 768
        self.data = [dict()] * self.base

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.base
        val_list = self.data[hash_key]
        val_list[key] = value

    def get(self, key: int) -> int:
        hash_key = key % self.base
        val_list = self.data[hash_key]
        return val_list[key] if key in val_list else -1

    def remove(self, key: int) -> None:
        hash_key = key % self.base
        val_list = self.data[hash_key]
        if key in val_list:
            val_list.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
