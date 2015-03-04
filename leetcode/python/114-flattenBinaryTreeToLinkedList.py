#!/usr/bin/python

# Given a binary tree, flatten it to a linked list in-place.

# For example, given
#         1
#        / \
#       2   5
#      / \   \
#     3   4   6
# The flattened tree should look like:
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6

from leetcode.python import Tree

# Flatten the left and right trees recursively and then manipulate the pointers for the current node.
def flatten(root, depth=0):
    if not root:
        return None
    if not root.left and not root.right:
        return root if not depth else (root, root)
    elif not root.left and root.right:
        right = flatten(root.right, depth + 1)
        return root if not depth else (root, right[1])
    elif root.left and not root.right:
        left = flatten(root.left, depth + 1)
        root.right = root.left
        root.left = None
        return root if not depth else (root, left[1])
    else:
        left = flatten(root.left, depth + 1)
        right = flatten(root.right, depth + 1)
        root.left = None
        root.right = left[0]
        left[1].right = right[0]
        return root if not depth else (root, right[1])

def main():
    tree = Tree([1, 2, 5, 3, 4, '#', 6])
    print flatten(tree.root)

main()
