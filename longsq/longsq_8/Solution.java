package longsq.longsq_8;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    int MAX_INTEGER_VALUE = Integer.MAX_VALUE / 10;
    int MAX_POSITIVE_POS = Integer.MAX_VALUE % 10;
    public boolean isDigital(char c) {
        return c - '0' >= 0 && c - '0' <= 9;
    }
    public int myAtoi(String s) {
        s = s.trim();
        if (s.isEmpty()) return 0;
        int hasSign=0, sign = 1, res = 0;
        char[] arr = s.toCharArray();
        if (arr[0] == '-') { sign = -1; hasSign = 1;} else if (arr[0] == '+') {hasSign = 1;}
        for (int i = hasSign; i < arr.length; i++) {
            if (!isDigital(arr[i])) break;
            int pos = arr[i] - '0';
            if (res > MAX_INTEGER_VALUE || (res == MAX_INTEGER_VALUE && pos > MAX_POSITIVE_POS)) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            } else {
                res = res * 10 + pos;
            }
        }
        return res * sign;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(myAtoi(s));
    }
}
