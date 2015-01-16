#!/usr/bin/python

# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.

# Starting from the end of A, compare and fill A. Thus O(n).
def merge(A, m, B, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if A[i] < B[j]:
            A[k] = B[j]
            j = j - 1
        else:
            A[k] = A[i]
            i = i - 1
        k = k - 1
    # In case anything left in B not done yet.
    while j >= 0:
        A[k] = B[j]
        j = j - 1
        k = k - 1

def main():
    A = [14, 15, 16, 0, 0, 0, 0, 0, 0, 0]
    B = [3, 5, 6, 8, 9, 11, 13]
    merge(A, 3, B, 7)
    print A

main()
