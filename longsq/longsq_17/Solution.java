package longsq.longsq_17;

import com.alibaba.fastjson.JSON;
import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static String[] mapping = new String[] {
            "", "", "abc", "def", "ghi", "jkl", "mon", "pqrs", "tuv", "wxyz",
    };

    public List<String> letterCombinations(String digits) {
        List<String> ans = new ArrayList<>();
        int n = digits.length();
        if (n <= 0) {
            return ans;
        }
        dfs(0, n, "", digits, ans);
        return ans;
    }

    private void dfs(int deep, int n, String current, String digits, List<String> res) {
        if (deep == n) {
            res.add(current);
            return;
        }
        for (char c : mapping[digits.charAt(deep) - '0'].toCharArray()) {
            dfs(deep + 1,n, current + c, digits, res);
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String digits = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(letterCombinations(digits));
    }
}
