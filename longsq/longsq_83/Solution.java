package longsq.longsq_83;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import qubhjava.models.ListNode;

public class Solution extends BaseSolution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;
        ListNode pre = head, after = head.next;
        while (after != null) {
            if (pre.val == after.val) {
                after = after.next;
            } else {
                pre.next = after;
                pre = pre.next;
                after = after.next;
            }
        }
        pre.next = after;
        return head;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(deleteDuplicates(head)));
    }
}
