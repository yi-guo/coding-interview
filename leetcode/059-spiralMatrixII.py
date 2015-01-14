#!/usr/bin/python

# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example, given n = 3, you should return the following matrix:
# [[ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]]

import sys

# Generate the matrix inside out layer by layer recursively.
def generateMatrix(n, layer=0):
    if n == 0:
        return list()
    elif n == 1:
        return [[1]]
    if layer == (n - 1) / 2:
        matrix = [[0 for i in range(n)] for i in range(n)]
        if n % 2 == 0:
            matrix[layer][layer] = n * n - 3
            matrix[layer][layer + 1] = n * n - 2
            matrix[layer + 1][layer] = n * n
            matrix[layer + 1][layer + 1] = n * n - 1
        else:
            matrix[layer][layer] = n * n
        return matrix
    else:
        matrix = generateMatrix(n, layer + 1)
        num = matrix[layer + 1][layer + 1] - 1
        for i in range(layer + 1, n - layer):
            matrix[i][layer] = num
            matrix[n - layer - 1][i] = num - (n - layer * 2) + 1
            num = num - 1
        num = matrix[n - layer - 1][n - layer - 1] - 1
        for i in range(n - layer - 2, layer - 1, -1):
            matrix[i][n - layer - 1] = num
            matrix[layer][i] = num - (n - layer * 2) + 1
            num = num - 1
        return matrix

def main():
    print generateMatrix(int(sys.argv[1]))

main()
