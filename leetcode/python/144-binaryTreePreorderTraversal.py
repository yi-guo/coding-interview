#!/usr/bin/python

# Given a binary tree, return the preorder traversal of its nodes' values.

# For example, given binary tree [1, #, 2, 3],
#   1
#    \
#     2
#    /
#   3
# return [1, 2, 3].

# Note: Recursive solution is trivial, could you do it iteratively?

from leetcode.python import Tree


def preorderTraversal(root):
    tree = list()
    node, stack = root, list()
    while node or stack:
        if node:
            tree.append(node.val)
            if node.right:
                stack.append(node.right)
            node = node.left
        else:
            node = stack.pop()
    return tree

def main():
    T = Tree([1, 2, 3, 4, 5])
    print preorderTraversal(T.root)

main()
