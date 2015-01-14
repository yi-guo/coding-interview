#!/usr/bin/python

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach
# the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Note: m and n will be at most 100.

# Dynamic programming. 
# Construct a matrix d where d[i][j] indicates the number of unique paths from grid[i][j] to 'Finish'.
# Fill d from d[m-2][n-2] back to d[0][0] and d[0][0] will be the answer, thus O(mn).
def uniquePaths(m, n):
    if m < 1 or n < 1:
        return 0
    elif m == 1 or n == 1:
        return 1
    d = [[1 for i in range(n)] for i in range(m)]
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            d[i][j] = d[i][j + 1] + d[i + 1][j]
    return d[0][0]

def main():
    print uniquePaths(3, 3)

main()
