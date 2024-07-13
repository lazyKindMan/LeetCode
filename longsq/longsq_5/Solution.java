package longsq.longsq_5;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String longestPalindrome(String s) {
        if (s == null || s.isEmpty()) return s;
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int start = 0, end = 0, maxPalindromeLength = 1;
        for (int r = 1; r < n; r++) {
            for (int l = 0; l <= r; l++) {
                if (s.charAt(l) == s.charAt(r) && (r - l + 1 <= 2 || dp[l + 1][r - 1])) {
                    dp[l][r] = true;
                    if (r - l + 1 > maxPalindromeLength) {
                        maxPalindromeLength = r - l + 1;
                        start = l;
                        end = r;
                    }
                }
            }
        }
        return s.substring(start, end + 1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(longestPalindrome(s));
    }
}
