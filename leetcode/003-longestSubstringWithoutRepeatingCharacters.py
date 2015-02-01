#!/usr/bin/python

# Given a string, find the length of the longest substring without repeating characters. For example, the longest
# substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest
# substring is "b", with the length of 1.

# Traverse the given string and keep tracking of the visited characters; O(n)
def lengthOfLongestSubstring(s):
    length = longest = 0
    start, visited = 0, dict()
    for i, c in enumerate(s):
        if c in visited and visited[c] >= start:
            longest = max(longest, length)
            start = visited[c] + 1
            length = i - visited[c]
        else:
            length += 1
        visited[c] = i
    return max(longest, length)

def main():
    s = 'wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'
    print lengthOfLongestSubstring(s)

main()
