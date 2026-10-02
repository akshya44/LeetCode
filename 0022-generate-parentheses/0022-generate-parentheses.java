import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();

        backtrack(result, new StringBuilder(), 0, 0, n);

        return result;
    }

    private void backtrack(List<String> result, StringBuilder current,
                            int open, int close, int n) {

        // A complete valid combination is formed.
        if (current.length() == 2 * n) {
            result.add(current.toString());
            return;
        }

        // We can add an opening bracket if we still have some left.
        if (open < n) {
            current.append('(');
            backtrack(result, current, open + 1, close, n);
            current.deleteCharAt(current.length() - 1);
        }

        // We can add a closing bracket only when there
        // is an unmatched opening bracket.
        if (close < open) {
            current.append(')');
            backtrack(result, current, open, close + 1, n);
            current.deleteCharAt(current.length() - 1);
        }
    }
}