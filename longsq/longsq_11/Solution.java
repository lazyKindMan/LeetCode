package longsq.longsq_11;

import com.alibaba.fastjson.JSON;
import java.util.*;

import com.beust.ah.A;
import com.sun.source.tree.Tree;
import qubhjava.BaseSolution;
import qubhjava.models.ListNode;


public class Solution extends BaseSolution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int res = 0;
        while (left < right) {
            int tmpRes = Math.min(height[left], height[right]) * (right - left);
            if (res < tmpRes) {
                res = tmpRes;
            }
            if (height[right] > height[left]) {
                left ++;
            } else {
                right --;
            }
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] height = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxArea(height));
    }
}
