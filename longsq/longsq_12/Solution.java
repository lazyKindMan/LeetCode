package longsq.longsq_12;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    static TreeMap<Integer, String> romanNumberMap = new TreeMap<>((a, b) -> b - a); 
    static {
        romanNumberMap.put(1, "IXCM");
        romanNumberMap.put(5, "VLD");
    }
    
    public String intToRoman(int num) {
        char[] charArr = String.valueOf(num).toCharArray();
        StringBuilder resBuilder = new StringBuilder();
        for (int i = 0; i < charArr.length; i++) {
            int pos = charArr.length - i - 1;
            int val = charArr[i] - '0';
            if (romanNumberMap.containsKey(val)) {
                resBuilder.append(romanNumberMap.get(val).charAt(pos));
            } else if (val == 4){
                resBuilder.append(romanNumberMap.get(1).charAt(pos))
                        .append(romanNumberMap.get(5).charAt(pos));
            } else if (val == 9) {
                resBuilder.append(romanNumberMap.get(1).charAt(pos))
                        .append(romanNumberMap.get(1).charAt(pos + 1));
            } else {
                if (val > 5) { val = val - 5; resBuilder.append(romanNumberMap.get(5).charAt(pos));}
                for (int j = 0 ; j < val; j++) {
                    resBuilder.append(romanNumberMap.get(1).charAt(pos));
                }
            }
        }
        return resBuilder.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(intToRoman(num));
    }
}
