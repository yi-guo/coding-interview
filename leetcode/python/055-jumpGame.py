#!/usr/bin/python

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
#   A = [2, 3, 1, 1, 4], return true.
#   A = [3, 2, 1, 0, 4], return false.

# Greedy algorithm. O(n).
def canJump(A):
    if len(A) < 2:
        return True
    elif len(A) == 2:
        return A[0] != 0
    i = farthest = 0
    while i < len(A):
        farthest = max(farthest, A[i] + i)
        if farthest >= len(A) - 1:
            return True
        if A[i] == 0 and farthest == i:
            return False
        i = i + 1
    return True

def main():
    A = [3, 2, 1, 0, 4]
    print canJump(A)

main()
