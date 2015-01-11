#!/usr/bin/python

# Given a sorted array and a target value, return the index if the target is found. If not, return the index
# where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are a few examples.
#   [1, 3, 5, 6], 5 -> 2
#   [1, 3, 5, 6], 2 -> 1
#   [1, 3, 5, 6], 7 -> 4
#   [1, 3, 5, 6], 0 -> 0

# A recursive binary search solution, thus O(n).
def searchInsert(A, target, i=None, j=None):
    if not A:
        return 0
    if i is None and j is None:
        i, j = 0, len(A) - 1
    if A[i] > target:
        return i
    elif A[j] < target:
        return j + 1
    mid = (i + j) / 2
    if A[mid] < target:
        return searchInsert(A, target, mid + 1, j)
    elif A[mid] > target:
        return searchInsert(A, target, i, mid - 1)
    else:
        return mid

def main():
    print searchInsert([1, 3, 5, 6], 5)

main()
