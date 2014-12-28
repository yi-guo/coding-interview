#!/usr/bin/python

# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

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

# Hash table mapping numbers to their indices; O(n)
def twoSum2(num, target):
    nums = dict()
    for i, n in enumerate(num):
        if nums.has_key(n):
            nums[n].append(i + 1)
        else:
            nums[n] = [i + 1]
    for key, value in nums.iteritems():
        if key == target - key and len(value) > 1:
            return (min(value), max(value))
        elif key != target - key and nums.has_key(target - key):
            i, j = value[0], nums[target - key][0]
            return (min(i, j), max(i, j))
    return None

def main():
    num, target = [2, 7, 2, 11, 15], 4
    print twoSum1(num, target)
    print twoSum2(num, target)


main()