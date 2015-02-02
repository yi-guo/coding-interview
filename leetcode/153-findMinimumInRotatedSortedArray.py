#!/usr/bin/python

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Binary search a number which is just smaller than its previous one.
def findMin(num):
    i, j = 0, len(num) - 1
    while i < j:
        m = (i + j) / 2
        if m > 0 and num[m] < num[m - 1]:
            return num[m]
        if num[i] < num[m]:
            if num[m] < num[j]:
                return num[i]
            i = m + 1
        elif num[i] > num[m]:
            j = m - 1
        else:
            return min(num[i], num[j])
    return num[i]

def main():
    num = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in xrange(len(num)):
        newNum = num[i:] + num[:i]
        print '%s => %d' % (newNum, findMin(newNum))

main()
