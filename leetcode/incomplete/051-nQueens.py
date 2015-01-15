#!/usr/bin/python

from pprint import pprint

def solveNQueens(n):
    board = [['.' for i in range(n)] for j in range(n)]
    i = 0
    while i >= 0 and i < n:
        index = move(board, i)
        if index == -1:
            board[i] = ['.' for i in range(n)]
            i = i - 1
        else:
            if not check(board, i, index):
                board[i][index] = 'Q'
                i = i + 1
    if i == -1:
        return "No solution"
    return board

def move(board, i):
    for j in range(len(board)):
        if board[i][j] == 'Q':
            if j == len(board) - 1:
                return -1
            board[i][j] = '.'
            return j + 1
    return 0

def check(board, i, j):
    column = [board[k][j] for k in range(len(board))]
    if 'Q' in column:
        return True
    k = 1
    while i + k < len(board) and j + k < len(board):
        if board[i + k][j + k] == 'Q':
            return True
        k = k + 1
    k = 1
    while i - k >= 0 and j - k >= 0:
        if board[i - k][j - k] == 'Q':
             return True
        k = k + 1
    k = 1
    while i - k >= 0 and j + k < len(board):
        if board[i - k][j + k] == 'Q':
            return True
        k = k + 1
    k = 1
    while i + k < len(board) and j - k >= 0:
        if board[i + k][j - k] == 'Q':
            return True
        k = k + 1
    return False

def main():
    pprint(solveNQueens(8))


main()
