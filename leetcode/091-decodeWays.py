#!/usr/bin/python

# A message containing letters from A - Z is being encoded to numbers using the following mapping:

#   'A' -> 1
#   'B' -> 2
#   ...
#   'Z' -> 26

# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example, given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

import sys

# Dynamic programming where i is the number of ways decoding s[i:]. One pass, thus O(n).
def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    decodings = [1, 1]
    for i in xrange(1, len(s)):
        decodings.append(int(s[i] != '0') * decodings[i] + int(s[i - 1] != '0' and 0 < int(s[i - 1 : i + 1]) < 27) * decodings[i - 1])
    return decodings[len(s)]

def main():
    print numDecodings(sys.argv[1])

main()
