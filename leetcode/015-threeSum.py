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
    i, threesum = 0, list()
    while i < len(num):
        if i != 0 and num[i] == num[i - 1]:
            i = i + 1
            continue
        twosum = twoSum(num, i, 0 - num[i])
        if twosum:
            threesum.extend(twosum)
        i = i + 1
    return threesum

# Two pointers move toward each other, thus O(n)
def twoSum(num, current, target):
    i, j = 0, len(num) - 1
    twosum, exists = list(), set()
    while i < j:
        if i == current:
            i = i + 1
            continue
        elif j == current:
            j = j - 1
            continue
        sum = num[i] + num[j]
        if sum < target:
            i = i + 1
        elif sum > target:
            j = j - 1
        else:
            # First constraint removes duplicates like (-4, 2, 2) when current is 2
            # Second constraint removes duplicates like (-4, 2, 2) when current is -4
            if num[current] <= num[i] and num[i] not in exists:
                exists.add(num[i])
                twosum.append([num[current], num[i], num[j]])              
            i = i + 1
            j = j - 1
    return twosum

def main():
    print threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])

main()
