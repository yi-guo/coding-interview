#!/usr/bin/python

# An integer whose base-twn representation consists only of zero and one is called "zero-one".

# Given an arbitrary integer n, which 0 < n < 100,000. find the smallest positive "zero-one" integer s which is the
# multiple of n. (It is mathematically guaranteed that every n has such an s.)


import sys
from collections import defaultdict


def zeroOneMultiple(n):
    i, remainders = 1, defaultdict(list)
    while True:
        remainder = i % n
        if remainder == 0:
            return i
        temp = dict(remainders)
        for subsetSum, subset in temp.iteritems():
            newSubsetSum = remainder + subsetSum
            if newSubsetSum == n:
                return sum(subset) + i
            if newSubsetSum % n not in remainders:
                remainders[newSubsetSum % n] = list(subset) + [i]
        if remainder not in remainders:
            remainders[remainder].append(i)
        i *= 10


def main():
    print zeroOneMultiple(int(sys.argv[1]))


main()
