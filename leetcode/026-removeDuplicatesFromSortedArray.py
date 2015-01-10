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
    elif len(A) < 2:
        return len(A)
    i = j = 0
    prev, length = None, len(A)
    while i < len(A):
        if A[i] == prev:
            length = length - 1
        else:
            prev = A[i]
            A[i], A[j] = A[j], A[i]
            j = j + 1
        i = i + 1
    return length

def main():
    A = [1, 1, 2, 2, 2, 3, 4, 5, 5]
    print "Before: %s, length = %d" % (str(A), len(A))
    length = removeDuplicates(A)
    print ' After: %s, length = %d' % (str(A), length)

main()
