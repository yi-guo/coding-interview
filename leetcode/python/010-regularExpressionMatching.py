#!/usr/bin/python

# Implement regular expression matching with support for '.' and '*'

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true

# Recursion.
def isMatch1(s, p):
    if not p: return not s
    if len(p) == 1 or p[1] != '*':
        if len(s) < 1 or (p[0] != '.' and s[0] != p[0]):
            return False
        return isMatch1(s[1:], p[1:])
    else:
        i = -1
        while i < len(s) and (i < 0 or p[0] == '.' or p[0] == s[i]):
            if isMatch1(s[i + 1:], p[2:]):
                return True
            i = i + 1
        return False

# Dynamic programming.
def isMatch2(s, p):
    d = [[False for _ in xrange(len(s) + 1)] for _ in xrange(len(p) + 1)]
    d[0][0] = True
    for i in xrange(1, len(p)):
        d[i + 1][0] = d[i - 1][0] and p[i] == '*'
    for i in xrange(len(p)):
        for j in xrange(len(s)):
            if p[i] == '*':
                d[i + 1][j + 1] = d[i - 1][j + 1] or d[i][j + 1]
                if p[i - 1] == s[j] or p[i - 1] == '.':
                    d[i + 1][j + 1] |= d[i + 1][j]
            else:
                d[i + 1][j + 1] = d[i][j] and (p[i] == '.' or p[i] == s[j])
    return d[-1][-1]

def main():
    print isMatch2('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')

main()
