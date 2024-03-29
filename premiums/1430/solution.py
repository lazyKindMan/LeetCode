import solution
from typing import *
from object_libs import list_to_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, arr = test_input
        root0 = list_to_tree(nums0)
        return self.isValidSequence(root0, arr)

    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
            pass