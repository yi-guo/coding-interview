#!/usr/bin/python

# Given a matrix of m x n elements (m rows and n columns), return all elements of the matrix in spiral order.

# For example, given the following matrix:
#   [[ 1, 2, 3 ],
#    [ 4, 5, 6 ],
#    [ 7, 8, 9 ]]
# You should return [1, 2, 3, 6, 9, 8, 7, 4, 5].

# Get the spiral order layer by layer starting from the outmost.
def spiralOrder(matrix, layer=0):
    if layer == len(matrix) / 2:
        if len(matrix) % 2 == 0:
            return list()
        return list(matrix[layer][layer : len(matrix[0]) - layer])
    elif layer == len(matrix[0]) / 2:
        if len(matrix[0]) % 2 == 0:
            return list()
        len(matrix)
        return [matrix[i][len(matrix[0]) - layer - 1] for i in range(layer, len(matrix) - layer)]
    else:
        top = list(matrix[layer][layer : len(matrix[0]) - layer])
        right = [matrix[i][len(matrix[0]) - layer - 1] for i in range(layer + 1, len(matrix) - layer - 1)]
        bottom = list(reversed(matrix[len(matrix) - 1 - layer][layer : len(matrix[0]) - layer]))
        left = [matrix[i][layer] for i in range(len(matrix) - layer - 2, layer, -1)]
        return top + right + bottom + left + spiralOrder(matrix, layer + 1)

def main():
    matrix1 = [[ 1,  2,  3],
               [ 4,  5,  6],
               [ 7,  8,  9],
               [10, 11, 12]]

    matrix2 = [[1, 2, 3, 10],
               [4, 5, 6, 11],
               [7, 8, 9, 12]]

    matrix3 = [[7],[9],[6]]

    print spiralOrder(matrix1)
    print spiralOrder(matrix2)
    print spiralOrder(matrix3)

main()
