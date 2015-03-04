#!/usr/bin/python

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.

# Recursively check difference in heights while computing them bottom up.
# Each node is ONLY visited once, thus O(n).
def isBalanced(root):
    if height(root) == -1:
        return False
    return True

def height(node):
    # Leaf, return 0
    if not node:
        return 0
    # Get the height of the left child, and if not balanced already, return False and exit.
    left = height(node.left)
    if left == -1:
        return left
    # Get the height of the right child, and if not balanced already, return False and exit.
    right = height(node.right)
    if right == -1:
        return right
    # Check the difference in height of the two subtrees, if not balanced, return False and exit.
    if abs(left - right) > 1:
        return -1
    # Otherwise, return the normal height.
    return max(left, right) + 1

# THE BEST SOLUTION. No need to test.