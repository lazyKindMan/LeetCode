package longsq.longsq_21;

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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null || list2 == null) return list1 == null ? list2 : list1;
        ListNode head = new ListNode(-101);
        ListNode cur = head;
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                cur.next = list1;
                cur = cur.next;
                list1 = list1.next;
                cur.next = null;
            } else {
                cur.next = list2;
                cur = cur.next;
                list2 = list2.next;
                cur.next = null;
            }
        }
        if (list1 != null) {
            cur.next = list1;
        } else {
            cur.next = list2;
        }
        return head.next;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode list1 = jsonArrayToListNode(inputJsonValues[0]);
		ListNode list2 = jsonArrayToListNode(inputJsonValues[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(mergeTwoLists(list1, list2)));
    }
}
