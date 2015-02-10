#!/usr/bin/python

# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false

# Two pointers keeping track of the indices in s and p if hits a '*' in p.
def isMatch(s, p):
    i = j = 0
    currS = currP = -1
    while i < len(s):
        if j < len(p) and (s[i] == p[j] or p[j] == '?'):
            i = i + 1
            j = j + 1
        elif j < len(p) and p[j] == '*':
            currS = i
            currP = j
            j = j + 1
        elif currS != -1:
            currS = currS + 1
            i = currS
            j = currP + 1
        else:
            return False
    while j < len(p) and p[j] == '*':
        j = j + 1
    return True if i == len(s) and j == len(p) else False

def main():
    print isMatch("aa", "*")

main()
