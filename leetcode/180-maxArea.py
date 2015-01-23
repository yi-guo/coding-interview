#!/usr/bin/python

# Given a matrix of 0's and 1's, find the largest area formed by consecutive 1's in the matrix.

def maxArea(matrix):
	maximum = 0
	visited = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] and not visited[i][j]:
				maximum = max(maximum, area(matrix, visited, i, j))
	return maximum

def area(matrix, visited, i, j):
	if i < len(matrix) and j < len(matrix[0]) and matrix[i][j] and not visited[i][j]:
		visited[i][j] = 1
		return area(matrix, visited, i + 1, j) + area(matrix, visited, i - 1, j) + \
			   area(matrix, visited, i, j + 1) + area(matrix, visited, i, j - 1) + 1
	return 0

def main():
	matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 1, 1, 0, 0, 1, 1, 0],
			  [1, 0, 0, 1, 1, 0, 0, 1, 0],
			  [1, 0, 1, 1, 0, 1, 1, 1, 0],
			  [0, 1, 0, 1, 1, 0, 0, 0, 1],
			  [0, 0, 0, 0, 0, 0, 1, 1, 1]]
	print maxArea(matrix)

main()
