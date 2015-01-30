#!/usr/bin/python

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.

# Note:
#   1. Elements in a quadruplet (a, b, c, d) must be in non-descending order, i.e., a <= b <= c <= d.
#   2. The solution set must not contain duplicate quadruplets.

# For example, given array S = {1, 0, -1, 0, -2, 2} and target = 0, a solution set is
# {(-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)}.

import collections


# For every possible pair, do twoSum, thus O(n^2) for finding all possible pairs plus O(n/2) for
# running twoSum amongst the pairs, which leads to O(n^2) overall.
def fourSum(num, target):
    if not num or len(num) < 4:
        return list()
    pairs, foursums = collections.defaultdict(list), set()
    for i in xrange(len(num)):
        for j in xrange(i + 1, len(num)):
            pairs[num[i] + num[j]].append((i, j))
    newNum = list()
    for key, value in pairs.iteritems():
        newNum.extend([key] * len(value))
    twosums = twoSum(sorted(newNum), target)
    for twosum in twosums:
        for p1 in pairs[twosum[0]]:
            for p2 in pairs[twosum[1]]:
                merged = set(p1 + p2)
                if len(merged) < 4:
                    continue
                foursums.add(tuple(sorted([num[i] for i in merged])))
    return [list(quadruplet) for quadruplet in foursums]


# Two pointers as always, thus O(n).
def twoSum(num, target):
    twosums = set()
    i, j = 0, len(num) - 1
    while i < j:
        if num[i] + num[j] < target:
            i += 1
        elif num[i] + num[j] > target:
            j -= 1
        else:
            twosums.add((num[i], num[j]))
            i += 1
            j -= 1
    return twosums


def main():
    print fourSum([1, 0, -1, 0, -2, 2], 0)

main()
