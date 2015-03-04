#!/usr/bin/python

# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

def titleToNumber(s):
    num = 0
    for i in xrange(len(s)):
        num += (ord(s[i]) - 64) * pow(26, len(s) - i - 1)
    return num

def main():
    print titleToNumber('AA')

main()
