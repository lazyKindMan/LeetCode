import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums_arr = test_input
        heads = [list_to_linked_list(nums) for nums in nums_arr]
        res = self.sortLinkedList(heads)
        return linked_list_to_list(res)

    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            pass