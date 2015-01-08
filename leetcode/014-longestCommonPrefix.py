#!/usr/bin/python

# Write a function to find the longest common prefix string amongst
# an array of strings.

# Divide and conquer. T(n) = 2T(n/2) + O(m), thus O(mn).
def longestCommonPrefix(strs):
    if len(strs) == 0:
        return str()
    elif len(strs) == 1:
        return strs[0]
    elif len(strs) == 2:
        i, prefix = 0, list()
        s1, s2 = strs[0], strs[1]
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                break
            prefix.append(s1[i])
            i = i + 1
        return ''.join(prefix)
    else:
        q = len(strs) / 2
        return longestCommonPrefix([longestCommonPrefix(strs[:q]), longestCommonPrefix(strs[q:])])

def main():
    strs = ['a', 'aabba', 'abaabba', 'abba', 'abaaa']
    print longestCommonPrefix(strs)

main()
