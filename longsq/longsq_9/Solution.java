package longsq.longsq_9;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int cur = 0;
        for (int tmp = x; tmp != 0; tmp = tmp / 10) {
            cur = cur * 10 + tmp % 10;
        }
        return x == cur;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int x = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(isPalindrome(x));
    }
}
