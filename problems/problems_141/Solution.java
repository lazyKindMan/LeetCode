package problems.problems_141;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import qubhjava.models.ListNode;

public class Solution extends BaseSolution {
    public boolean hasCycle(ListNode head) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        ListNode head = jsonArrayToListNode(inputJsonValues[0]);
        return JSON.toJSON(hasCycle(head));
    }
}
