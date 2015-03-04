# -*- coding: utf-8 -*-

#!/usr/bin/python

# A peak element is an element that is greater than its neighbors.

# Given an input array where num[i] != num[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that num[-1] = num[n] = -∞.

# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

# Note: Your solution should be in logarithmic complexity.

def findPeakElement(num):
    i, j = 0, len(num) - 1
    while i < j:
        m = (i + j) / 2
        if m == 0 or num[m - 1] < num[m]:
            if m == len(num) - 1 or num[m] > num[m + 1]:
                return m
            i = m + 1
        else:
            j = m - 1
    return j

def main():
    num = [1, 2, 3, 1]
    print findPeakElement(num)

main()
