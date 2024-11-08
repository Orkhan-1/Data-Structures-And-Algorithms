import java.util.HashMap;

public class Solution {
    public int climbStairs(int n) {
        HashMap<Integer, Integer> memo = new HashMap<>();
        return climbStairsHelper(n, memo);
    }

    private int climbStairsHelper(int n, HashMap<Integer, Integer> memo) {
        if (n == 1) {
            return 1;
        }

        if (!memo.containsKey(n)) {
            memo.put(n, climbStairsHelper(n - 1, memo) + climbStairsHelper(n - 2, memo));
        }

        return memo.get(n);
    }
}
