package longsq.longsq_16;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int res = 0;
        int minDiffer = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length - 2; i++) {
            if(i > 0 && nums[i - 1] == nums[i]) continue;
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                int differ = target - sum;
                if (minDiffer > Math.abs(differ)) {
                    minDiffer = Math.abs(differ);
                    res = sum;
                }
                if (differ > 0) {
                    for (left = left + 1; left < right && nums[left - 1] == nums[left]; left++);
                } else if (differ < 0) {
                    for (right = right - 1; left < right && nums[right + 1] == nums[right]; right--);
                } else {
                    break;
                }
            }
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(threeSumClosest(nums, target));
    }
}
