#!/usr/bin/python

# Given a sorted array, remove the duplicates in place such that each element appear only once
# and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example, given input array A = [1, 1, 2], your function should return length = 2, and A is now [1, 2].

# Two pointers i and j moving ahead with another variable prev keeping track of the previous element.
# Swap A[i] and A[j] whenever A[i] is not prev. Update prev and increment j.
# Hence, O(n).
def removeDuplicates(A):
    if not A:
        return 0
    i, j, prev = 1, 1, A[0]
    while A[i - 1] != A[-1]:
        while j < len(A) and A[j] == prev:
            j = j + 1
        j = min(j, len(A) - 1)
        prev = A[i] = A[j]
        i = i + 1
    return i

def main():
    A = [1, 1, 2, 2, 2, 3, 4, 5, 5]
    print "Before: %s, length = %d" % (str(A), len(A))
    length = removeDuplicates(A)
    print ' After: %s, length = %d' % (str(A), length)

main()
