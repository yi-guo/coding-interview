#!/usr/bin/python

# Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

# You may assume that the array is non-empty and the majority element always exist in the array.

from collections import defaultdict

# Hash table. O(n) in both time and space.
def majorityElement1(num):
    count, majority = defaultdict(int), len(num) / 2
    for n in num:
        if count[n] == majority:
            return n
        count[n] += 1

# Moore's Voting Algorithm. O(n) in time and O(1) in space.
def majorityElement2(num):
    majority, count = num[0], 1
    for i in xrange(1, len(num)):
        if num[i] == majority:
            count += 1
            continue
        count -= 1
        if count == 0:
            count = 1
            majority = num[i]
    return majority

def main():
    print majorityElement2([1, 2, 2])

main()
