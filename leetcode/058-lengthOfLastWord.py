#!/usr/bin/python

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example, given s = "Hello World", return 5.

import sys

# Strip the leading and trailing whitespaces and search for the first whitespace in the string from right to left.
def lengthOfLastWord(s):
    s = s.strip()
    if not s:
        return 0
    i = len(s) - 1
    while i >= 0:
        if s[i].isspace():
            return len(s) - i - 1
        i = i - 1
    return len(s)

def main():
    print lengthOfLastWord(sys.argv[1])

main()
