#!/usr/bin/python

# Follow up for "Search in Rotated Sorted Array".

# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Write a function to determine if a given target is in the array.

# Modified solution from "Search in Rotated Sorted Array", O(log(n)) in average and O(n) in the worst case.
def search(A, target):
    # Direct compare if A is of length 0 or 1.
    if not A:
        return False
    elif len(A) < 2:
        return A[0] == target
    i, j = 0, len(A) - 1
    while i <= j:
        m = (i + j) / 2
        if A[m] == target:
            return True
        # Left partition is sorted.
        if A[i] < A[m]:
            if A[i] <= target < A[m]:
                j = m -1
            else:
                i = m + 1
        # Right partition is sorted.
        elif A[i] > A[m]:
            if A[m] < target <= A[j]:
                i = m + 1
            else:
                j = m - 1
        # Cannot decide which side to go as in [1, 3, 1, 1, 1]
        else:
            i = i + 1
    return False

def main():
    A = [2, 2, 2, 0, 0, 1]
    print search(A, 0)

main()
