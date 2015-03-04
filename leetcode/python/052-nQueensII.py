#!/usr/bin/python

# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.

def solveNQueens(n):
    solutions = [[['.' for i in xrange(n)] for j in xrange(n)]]
    for i in xrange(n):
        length = len(solutions)
        for k in xrange(length):
            for j in xrange(n):
                if isValid(solutions[k], i, j):
                    board = [list(row) for row in solutions[k]]
                    board[i][j] = 'Q'
                    solutions.append(board)
        solutions = solutions[length:]
    return len(solutions)

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
    print solveNQueens(4)

main()
