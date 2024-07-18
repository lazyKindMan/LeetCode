package longsq.longsq_237;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import qubhjava.models.ListNode;

public class Solution extends BaseSolution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode node = jsonArrayToListNode(inputJsonValues[0]);
		deleteNode(node);
        return JSON.toJSON(node);
    }
}
