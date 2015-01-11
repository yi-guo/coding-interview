#!/usr/bin/python

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

# You are given a target value to search. If found in the array, return its index; otherwise, return -1.

# You may assume no duplicate exists in the array.

# A revised binary search, thus O(log(n)).
def search(A, target):
    if not A:
        return -1
    elif len(A) == 1:
        if A[0] == target:
            return 0
        return -1
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] == target:
            return i
        elif A[j] == target:
            return j
        mid = (i + j) / 2
        if A[mid] == target:
            return mid
        if A[i] < A[mid]:
            if A[i] < target and target < A[mid]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if A[mid] < target and target < A[j]:
                i = mid + 1
            else:
                j = mid - 1
    return -1

def main():
    A = [4, 5, 6, 7, 0, 0, 0, 1, 2]
    print search(A, 2)

main()
