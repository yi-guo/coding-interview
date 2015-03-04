#!/usr/bin/python

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab", return 1 since the palindrome partitioning ["aa", "b"] could be produced using 1 cut.

# Dynamic programming
# Define cuts[i] as the minimum number of cuts for string[i:]. Hence, initially we have cuts[i] = len(s) - i - 1.
# Define isPalindromic[i][j] is TRUE if string[i : j + 1] is palindromic.
# For any i and j, isPalindromic[i][j] is true if
#   1. s[i] == s[j] and isPalindromic[i + 1][j - 1] is true (s[i + 1 : j] is a palindrome).
#   2. s[i] == s[j] and j - i < 2. This includes the case when a palindromic string is of length 1 or 2.
# Maintain cuts from the end of s while maintaining isPalindromic. cuts[i] always takes the minimum of cuts[i] itself
# and cuts[j + 1] + 1, which means s[i : j + 1] is palindromic. 
def minCut(s):
    if not s or len(s) < 2:
        return 0
    cuts = [len(s) - i - 1 for i in range(len(s) + 1)]
    isPalindromic = [[False for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i < 2 or isPalindromic[i + 1][j - 1]):
                isPalindromic[i][j] = True
                cuts[i] = min(cuts[i], cuts[j + 1] + 1)
    return cuts[0]

def main():
    print minCut('aaba')

main()
