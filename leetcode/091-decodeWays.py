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
    if not s: return 0          # s is empty, thus 0
    if s[0] == '0': return 0    # s starts with 0, thus 0
    if len(s) == 1: return 1    # s is of length 1, thus 1 since it's already not 0
    # Build DP where the base case says if the last element in s is not 0, then there is only 1 way to decode.
    d = [1 for i in range(len(s) + 1)]
    d[-2] = 1 if s[-1] != '0' else 0
    # Maintain DP. Be careful with 0s.
    for i in range(len(d) - 3, -1, -1):
        # If s[i] is 0, then d[i] is d[i + 1] if s[i - 1] is either 1 or 2; otherwise, d[i] = 0
        if s[i] == '0':
            d[i] = d[i + 1] if d[i - 1] == '1' or d[i - 1] == '2' else 0
        # If not otherwise, d[i] = the number of ways to decode s[i + 1:] and the number of ways to decode s[i + 2:]
        # given s[i : i + 2] can be decoded.
        else:
            d[i] = d[i + 1] + int(int(s[i : i + 2]) < 27) * d[i + 2]
    return d[0]

def main():
    print numDecodings(sys.argv[1])

main()
