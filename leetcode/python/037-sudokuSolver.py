#!/usr/bin/python

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# Empty cells are indicated by the character '.'.

# You may assume that there will be only one unique solution.

def solveSudoku(board):
    stack = list()
    # Put all unassigned cell into a stack.
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if board[i][j] == '.':
                stack.append((i, j))
    # Backtrack
    index = 0
    while 0 <= index < len(stack):
        i, j = stack[index]
        if assigned(board, i, j):
            index = index + 1
        else:
            index = index - 1
    return board

def assigned(board, i, j):
    curr = max(ord(board[i][j]), 48)
    for n in xrange(curr + 1, 58):
        if isValid(board, i, j, chr(n)):
            board[i][j] = chr(n)
            return True
    board[i][j] = '.'
    return False

def isValid(board, i, j, n):
    return checkRow(board, i, n) and checkCol(board, j, n) and checkBox(board, i, j, n)

def checkRow(board, i, n):
    for j in xrange(len(board[i])):
        if board[i][j] == n:
            return False
    return True

def checkCol(board, j, n):
    for i in xrange(len(board)):
        if board[i][j] == n:
            return False
    return True

def checkBox(board, i, j, n):
    row, col = i - i % 3, j - j % 3
    for i in xrange(row, row + 3):
        for j in xrange(col, col + 3):
            if board[i][j] == n:
                return False
    return True

def display(board):
    for row in board:
        print row

def main():
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    display(solveSudoku(board))

main()
