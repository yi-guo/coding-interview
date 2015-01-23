#!/usr/bin/python

# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5, return
#	 [[1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]]

import sys

# Generate current one based on the previous one.
def generate(numRows):
    if numRows == 0: return []
    if numRows == 1: return [[1]]
    i, triangle = 2, [[1], [1, 1]]
    while i < numRows:
        curr = [1]
        prev = triangle[i - 1]
        for j in range(len(prev) - 1):
            curr.append(prev[j] + prev[j + 1])
        curr.append(1)
        triangle.append(curr)
        i = i + 1
    return triangle

def main():
    print generate(int(sys.argv[1]))

main()
