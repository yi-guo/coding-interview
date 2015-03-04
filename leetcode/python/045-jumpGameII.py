#!/usr/bin/python

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example, given array A = [2, 3, 1, 1, 4], the minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Greedy algorithm. O(n).
def jump(A):
    i = farthest = 0
    curr = steps = 0
    while i < len(A):
        if i > curr:
            curr = farthest
            steps = steps + 1
        farthest = max(farthest, A[i] + i)
        i = i + 1
    return steps

def main():
    print jump([4, 1, 1, 3, 1, 1, 1])

main()
