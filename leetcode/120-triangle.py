#!/usr/bin/python

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
#    [[2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]]

# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# Dynamic programming.
# Notice that at any time, triangle[i][j]'s adjacent item indices in triangle[i + 1] is j and j + 1.
# Maintain d such that d[j] is the minimum path sum from triangle[i][j] for any valid i n - 2 ... 0.
def minimumTotal(triangle):
    d = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            d[j] = triangle[i][j] + min(d[j], d[j + 1])
    return d[0]

def main():
    print minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])

main()
