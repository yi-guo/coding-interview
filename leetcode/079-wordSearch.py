#!/usr/bin/python

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example, given board =
#   ["ABCE",
#    "SFCS",
#    "ADEE"]

# word = "ABCCED" -> returns true,
# word = "SEE" -> returns true,
# word = "ABCB" -> returns false.

# The following presents a recursive solution to the problem. Do search for each cell on board.
def exist(board, word):
    if not board or not board[0]:
        return False
    if not word:
        return True
    visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if found(board, word, 0, visited, i, j):
                return True
    return False

# Return true if word is found at board[i][j]
def found(board, word, curr, visited, i, j):
    # Search is over, return true.
    if curr >= len(word):
        return True
    # Out of boundary, return false.
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
        return False
    # Current cell has been used once, thus false.
    if visited[i][j]:
        return False
    # Current cell does not have the needed character, thus false.
    if board[i][j] != word[curr]:
        return False
    # Otherwise, presume good so far.
    # Mark the current cell as used and recursively search adjacent cells.
    visited[i][j] = True
    search = found(board, word, curr + 1, visited, i - 1, j) or found(board, word, curr + 1, visited, i + 1, j) or \
             found(board, word, curr + 1, visited, i, j + 1) or found(board, word, curr + 1, visited, i, j - 1)
    # If any of the four adjacent cells presents true, then found!
    visited[i][j] = False
    return search

# The following BFS approach works, but exceeds the time limit on LeetCode.
#
# def exist(board, word):
#     pos, chars = {c : [] for c in word}, set(word)
#     for i in range(len(board)):
#         for j, c in enumerate(board[i]):
#             if c in chars:
#                 pos[c].append((i, j))
#     paths = [[]]
#     for c in word:
#         i, length = 0, len(paths)
#         while i < length:
#             path = paths.pop(0)
#             if not path:
#                 paths.extend([[cell] for cell in pos[c]])
#             else:
#                 curr = path[-1]
#                 for cell in pos[c]:
#                     if cell not in path and adjacent(curr, cell):
#                         paths.append(path + [cell])
#             i = i + 1
#     return len(paths) > 0
#
# def adjacent(c1, c2):
#     return c2 == (c1[0] + 1, c1[1]) or c2 == (c1[0] - 1, c1[1]) or \
#            c2 == (c1[0], c1[1] + 1) or c2 == (c1[0], c1[1] - 1) and c1 != c2

def main():
    board = ["ABCE",
             "SFCS",
             "ADEE"]
    print exist(board, "ABCCED")

main()
