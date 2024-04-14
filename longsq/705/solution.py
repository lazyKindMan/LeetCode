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
        self.base = 769
        self.data = [list()] * self.base

    def add(self, key: int) -> None:
        hash_key = key % self.base
        if key not in self.data[hash_key]:
            self.data[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.base
        data_list = self.data[hash_key]
        if key not in data_list:
            return
        data_list.remove(key)

    def contains(self, key: int) -> bool:
        hash_key = key % self.base
        data_list = self.data[hash_key]
        return False if key not in data_list else True