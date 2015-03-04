#!/usr/bin/python

# Determine if a Sudoku is valid, according to http://sudoku.com.au/TheRules.aspx.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# Note: A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

# Check validity for each row, column, and grid, thus O(3 * 9 * 9).
def isValidSudoku(board):
    for i in range(len(board)):
        if not isValid(filter(lambda x : x != '.', board[i])):
            return False
    for i in range(len(board)):
        if not isValid(filter(lambda x : x != '.', [row[i] for row in board])):
            return False
    for i in range(0, len(board), 3):
        grid = [row[i : i + 3] for row in board]
        for j in range(0, len(grid), 3):
            if not isValid(filter(lambda x : x != '.', [n for g in grid[j : j + 3] for n in g])):
                return False
    return True

# Return TRUE if no digit appears twice.
def isValid(lst):
    exist = set()
    for n in lst:
        if n in exist:
            return False
        else:
            exist.add(n)
    return True

def main():
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    print isValidSudoku(board)

main()
