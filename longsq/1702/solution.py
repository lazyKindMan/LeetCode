import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumBinaryString(test_input)

    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        last_zero_index = -1
        binary_list = list(binary)
        for i in range(n - 1):
            if binary_list[i] == '0':
                if binary_list[i + 1] == '0':
                    binary_list[i] = '1'
                    last_zero_index = i + 1
                else:
                    last_zero_index = i
            else:
                if binary_list[i + 1] == '0' and last_zero_index != -1:
                    binary_list[i + 1] = '1'
                    binary_list[last_zero_index] = '1'
                    binary_list[last_zero_index + 1] = '0'
                    last_zero_index += 1
        return ''.join(binary_list)