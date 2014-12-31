#!/usr/bin/python

# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

def lengthOfLongestSubstring(s):
    longest = 0
    visited = dict()
    for i, c in enumerate(s):
        if c in visited:
            length = i - visited[c]
            if longest < length:
                longest = length
                visited.clear()
            print i, c, length, longest
            print visited
        else:
            longest = longest + 1
        visited[c] = i
    return longest

def main():
    s = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
    print lengthOfLongestSubstring(s)

main()
