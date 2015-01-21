#!/usr/bin/python

# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
# The overall run time complexity should be O(log(m+n))

# Convert the problem into finding the kth smallest element in the merged array of size m + n.
def findMedianSortedArrays(A, B):
    size = len(A) + len(B)
    if size % 2 != 0:
        return findKthElement(A, len(A), B, len(B), size / 2 + 1)
    else:
        return (findKthElement(A, len(A), B, len(B), size / 2) + findKthElement(A, len(A), B, len(B), size / 2 + 1)) / 2.0

def findKthElement(A, m, B, n, k):
    if m > n:
        return findKthElement(B, n, A, m, k)
    if m == 0:
        return B[k - 1]
    if k == 1:
        return min(A[0], B[0])
    i = min(k / 2, m)
    j = k - i
    if A[i - 1] < B[j - 1]:
        return findKthElement(A[i:], m - i, B, n, k - i)
    elif A[i - 1] > B[j - 1]:
        return findKthElement(A, m, B[j:], n - j, k - j)
    else:
        return A[i - 1]

def main():
    A = [0, 2, 8, 24, 35]
    B = [1, 3, 4, 5, 6, 8, 9, 10]
    print findMedianSortedArrays(A, B)

main()
