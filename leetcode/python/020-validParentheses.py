#!/usr/bin/python

# Given a string containing just the characters '(', ')', '{', '}', '[', and ']',
# determine if the input string is valid.

# The brackets must close in the correct order. "()" and "()[]{}" are all valid,
# but "(]" and "([)]" are not.

# Use stack to check validity, thus O(n).
def isValid(s):
    stack = list()
    parentheses = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c not in parentheses:
            stack.append(c)
        else:
            if not stack or stack.pop() != parentheses[c]:
                return False
    return False if stack else True

def main():
    print isValid('()[]{}')

main()
