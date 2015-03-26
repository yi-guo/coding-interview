import java.util.HashMap;

public class Q076_MinimumWindowSubstring {

    /**
     * Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
     *
     * For example,
     *   S = "ADOBECODEBANC"
     *   T = "ABC"
     *   Minimum window is "BANC".
     *
     * Note:
     * 1. If there is no such window in S that covers all characters in T, return the empty string "".
     * 2. If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
     *
     */

    public static void main(String[] args) {
        String S = "ADOBECODEBANC";
        String T = "ABC";
        System.out.println(minWindow(S, T));
    }

    public static String minWindow(String S, String T) {
        if (S == null || T == null || S.length() < T.length())
            return "";
        HashMap<Character, Integer> targetCounter = new HashMap<Character, Integer>();
        for (int i = 0; i < T.length(); i++) {
            char c = T.charAt(i);
            if (targetCounter.containsKey(c))
                targetCounter.put(c, targetCounter.get(c) + 1);
            else
                targetCounter.put(c, 1);
        }
        int j = 0, length = 0;
        String minWindow = S;
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            if (targetCounter.containsKey(c)) {
                if (targetCounter.get(c) > 0)
                    length = length + 1;
                targetCounter.put(c, targetCounter.get(c) - 1);
                if (length >= T.length()) {
                    while (j < i - T.length()) {
                        if (targetCounter.containsKey(S.charAt(j)) && targetCounter.get(S.charAt(j)) == 0)
                            break;
                        j = j + 1;
                    }
                    String window = S.substring(j, i + 1);
                    if (window.length() < minWindow.length())
                        minWindow = window;
                }
            }
        }
        return minWindow;
    }

}
