#!/usr/bin/python

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab", return [["aa", "b"], ["a", "a", "b"]].

def partition(s):
    
    def nextPalindrome(s, index, palindrome):
        if index >= len(s):
            res.append(list(palindrome))
        else:
            for i in range(index, len(s)):
                if isPalindromic(s, index, i):
                    palindrome.append(s[index : i + 1])
                    nextPalindrome(s, i + 1, palindrome)
                    palindrome.pop()

    res = list()
    nextPalindrome(s, 0, list())
    return res

# Determine if string s[i : j + 1] is palindromic.
def isPalindromic(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def main():
    print partition('aab')

main()
