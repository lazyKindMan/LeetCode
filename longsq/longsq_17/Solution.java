package longsq.longsq_17;

import com.alibaba.fastjson.JSON;
import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    static Map<Integer, String> map = new HashMap<>();
    static {
        map.put(2, "abc");
        map.put(3, "def");
        map.put(4, "ghi");
        map.put(5, "jkl");
        map.put(6, "mno");
        map.put(7, "pqrs");
        map.put(8, "tuv");
        map.put(9, "wxyz");
    }

    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits.length() <= 0) return res;
        combinationString(0, null, digits, res);
        return res;
    }

    private void combinationString(int dept, StringBuilder sb, String digits, List<String> res) {
        if (dept == digits.length()) {
            res.add(sb == null ? "" : sb.toString());
            return;
        }
        for (char c : map.get(digits.charAt(dept) - '0').toCharArray()) {
            if (sb == null) {
                combinationString(dept + 1, new StringBuilder().append(c), digits, res);
            } else {
                combinationString(dept + 1, sb.append(c), digits, res);
                sb.deleteCharAt(dept);
            }
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String digits = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(letterCombinations(digits));
    }
}
