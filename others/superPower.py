#!/usr/bin/python

# Source: Zappos.com Online Assessment

# Given a positive integer z, where 1 <= z <= 10^9, check if z can be written as p ^ q, where p and q are positive
# integers greater than 1. If z can be written as p ^ q, return 1. Otherwise, return 0.

import sys

# Binary search.
def superPower(z):
    if z < 4:
        return 0
    for q in xrange(2, 30):
        i, j = 2, z / q
        while i <= j:
            p = (i + j) / 2
            power = pow(p, q)
            if power < z:
                i = p + 1
            elif power > z:
                j = p - 1
            else:
                return 1
    return 0

def main():
    print superPower(int(sys.argv[1]))

main()
