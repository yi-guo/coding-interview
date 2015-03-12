import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {
	
	public static void main(String[] args) {
		String s = "((()())())";
		System.out.println(isValid(s));
	}
	
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
