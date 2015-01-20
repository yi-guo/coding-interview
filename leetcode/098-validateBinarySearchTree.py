#!/usr/bin/python

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:
#   1. The left subtree of a node contains only nodes with keys less than the node's key.
#   2. The right subtree of a node contains only nodes with keys greater than the node's key.
#   3. Both the left and right subtrees must also be binary search trees.

# Recursively check validity.
def isValidBST(root, minimum=float('-inf'), maximum=float('inf')):
    if not root:
        return True
    res = True
    if root.left:
        res = minimum < root.left.val < root.val and isValidBST(root.left, minimum, min(root.val, maximum))
    if root.right:
        res = res and root.val < root.right.val < maximum and isValidBST(root.right, max(root.val, minimum), maximum)
    return res
