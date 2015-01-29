#!/usr/bin/python

# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1
# must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: num = [2, 7, 11, 15], target = 9
# Output: (1, 2)

# Sort the array and conduct binary search; O(nlog(n))
def twoSum1(num, target):
    nums = sorted(num)
    i, j = 0, len(num) - 1
    while i < len(num) and j >= 0:
        sum = nums[i] + nums[j]
        if sum < target:
            i = i + 1
        elif sum > target:
            j = j - 1
        else:
            x = -1
            for k, n in enumerate(num):
                if x == -1 and n == nums[i]:
                    x = k
                if x != k and n == nums[j]:
                    return (min(x, k) + 1, max(x, k) + 1)
    return None

# Hash table look-up. One pass, O(n).
def twoSum2(num, target):
    nums = dict()
    for i, n in enumerate(num):
        if target - n in nums and i != nums[target - n]:
            return nums[target - n] + 1, i + 1
        nums[n] = i

def main():
    num, target = [2, 7, 2, 11, 15], 4
    print twoSum1(num, target)
    print twoSum2(num, target)

main()
