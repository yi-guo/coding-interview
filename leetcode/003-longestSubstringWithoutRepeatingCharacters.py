#!/usr/bin/python

# Given a string, find the length of the longest substring without repeating characters. For example, the longest
# substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest
# substring is "b", with the length of 1.

# Traverse the given string and keep tracking of the visited characters; O(n)
def lengthOfLongestSubstring(s):
    visited = dict()
    currStart = 0
    currLength = longest = 0
    for i, c in enumerate(s):
        if c in visited and visited[c] >= currStart:
            if currLength > longest:
                longest = currLength
            currStart = visited[c] + 1
            currLength = i - visited[c]
        else:
            currLength = currLength + 1
        visited[c] = i
    if currLength > longest:
        longest = currLength
    return longest

def main():
    s = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
    print lengthOfLongestSubstring(s)

main()
