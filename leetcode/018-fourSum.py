#!/usr/bin/python

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.

# Note:
#   1. Elements in a quadruplet (a, b, c, d) must be in non-descending order, i.e., a <= b <= c <= d.
#   2. The solution set must not contain duplicate quadruplets.

# For example, given array S = {1, 0, -1, 0, -2, 2} and target = 0, a solution set is
# {(-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)}.

# For every possible pair, do twoSum, thus O(n^2) for finding all possible pairs plus O(n/2) for
# running twoSum amongst the pairs, which leads to O(n^2) overall.
def fourSum(num, target):
    if len(num) < 4:
        return list()
    elif len(num) == 4 and sum(num) == target:
        return [sorted(num)]
    num.sort()
    nums, foursum = dict(), list()
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            key = num[i] + num[j]
            if key in nums:
                nums[key].append([num[i], num[j]])
            else:
                nums[key] = [[num[i], num[j]]]
    twosum_num = list()
    for key, value in nums.iteritems():
        twosum_num.extend([key for i in range(len(value))])
    twosum = twoSum(sorted(twosum_num), target)
    for pair in twosum:
        for p1 in nums[pair[0]]:
            for p2 in nums[pair[1]]:
                lst = list(p1)
                lst.extend(p2)
                lst.sort()
                if lst not in foursum and not conflict(num, lst):
                    foursum.append(lst)
    return foursum

# Two pointers as always, thus O(n).
def twoSum(num, target):
    twosum = list()
    i, j = 0, len(num) - 1
    while i < j:
        sum = num[i] + num[j]
        if sum < target:
            i = i + 1
        elif sum > target:
            j = j - 1
        else:
            twosum.append((num[i], num[j]))
            i = i + 1
            j = j - 1
    return twosum

# Check if the quadruplet conflicts the given array by having a number more times than it is given.
def conflict(num, lst):
    for n in lst:
        if lst.count(n) > num.count(n):
            return True
    return False

def main():
    print fourSum([1, 0, -1, 0, -2, 2], 0)

main()
