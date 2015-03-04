#!/usr/bin/python

# Given two binary strings, return their sum (also a binary string).

# For example, a = "11", b = "1", return "100".

import sys

# Do addition with the carry bit starting at the least significant bit till both are empty. O(n).
def addBinary(a, b):
    diff = len(a) - len(b)
    if diff < 0:
        a = '0' * abs(diff) + a
    else:
        b = '0' * abs(diff) + b
    sum, carry = list(), 0
    for i in xrange(len(a) - 1, -1, -1):
        curr = int(a[i]) + int(b[i]) + carry
        curr, carry = curr % 2, curr / 2
        sum.append(str(curr))
    return ('1' if carry else '') + ''.join(sum[::-1])

def main():
    print addBinary(sys.argv[1], sys.argv[2])

main()
