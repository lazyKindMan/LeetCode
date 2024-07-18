package longsq.longsq_19;

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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode pre = dummy, cur = dummy;
        while (n-- > 0 && cur.next != null) {
            cur = cur.next;
        }
        while (cur.next != null) {
            pre = pre.next;
            cur = cur.next;
        }
        if (pre.next == null) {
            return head;
        }
        pre.next = pre.next.next;
        return dummy.next;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(removeNthFromEnd(head, n)));
    }
}
