package longsq.longsq_13;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
   static Map<Character, Integer> romaNumberMap = new HashMap<>();
   static {
       romaNumberMap.put('I', 1);
       romaNumberMap.put('V', 5);
       romaNumberMap.put('X', 10);
       romaNumberMap.put('L', 50);
       romaNumberMap.put('C', 100);
       romaNumberMap.put('D', 500);
       romaNumberMap.put('M', 1000);
   }


    public int romanToInt(String s) {
        char[] chars = s.toCharArray();
        int res = 0;
        int preNum = romaNumberMap.get(chars[0]);
        for (int i = 1; i < s.length(); i++) {
            int cur = romaNumberMap.get(chars[i]);
            if (preNum < cur) {
                res -= preNum;
            } else {
                res += preNum;
            }
            preNum = cur;
        }
        res += preNum;
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(romanToInt(s));
    }
}
