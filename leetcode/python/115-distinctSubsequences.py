#!/usr/bin/python

# Given a string S and a string T, count the number of distinct subsequences of T in S.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of
#the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Here is an example: S = "rabbbit", T = "rabbit", return 3.

# Dynamic programming. Let d[i][j] represents the number of distinct subsequences of T[:i] in S[:j].
# Hence, d[0][j] = 1 and d[i][j] = 0 for all i > j
# Maintain the matrix row by row starting at i == j, where d[i][j] = d[i][j - 1] if T[i - 1] != S[j - 1].
# If, on the other hand, T[i][j - 1] = S[i][j - 1], d[i][j] = d[i][j - 1] + d[i - 1][j - 1].
def numDistinct(S, T):
    if len(S) < len(T):
        return 0
    elif len(S) > len(T):
        m, n = len(T), len(S)
        d = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(n + 1):
            d[0][i] = 1
        for i in range(1, m + 1):
            for j in range(i, n + 1):
                d[i][j] = d[i][j - 1] if T[i - 1] != S[j - 1] else d[i][j - 1] + d[i - 1][j - 1]
        return d[m][n]
    else:
        return int(S == T)

def main():
    print numDistinct('ccc', 'c')

main()
