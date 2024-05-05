import solution
from typing import *
from python.object_libs import list_to_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        return self.equalToDescendants(root0)

    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
            pass