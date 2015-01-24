#!/usr/bin/python

# Given a binary tree, find the maximum path sum.

# The path may start and end at any node in the tree.

# For example, given the below binary tree,
#       1
#      / \
#     2   3
# return 6.

def maxPathSum(root):
    if not root:
        return 0
    