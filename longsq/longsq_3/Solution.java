package longsq.longsq_3;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if (n <= 1) {
            return n;
        }
        Set<Character> set = new HashSet<>();
        set.add(s.charAt(n - 1));
        int start = n - 2,  end = n - 1;
        int res = 0;
        for (int i = n - 2; i >= 0; i--){
            while (start < end && set.contains(s.charAt(i))) {
                set.remove(s.charAt(end --));
            }
            set.add(s.charAt(i));
            start --;
            if (end - start > res) {
                res  = end - start;
            }
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(lengthOfLongestSubstring(s));
    }
}
