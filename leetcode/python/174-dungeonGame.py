#!/usr/bin/python

# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
# consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room
# and must fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point
# drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
# other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path
# RIGHT-> RIGHT -> DOWN -> DOWN.

# -2 (K)  -3    3
# -5	 -10    1
# 10      30   -5 (P)

# Notes:
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room
# where the princess is imprisoned.

# Dynamic programming. O(n^2) in time.
def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    dungeon[-1][-1] = abs(dungeon[-1][-1]) + 1 if dungeon[-1][-1] < 0 else 1
    for i in xrange(m - 2, -1, -1):
        dungeon[i][-1] = abs(dungeon[i][-1]) + dungeon[i + 1][-1] if dungeon[i][-1] < 0 else max(dungeon[i + 1][-1] - dungeon[i][-1], 1)
    for i in xrange(n - 2, -1, -1):
        dungeon[-1][i] = abs(dungeon[-1][i]) + dungeon[-1][i + 1] if dungeon[-1][i] < 0 else max(dungeon[-1][i + 1] - dungeon[-1][i], 1)
    for i in xrange(m - 2, -1, -1):
        for j in xrange(n - 2, -1, -1):
            dungeon[i][j] = abs(dungeon[i][j]) + min(dungeon[i + 1][j], dungeon[i][j + 1]) if dungeon[i][j] < 0 else max(min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j], 1)
    return dungeon[0][0]

def main():
    dungeon = [[-2, -3, 3],
               [-5, -10, 1],
               [10, 30, -5]]
    print calculateMinimumHP(dungeon)

main()
