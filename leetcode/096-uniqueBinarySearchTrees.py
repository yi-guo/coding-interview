#!/usr/bin/python

# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

# For example, given n = 3, there are a total of 5 unique BST's.

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

import sys

# Dynamic programming.
# n = 0, there is only one BST, which is NULL
# n = 1, there is only one BST, which is 1 as the root
# n = 2, there are two BST's, which are 1 as the root and 2 as the root
# Hence, given the BST property, construct a 1-dimension DP array d, where d[i] indicates the number
# of unique BST's to store values 1...i
# Notice that each value in 1...i can be put as root, and the number of unique trees is simply
# d[0...j - 1] * d[j + 1 ... i] if j is at root.
# Do so for each j in 1...i, the solution is the sum.
def numTrees(n):
    d = [0 if i > 1 else 1 for i in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i):
            d[i] += d[j] * d[i - j - 1]
    return d[n]

def main():
    print numTrees(int(sys.argv[1]))

main()
