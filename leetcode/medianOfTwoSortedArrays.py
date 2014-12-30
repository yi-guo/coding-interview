#!/usr/bin/python

# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n))

def medianOfTwoSortedArrays(A, B):
    m, n = len(A), len(B)
    a, b = median(A), median(B)
    if a < b:
        return medianOfTwoSortedArrays(A[(m-1)/2:], B[:(n-1)/2+1])
    elif a > b:
        return medianOfTwoSortedArrays(A[:(m-1)/2+1], B[(n-1)/2:])
    else:
        return a

def median(A):
    n = len(A)
    if n % 2 == 0:
        return A[n/2 - 1]
    else:
        return A[n/2]

def main():
    A = [1,2,3,4,5,7]
    B = [2,3,4,5,6,7,8,9,10]
    print median(A)
    print median(B)
    print median([1])
    print medianOfTwoSortedArrays(A, B)

main()