package longsq.longsq_7;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int reverse(int x) {
        int res = 0;
        int maxValue = Integer.MAX_VALUE / 10;
        int positiveMaxPos = Integer.MAX_VALUE % 10;
        int negativeMinPost = -1 - positiveMaxPos;
        while (x != 0) {
             if (x / 10 == 0) {
                 if (res > maxValue || res < -maxValue || (res == maxValue && x > positiveMaxPos) || res == -maxValue && x < negativeMinPost) {
                     return 0;
                 }
             }
             res = res * 10 + (x % 10);
             x = x / 10;
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int x = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(reverse(x));
    }
}
