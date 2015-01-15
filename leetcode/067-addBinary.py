#!/usr/bin/python

# Given two binary strings, return their sum (also a binary string).

# For example, a = "11", b = "1", return "100".

import sys

# Do addition with the carry bit starting at the least significant bit till both are empty. O(n).
def addBinary(a, b):
    if not a:
        return b
    elif not b:
        return a
    a, b = list(a), list(b)
    carry, result = 0, list()
    # Pop the last element in a and b and do addition until one of them is empty.
    while a and b:
        add = int(a.pop()) + int(b.pop()) + carry
        if add < 2:
            carry = 0
            result.append(str(add))
        else:
            carry = 1
            result.append(str(add % 2))
    # If b is empty first, do addition with the carry bit till carry clears out.
    while a:
        add = int(a.pop()) + carry
        if add < 2:
            result.append(str(add))
            return ''.join(a + result[::-1])
        result.append(str(add % 2))
    # If a is empty first, do addition with the carry bit till carry clears out.
    while b:
        add = int(b.pop()) + carry
        if add < 2:
            result.append(str(add))
            return ''.join(b + result[::-1])
        result.append(str(add % 2))
    # If carry bit is yet cleared out, add 1 more bit to the front.
    if carry:
        result.append('1')
    return ''.join(result[::-1])

def main():
    print addBinary(sys.argv[1], sys.argv[2])

main()
