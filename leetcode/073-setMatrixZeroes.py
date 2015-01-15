#!/usr/bin/python

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

import pprint

# Use elements in the first row and column as flags. O(mn) in time and O(1) in space.
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    # Check the first row and column.
    row = 0 in matrix[0]
    column = 0 in [matrix[i][0] for i in range(m)]
    # For each (i,j) if matrix[i][j] = 0, set flag.
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # Zero rows.
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0
    # Zero columns.
    for i in range(1, n):
        if matrix[0][i] == 0:
            for j in range(1, m):
                matrix[j][i] = 0
    # Zero the first row, if needed.
    if row:
        for i in range(n):
            matrix[0][i] = 0
    # Zero the first column, if needed.
    if column:
        for i in range(m):
            matrix[i][0] = 0

def main():
    matrix = [[1, 1, 0, 1, 1],
              [0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 1, 1, 0],
              [1, 1, 1, 1, 1]]
    pp = pprint.PrettyPrinter(width=20)
    pp.pprint(matrix)
    setZeroes(matrix)
    pp.pprint(matrix)

main()
