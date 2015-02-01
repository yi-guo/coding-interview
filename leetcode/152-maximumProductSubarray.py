#!/usr/bin/python

# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2, 3, -2, 4], the contiguous subarray [2, 3] has the largest product = 6.

# Need to keep track of the maximum and minimum, in case of two negative numbers. One pass, thus O(n).
def maxProduct(A):
    if not A:
        return 0
    res = minimum = maximum = A[0]
    for i in xrange(1, len(A)):
        temp = maximum
        maximum = max(A[i], A[i] * temp, A[i] * minimum)
        minimum = min(A[i], A[i] * temp, A[i] * minimum)
        res = max(res, maximum)
    return res

def main():
    print maxProduct([2, 3, -2, 4])

main()
