#!/usr/bin/python

# Follow up for "Remove Duplicates": What if duplicates are allowed at most twice?

# For example, given sorted array A = [1, 1, 1, 2, 2, 3], your function should return length = 5,
# and A is now [1, 1, 2, 2, 3].

# Same idea as in "Remove Duplicates" but with another variable keeping track of the number of each element.
# One pass, thus O(n)
def removeDuplicates(A):
    if not A:
        return 0
    elif len(A) < 3:
        return len(A)
    prev, count = None, 0
    i, j, length = 0, 0, len(A)
    while i < len(A):
        if A[i] == prev:
            count = count + 1
            if count > 2:
                length = length - 1
                i = i + 1
                continue
        else:
            count = 1
            prev = A[i]
        A[i], A[j] = A[j], A[i]
        j = j + 1
        i = i + 1
    return length

def main():
    A = [1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5]
    print "Before: %s, length = %d" % (str(A), len(A))
    length = removeDuplicates(A)
    print ' After: %s, length = %d' % (str(A), length)

main()
