#!/usr/bin/python

# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

# Try to solve it in linear time/space.

# Return 0 if the array contains less than 2 elements.

# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

# Radix sort the array and find the maximum gap.
def maximumGap(num):
    if not num or len(num) < 2:
        return 0
    gap, num = 0, radixSort(num)
    for i in xrange(1, len(num)):
        gap = max(gap, num[i] - num[i - 1])
    return gap

def radixSort(num):
    exp, maximum = 1, max(num)
    radix = [[] for i in xrange(10)]
    while maximum / exp > 0:
        for n in num:
            radix[n / exp % 10].append(n)
        num = radix[0]
        for i in xrange(1, 10):
            num.extend(radix[i])
        exp = exp * 10
        radix = [[] for i in xrange(10)]
    return num

def main():
    print maximumGap([170, 45, 75, 90, 802, 24, 2, 66, 1611])

main()
