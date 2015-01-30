#!/usr/bin/python

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets
# in the array which gives the sum of zero.

# Note:
#   1. Elements in a triplet (a, b, c) must be in non-descending order, i.e., a <= b <= c.
#   2. The solution set must not contain duplicate triplets.

# For example, given array S = {-1, 0, 1, 2, -1, -4}, a solution set is {(-1, 0, 1), (-1, -1, 2)}

# For every number that has not been visited, do twoSum, thus O(n) * O(n) = O(n^2).
def threeSum(num):
    num.sort()
    threesum = set()
    for i, n in enumerate(num):
        twosum = twoSum(num, i, 0 - n)
        if twosum:
            for res in twosum:
                threesum.add(tuple(sorted((res[0], res[1], n))))
    return [list(triplet) for triplet in threesum]


def twoSum(num, curr, target):
    res = list()
    i, j = 0, len(num) - 1
    while i < j:
        if i == curr:
            i = i + 1
            continue
        elif j == curr:
            j = j - 1
            continue
        twosum = num[i] + num[j]
        if twosum < target:
            i = i + 1
        elif twosum > target:
            j = j - 1
        else:
            res.append([num[i], num[j]])
            i = i + 1
            j = j - 1
    return res

def main():
    print threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])

main()
