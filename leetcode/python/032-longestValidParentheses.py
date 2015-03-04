#!/usr/bin/python

# Given a string containing just the characters '(' and ')', find the length of the longest valid
# (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Dynamic programming - d[i] indicates the length of the longest parentheses starting at s[i].
#   If s[i] == ')', then d[i] = 0.
#   If s[i] == '(', then j = i + 1 + d[i + 1]
#       if s[j] == ')', then d[i] = d[i + 1] + 2 + d[j + 1]
#       otherwise, d[i] == 0
# Maintain such d from right to left and return max(d), thus O(n)
def longestValidParentheses(s):
    if not s or len(s) < 2:
        return 0
    d = [0 for i in range(len(s))]
    for i in range(len(s) - 2, -1, -1):
        if s[i] == '(':
            j = i + 1 + d[i + 1]
            if j < len(s) and s[j] == ')':
                d[i] = d[i + 1] + 2
                if j < len(s) - 1:
                    d[i] = d[i] + d[j + 1]
    return max(d)

def main():
    s = '(()'
    print longestValidParentheses(s)

main()
