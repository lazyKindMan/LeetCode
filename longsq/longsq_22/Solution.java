package longsq.longsq_22;

import com.alibaba.fastjson.JSON;
import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> generateParenthesis(int n) {
        Queue<StringBuilder> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (queue.isEmpty()) {
                queue.add(new StringBuilder("()"));
            } else {
                int size = queue.size();
                for (int j = 0; j < size; j++) {
                    StringBuilder sb = queue.poll();
                    for (int l = 0; l < sb.length(); l ++) {
                        if (l == 0) {
                            queue.add(new StringBuilder("()").append(sb));
                        }
                        if (sb.charAt(l) == '(') {
                            queue.add(new StringBuilder(sb.substring(0, l + 1)).append("()").append(sb.substring(l + 1, sb.length())));
                        }
                    }
                }
            }
        }
        return queue.stream().map(StringBuilder::toString).toList();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(generateParenthesis(n));
    }
}
