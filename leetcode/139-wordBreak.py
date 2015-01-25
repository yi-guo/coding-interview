#!/usr/bin/python

# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of
# one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

# Dynamic programming. Maintain an array breakable such that breakable[i] is true if s[0 : i + 1] is breakable.
def wordBreak(s, dict):
    breakable = [False for c in s]
    for i in range(1, len(s) + 1):
        if s[0 : i] in dict:
            breakable[i - 1] = True
            continue
        for j in range(0, i):
            if breakable[j] and s[j + 1 : i] in dict:
                breakable[i - 1] = True
                break
    return breakable[-1]

def main():
    s = 'leetcode'
    dict = ['leet', 'code']
    print wordBreak(s, dict)

main()
