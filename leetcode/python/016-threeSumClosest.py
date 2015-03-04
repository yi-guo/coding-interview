#!/usr/bin/python

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. # Return the sum of the three integers. You may assume that each input would have exactly one solution.

# For example, given array S = {-1, 2, 1, -4} and target = 1, the sum that is closest to the target is 2
# since -1 + 2 + 1 = 2.

# For every number that has not been visited, do twoSumClosest, thus O(n) * O(n) = O(n^2).
def threeSumClosest(num, target):
    if len(num) == 3:
        return sum(num)
    num.sort()
    closest, variance = 0, float('inf')
    i = 0
    while i < len(num):
        if i != 0 and num[i] == num[i - 1]:
            i = i + 1
            continue
        threesum = num[i] + twoSumClosest(num, i, target - num[i])
        if threesum == target:
            return threesum
        if abs(target - threesum) < variance:
            closest = threesum
            variance = abs(target - threesum)
        i = i + 1
    return closest

# Two pointers move toward each other, thus O(n).
def twoSumClosest(num, current, target):
    i, j = 0, len(num) - 1
    closest, variance = 0, float('inf')
    while i < j:
        if i == current:
            i = i + 1
            continue
        elif j == current:
            j = j - 1
            continue
        twosum = num[i] + num[j]
        if abs(target - twosum) < variance:
            closest = twosum
            variance = abs(target - closest)
        if twosum < target:
            i = i + 1
        elif twosum > target:
            j = j - 1
        else:
            break
    return closest

def main():
    print threeSumClosest([1, 1, -1, -1, 3], -1)
    print threeSumClosest([0, 1, 2], 0)

main()
