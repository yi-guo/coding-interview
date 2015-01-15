#!/usr/bin/python

# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent
# with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Follow up: A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
# then 1's and followed by 2's.

# Could you come up with an one-pass algorithm using only constant space?

# Counting sort, two pass, thus O(2n).
def sortColors1(A):
    k, count = 0, [0, 0, 0]
    for n in A:
        count[n] = count[n] + 1
    for i, n in enumerate(count):
        for j in range(n):
            A[k] = i
            k = k + 1

# Three-way partition with pivot = 1. One pass, thus O(n).
def sortColors2(A):
    i = j = -1
    for k in range(len(A)):
        if A[k] < 1:
            j = j + 1
            A[j], A[k] = A[k], A[j]
            i = i + 1
            A[i], A[j] = A[j], A[i]
        elif A[k] == 1:
            j = j + 1
            A[j], A[k] = A[k], A[j]

def main():
    A = [0, 0, 0, 1, 2, 1, 2, 2, 1, 2, 2]
    print A
    sortColors2(A)
    print A

main()
