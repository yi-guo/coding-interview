#!/usr/bin/python

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Dynamic programming. O(mn).
def minPathSum(grid):
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    if m == 1:
        return sum(grid[0])
    elif n == 1:
        return sum([grid[i][0] for i in range(m)])
    for i in range(m - 2, -1, -1):
        grid[i][n - 1] += grid[i + 1][n - 1]
    for i in range(n - 2, -1, -1):
        grid[m - 1][i] += grid[m - 1][i + 1]
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
    return grid[0][0]

# Mah, do I need test cases for this easy problem?
