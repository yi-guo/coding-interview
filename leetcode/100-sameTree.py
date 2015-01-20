#!/usr/bin/python

# Given two binary trees, write a funciton to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Check the root and then the subtrees recursively.
def isSameTree(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False