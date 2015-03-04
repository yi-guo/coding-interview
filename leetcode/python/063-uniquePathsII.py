#!/usr/bin/python

# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example, there is one obstacle in the middle of a 3 x 3 grid as illustrated below.
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# The total number of unique paths is 2.

# Note: m and n will be at most 100.

# Same approach as "Unique Paths" with additional attentio of the obstacles. O(mn).
def uniquePathsWithObstacles(obstacleGrid):
    # If empty, then no path.
    if not obstacleGrid or not obstacleGrid[0]:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    # If obstacle is at 'Finish', then no path.
    if obstacleGrid[m - 1][n - 1] == 1:
        return 0
    # If one row, then 1 if no obstacle and 0 otherwise.
    elif m == 1:
        return int(1 not in obstacleGrid[0])
    # If one column, then 1 if no obstacle and 0 otherwise.
    elif n == 1:
        return int(1 not in [obstacleGrid[i][0] for i in range(m)])
    # If grid has two obstacles blocking the only two possible paths to 'Finish', then no path.
    elif obstacleGrid[m - 1][n - 2] == 1 and obstacleGrid[m - 2][n - 1] == 1:
        return 0
    d = list(obstacleGrid)
    d[m - 1][n - 1] = 1
    # Update the last column of d.
    for i in range(m - 2, -1, -1):
        if d[i][n - 1] or not d[i + 1][n - 1]:
            d[i][n - 1] = 0
            continue
        d[i][n - 1] = 1
    # Update the last row of d.
    for i in range(n - 2, -1, -1):
        if d[m - 1][i] or not d[m - 1][i + 1]:
            d[m - 1][i] = 0
            continue
        d[m - 1][i] = 1
    # Maintain the rest of d till d[0][0]
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if d[i][j]:
                d[i][j] = 0
                continue
            d[i][j] = d[i + 1][j] + d[i][j + 1]
    return d[0][0]

def main():
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print uniquePathsWithObstacles(obstacleGrid)

main()
