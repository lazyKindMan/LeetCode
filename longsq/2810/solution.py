import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.finalString(test_input)

    def finalString(self, s: str) -> str:
            ans = ''
            for c in s:
                if c == 'i':
                    ans = ans[::-1]
                else:
                    ans += 'c'
                print(ans)
            return ans

