package longsq.longsq_162;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


/**
 * it proves that not only sorted array can use the binary search
 * it may be used when the array has it’s own local rules
 */
public class Solution extends BaseSolution {
    public int findPeakElement(int[] nums) {
        int n = nums.length;
        int left = 0, right = n - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[mid + 1]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(findPeakElement(nums));
    }
}
