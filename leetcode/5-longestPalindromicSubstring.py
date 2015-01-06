#!/usr/bin/python

# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
# and there exists one unique longest palindromic subtring.

# For each character, find the longest palindrom centered at itself. O(n^2)
def longestPalindromicSubstring(s):
    if len(s) < 2:
        return s
    longest = str()
    for i in range(len(s)):
        p1, p2 = longestPalindrom(s, i - 1, i + 1), str()
        if i < len(s) - 1 and s[i] == s[i + 1]:
            p2 = longestPalindrom(s, i - 1, i + 2)
        longest = max(p1, p2, longest, key = len)
    return longest

# Given a character, keep expanding until its left and right are different.
def longestPalindrom(s, l, r):
    while l >= 0 and r < len(s):
        if s[l] != s[r]:
            break
        l = l - 1
        r = r + 1
    return s[l + 1 : r]


def main():
   s = "12343343321"
   print longestPalindromicSubstring(s)

main()
