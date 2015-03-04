#!/usr/bin/python

# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

# For example, given [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], return 6.

# Traverse the array twice, thus O(n).
def trap(A):
    # Impossible to trap any water
    if not A or len(A) < 3:
        return 0
    water = 0
    # For every bar, find the highest bar on its left.
    maxLeft = list(A)
    for i in range(1, len(A)):
        maxLeft[i] = max(maxLeft[i], maxLeft[i - 1])
    # For every bar, find the highest bar on its right.
    maxRight = A[len(A) - 1]
    for i in range(len(A) - 2, 0, -1):
        maxRight = max(maxRight, A[i])
        # The maximum amount of trapped water at the ith bar is min(maxLeft, maxRight) - A[i]
        water += min(maxLeft[i], maxRight) - A[i]
    return water

def main():
    print trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print trap([8, 6, 2, 4, 6])

main()
