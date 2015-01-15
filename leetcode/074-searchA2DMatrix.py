#!/usr/bin/python

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example, consider the following matrix:

#   [[ 1,  3,  5,  7],
#    [10, 11, 16, 20],
#    [23, 30, 34, 50]]

# Given target = 3, return true.

# Binary search the row and then within the row. Hence, O(log(m) * log(n)).
def searchMatrix(matrix, target):
    # False if empty matrix.
    if not matrix or not matrix[0]:
        return False
    # False if target is smaller than the smallest in the matrix.
    if target < matrix[0][0]:
        return False
    # False if target is larger than the largest in the matrix.
    elif target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
        return False
    # Binary search the row.
    i, j = 0, len(matrix) - 1
    while i <= j:
        m = (i + j) / 2
        if matrix[m][0] < target:
            i = m + 1
        elif matrix[m][0] > target:
            j = m - 1
        else:
            return True
    # Binary search within the row.
    k = i - 1
    i, j = 0, len(matrix[k]) - 1
    while i <= j:
        m = (i + j) / 2
        if matrix[k][m] < target:
            i = m + 1
        elif matrix[k][m] > target:
            j = j - 1
        else:
            return True
    return False

def main():
    matrix = [[ 1,  3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50],
              [56, 58, 61, 63],
              [67, 69, 70, 72]]
    print searchMatrix(matrix, 30)

main()
