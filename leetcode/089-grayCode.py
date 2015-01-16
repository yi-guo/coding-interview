#!/usr/bin/python

# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
# A gray code sequence must begin with 0.

# For example, given n = 2, return [0, 1, 3, 2]. Its gray code sequence is:
#   00 - 0
#   01 - 1
#   11 - 3
#   10 - 2

# Note: For a given n, a gray code sequence is not uniquely defined.

# For example, [0, 2, 3, 1] is also a valid gray code sequence according to the above definition.

import sys

# Notice that
#   n = 2, [00, 01, 11, 10]
#   n = 3, [000, 001, 011, 010, 110, 111, 101, 100]
# The gray code of n - 1, plus the reversed gray code of n - 1 with 1 prefixed.
def grayCode(n):
    if n == 0: return [0]
    if n == 1: return [0, 1]
    prev = grayCode(n - 1)
    return prev + [i | 1 << (n - 1) for i in reversed(prev)]

def main():
    print grayCode(int(sys.argv[1]))

main()
