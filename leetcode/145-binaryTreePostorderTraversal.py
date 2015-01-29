#!/usr/bin/python

# Given a binary tree, return the postorder traversal of its nodes' values.

# For example, given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?

def postorderTraversal(root):
    tree, prev = list(), None
    node, stack = root, list()
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek = stack[-1]
            if peek.right and peek.right != prev:
                node = peek.right
            else:
                tree.append(peek.val)
                prev = stack.pop()
    return tree