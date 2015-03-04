#!/usr/bin/python

# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,

#   X X X X
#   X O O X
#   X X O X
#   X O X X

# After running your function, the board should be:

#   X X X X
#   X X X X
#   X X X X
#   X O X X

# Find 'O' on the four boundaries and conduct BFS, marking those that are NOT to be captured as 'S'.
def solve(board):
    if board and len(board) > 2 and len(board[0]) > 2:
        # Keey record of the 'O's on the boundaries and mark them as 'S'.
        queue = list()
        for i in range(len(board)):
            if board[i][0] == 'O':
                board[i][0] = 'S'
                queue.append((i, 0))
            if board[i][-1] == 'O':
                board[i][-1] = 'S'
                queue.append((i, len(board[i]) - 1))
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                board[0][i] = 'S'
                queue.append((0, i))
            if board[-1][i] == 'O':
                board[-1][i] = 'S'
                queue.append((len(board) - 1, i))
        # Conduct BFS and mark those can be searched as 'S'
        while queue:
            curr = queue.pop(0)
            i, j = curr[0], curr[1]
            if i - 1 > 0 and board[i - 1][j] == 'O':
                board[i - 1][j] = 'S'
                queue.append((i - 1, j))
            if i + 1 < len(board) and board[i + 1][j] == 'O':
                board[i + 1][j] = 'S'
                queue.append((i + 1, j))
            if j - 1 > 0 and board[i][j - 1] == 'O':
                board[i][j - 1] = 'S'
                queue.append((i, j - 1))
            if j + 1 < len(board[0]) and board[i][j + 1] == 'O':
                board[i][j + 1] = 'S'
                queue.append((i, j + 1))
        # Traverse the matrix, changing all 'S's to 'O' and 'O's to 'X'.
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

def main():
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    solve(board)
    print board

main()
