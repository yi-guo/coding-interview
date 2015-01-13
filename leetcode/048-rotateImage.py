#!/usr/bin/python

# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up: Could you do this in-place?

# Rotate the matirx layer by layer.
def rotate(matrix):
    if not matrix or len(matrix) < 2:
        return matrix
    n = len(matrix)
    for i in range(n / 2):
        for j in range((n + 1) / 2):
            temp = matrix[j][i]
            matrix[j][i] = matrix[n - i - 1][j]
            matrix[n - i - 1][j] = matrix[n - j - 1][n - i - 1]
            matrix[n - j - 1][n - i - 1] = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = temp
    return matrix

def main():
    matrix = [[ 0,  2,  3,  4,  5],
              [ 6,  7,  8,  9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    print rotate(matrix)

main()
