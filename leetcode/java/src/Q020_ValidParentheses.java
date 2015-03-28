import java.util.Stack;
import java.util.HashMap;

public class Q020_ValidParentheses {

    /**
     * Given a string containing just the characters '(', ')', '{', '}', '[', and ']',
     * determine if the input string is valid.
     *
     * The brackets must close in the correct order. "()" and "()[]{}" are all valid,
     * but "(]" and "([)]" are not.
     */

    public static void main(String[] args) {
        String s = "((()())())";
        System.out.println(isValid(s));
    }

    // Use stack to balance a left parenthesis when a right one is seen.
    // One pass, thus O(n) complexity in time and space.
    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        HashMap<Character, Character> parentheses = new HashMap<Character, Character>();
        parentheses.put(')', '(');
        parentheses.put(']', '[');
        parentheses.put('}', '{');
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (parentheses.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != parentheses.get(c))
                    return false;
            } else
                stack.push(c);
        }
        return stack.isEmpty();
    }

}
