#!/usr/bin/python

# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Two pointers i and j move ahead. Whenever A[i] hits elem, decrement length;
# Otherwise, swap A[i] and A[j] (if they are different) and increment j.
# Clearly, this can be done in O(n) linear time.
def removeElement(A, elem):
    j, length = 0, len(A)
    for i in range(length):
        if A[i] == elem:
            length = length - 1
        else:
            if i != j:
                A[i], A[j] = A[j], A[i]
            j = j + 1
    return length

def main():
    A = [1, 5, 7, 3, 2, 4, 7, 2]
    print "Before: %s, length = %d" % (str(A), len(A))
    length = removeElement(A, 7)
    print ' After: %s, length = %d' % (str(A), length)

main()
