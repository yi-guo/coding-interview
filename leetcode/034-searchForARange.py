#!/usr/bin/python

# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example, given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].

# A revised binary search, thus O(log(n)).
def searchRange(A, target, i=None, j=None):
    # If no i and j passed, then search inside A.
    if i is None and j is None:
        i, j = 0, len(A) - 1
    # In any circumstances, if the following condition holds, then jump to conclusion.
    if i > j or A[i] > target or A[j] < target:
        return [-1, -1]
    elif A[i] == target and A[j] == target:
        return [i, j]
    # Start binary search
    while i <= j:
        mid = (i + j) / 2
        # Search within the right partition
        if A[mid] < target:
            i = mid + 1
        # Search within the left partition
        elif A[mid] > target:
            j = mid - 1
        # Target found; search left AND right recursively for where it starts and ends.
        else:
            l = searchRange(A, target, i, mid)
            r = searchRange(A, target, mid + 1, j)
            # Take whichever is the range. If both are, take the union instead.
            if l == [-1, -1]:
                return r
            elif r == [-1, -1]:
                return l
            else:
                return [l[0], r[1]]
    # Can't find it anywhere inside A!
    return [-1, -1]

def main():
    print searchRange([5, 5, 6, 6, 6, 7, 8, 8, 10, 10, 10, 11], 6)

main()
