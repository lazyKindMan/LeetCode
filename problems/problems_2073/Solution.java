package problems.problems_2073;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int timeRequiredToBuy(int[] tickets, int k) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] tickets = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(timeRequiredToBuy(tickets, k));
    }
}