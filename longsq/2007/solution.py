import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findOriginalArray(test_input)

     def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n == 0 or n % 2 != 0:
            return []
        changed = sorted(changed)
        ans = []
        last_scan_base = 0
        ans_len = 0
        for i in range(n):
            if changed[i] % 2 == 0 and ans_len > last_scan_base:
                if ans[last_scan_base] * 2 == changed[i]:
                    last_scan_base += 1
                else:
                    ans.append(changed[i])
                    ans_len += 1
            else:
                ans.append(changed[i])
                ans_len += 1
            if ans_len * 2 > n:
                return []
        return ans