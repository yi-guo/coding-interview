#!/usr/bin/python

# Given an unsorted integer array, find the first missing positive integer.

# For example, given [1, 2, 0] return 3, and [3, 4, -1, 1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

# Move all positive integers in A such that A[i] == i + 1.
def firstMissingPositive(A):
    if not A:
        return 1
    i = 0
    while i < len(A):
        j = A[i] - 1
        if j >= 0 and i != j and j < len(A) and A[i] != A[j]:
            A[i], A[j] = A[j], A[i]
        else:
            i = i + 1
    # Traverse the "sorted" array and return the first index such that A[i] != i + 1.
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    # Otherwise, return len(A) + 1
    return len(A) + 1

def main():
    print firstMissingPositive([3, 4, -1, 1])

main()
