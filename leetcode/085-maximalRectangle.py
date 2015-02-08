#!/usr/bin/python

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

def maximalRectangle(matrix):
    maximum = 0
    if not matrix:
        return maximum
    m, n = len(matrix), len(matrix[0])
    left = [0 for i in xrange(n)]
    right = [n for i in xrange(n)]
    height = [0 for i in xrange(n)]
    for i in xrange(m):
        currLeft, currRight = 0, n
        for j in xrange(n):
            if matrix[i][j] == '1':
                height[j] = height[j] + 1
                left[j] = max(left[j], currLeft)
            else:
                left[j] = 0
                height[j] = 0
                currLeft = j + 1
        for j in xrange(n - 1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], currRight)
            else:
                right[j] = n
                currRight = j
        for j in xrange(n):
            maximum = max(maximum, (right[j] - left[j]) * height[j])
    return maximum

def main():
    matrix = [['1', '1', '1', '1', '0', '1'],
              ['1', '1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1', '0'],
              ['0', '0', '1', '1', '1', '1']]
    print maximalRectangle(matrix)

main()
