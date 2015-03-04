#!/usr/bin/python

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4], the contiguous subarray [4, -1, 2, 1]
# has the largest sum of 6.

# A divide-and-conquer approach. The maximum shall only occur
#   1. in the left subarray;
#   2. in the right subarray;
#   3. in the array crossing the midpoint;
# T(n) = 2T(n/2) + O(n), thus O(nlog(n)).
def maxSubArray1(A, i=None, j=None):
    if i is None and j is None:
        i, j = 0, len(A) - 1
    if j - i == 0:
        return A[i]
    elif j - i == 1:
        return max(A[i], A[j], A[i] + A[j])
    else:
        mid = (i + j) / 2
        leftSub = maxSubArray1(A, i, mid)
        rightSub = maxSubArray1(A, mid + 1, j)
        leftSum = rightSum = float('-inf')
        sum = 0
        for k in range(mid, i - 1, -1):
            sum = sum + A[k]
            leftSum = max(sum, leftSum)
        sum = 0
        for k in range(mid + 1, j + 1):
            sum = sum + A[k]
            rightSum = max(sum, rightSum)
        return max(leftSub, rightSub, leftSum + rightSum)

# Keep track of the maximum so far while traversing the array, thus O(n).
#   currMax: maximum sum ending at index i
#   maxSoFar: maximum sum achieved so far
def maxSubArray2(A):
    currMax = maxSoFar = A[0]
    for n in A[1:]:
        currMax = max(n, currMax + n)
        maxSoFar = max(currMax, maxSoFar)
    return maxSoFar

def main():
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print 'Divide & Conquer: %d' % maxSubArray1(A)
    print 'Kadane Algorithm: %d' % maxSubArray2(A)

main()
