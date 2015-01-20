#!/usr/bin/python

# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example, given:
#   s1 = "aabcc",
#   s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

# Dynamic programming with 2D boolean matrix match, where match[i][j] represents
# if s1[:i] and s2[:j] matches s3[:i+j]
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    m, n = len(s1), len(s2)
    match = [[True for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
    for i in range(1, n + 1):
        match[0][i] = match[0][i - 1] and s2[i - 1] == s3[i - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                          (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    return match[m][n]

def main():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print isInterleave(s1, s2, s3)

main()
