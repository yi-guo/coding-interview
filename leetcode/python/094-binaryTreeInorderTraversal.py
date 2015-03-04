#!/usr/bin/python

# Given a binary tree, return the inorder traversal of its nodes' values.

# For example, given binary tree {1, #, 2, 3},

#   1
#    \
#     2
#    /
#   3

# return [1,3,2].

# Note: Recursive solution is trivial, could you do it iteratively?

def inorderTraversal(root):
    res, temp, stack = list(), root, list()
    while stack or temp:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            res.append(temp.val)
            temp = temp.right
    return res