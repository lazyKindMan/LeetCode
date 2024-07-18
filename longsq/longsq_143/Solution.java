package longsq.longsq_143;

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
    private ListNode getMiddleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    private ListNode reverseList(ListNode head) {
        ListNode pre = null, cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }

    public void reorderList(ListNode head) {
        ListNode middle = getMiddleNode(head);
        ListNode head2 = reverseList(middle);
        ListNode head1 = head;
        while (head1 != middle && head2 != middle) {
            ListNode n1 = head1.next;
            ListNode n2 = head2.next;
            head1.next = head2;
            head2.next = n1;
            head1 = n1;
            head2 = n2;
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
		reorderList(head);
        return JSON.toJSON(head);
    }
}
