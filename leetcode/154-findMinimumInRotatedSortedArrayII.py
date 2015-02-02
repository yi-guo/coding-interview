#!/usr/bin/python

# Follow up for "Find Minimum in Rotated Sorted Array": What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

# Find the minimum element.

# The array may contain duplicates.

# Binary search a number which is just smaller than its previous one.
def findMin(num):
    i, j = 0, len(num) - 1
    while i < j:
        m = (i + j) / 2
        if m > 0 and num[m] < num[m - 1]:
            return num[m]
        if num[i] < num[m]:
            if num[m] <= num[j]:
                return num[i]
            i = m + 1
        elif num[i] > num[m]:
            j = m - 1
        else:
            if i == m:
                return min(num[i], num[j])
            i = i + 1
    return num[i]

def main():
    num = [1, 3, 3, 3]
    for i in xrange(len(num)):
        newNum = num[i:] + num[:i]
        print '%s => %d' % (newNum, findMin(newNum))

main()
