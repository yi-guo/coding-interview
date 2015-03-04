#!/usr/bin/python

# A recursive solution, which is VERY time consuming.
def isScramble1(s1, s2):
    if len(s1) != len(s2): return False
    if s1 == s2: return True
    if sorted(s1) != sorted(s2): return False
    for i in range(1, len(s1)):
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]): return True
        if isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i]): return True
    return False

print isScramble("great", 'rgeat')