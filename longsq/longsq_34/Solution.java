package longsq.longsq_34;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int lower_bound(int[] nums, int target) {
        int n = nums.length;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        int start = lower_bound(nums, target);
        if (start >= n || nums[start] != target) {
            return new int[]{-1, -1};
        }
        int end = lower_bound(nums, target + 1) - 1;
        return new int[]{start, end};
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(searchRange(nums, target));
    }
}
