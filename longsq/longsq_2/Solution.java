package longsq.longsq_2;

import com.alibaba.fastjson.JSON;
import java.util.*;
import java.util.concurrent.ScheduledThreadPoolExecutor;
import java.util.concurrent.ThreadFactory;
import java.util.concurrent.ThreadPoolExecutor;

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

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int pos = 0;
        ListNode cur = null;
        ListNode res = null;
        while (l1 != null || l2 != null) {
            int val = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + pos;
            if (cur == null) {
                cur = new ListNode(val % 10);
                res = cur;
            } else {
                cur.next = new ListNode(val % 10);
                cur = cur.next;
            }
            pos = val / 10;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        if (pos == 1) cur.next = new ListNode(pos);
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode l1 = jsonArrayToListNode(inputJsonValues[0]);
		ListNode l2 = jsonArrayToListNode(inputJsonValues[1]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(addTwoNumbers(l1, l2)));
    }
}
