#!/usr/bin/python

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen
# and an empty space respectively.

# For example, there exists two distinct solutions to the 4-queens puzzle:

#  [[".Q..",  // Solution 1
#    "...Q",
#    "Q...",
#    "..Q."],
#
#   ["..Q.",  // Solution 2
#    "Q...",
#    "...Q",
#    ".Q.."]]

def solveNQueens(n):
    solutions = [[['.' for i in xrange(n)] for j in xrange(n)]]
    for i in xrange(n):
        length = len(solutions)
        for k in xrange(length):
            for j in xrange(n):
                if isValid(solutions[k], i, j):
                    board = [list(row) for row in solutions[k]]
                    board[i][j] = 'Q'
                    solutions.append([''.join(row) for row in board])
        solutions = solutions[length:]
    return solutions

def isValid(board, i, j):
    return checkColumn(board, j) and checkDiagonal(board, i, j)

def checkColumn(board, j):
    for i in xrange(len(board)):
        if board[i][j] == 'Q':
            return False
    return True

def checkDiagonal(board, row, col):
    i, j = max(row - col, 0), max(col - row, 0)
    while i < len(board) and j < len(board):
        if board[i][j] == 'Q':
            return False
        i, j = i + 1, j + 1
    i = min(row + col, len(board) - 1)
    j = col - i + row
    while i > -1 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i, j = i - 1, j + 1
    return True

def display(solutions):
    for solution in solutions:
        print solution
    print

def main():
    display(solveNQueens(4))

main()
