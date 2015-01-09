#!/usr/bin/python

# Given a string containing just the characters '(', ')', '{', '}', '[', and ']',
# determine if the input string is valid.

# The brackets must close in the correct order. "()" and "()[]{}" are all valid,
# but "(]" and "([)]" are not.

# Use stack to check validity, thus O(n).
def isValid(s):
    if not s:
        return True
    elif len(s) % 2 != 0:
        return False
    pairs = {'(' : ')', '[' : ']', '{' : '}'}
    i, stack = 0, list()
    while i < len(s):
        if s[i] in pairs:
            stack.append(s[i])
        else:
            # Handle cases like ')' and '([)'
            if not stack or s[i] != pairs[stack.pop()]:
                return False
        i = i + 1
    # Handle cases like '(('
    if stack:
        return False
    else:
        return True

def main():
    print isValid('()[]{}')

main()
