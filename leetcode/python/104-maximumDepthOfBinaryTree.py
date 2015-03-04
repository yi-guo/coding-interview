#!/usr/bin/python

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from leetcode.python import Tree

# Compute recursively and return the maximum depth of the left and right subtree
def maxDepth(root, depth=0):
    if not root:
        return depth
    return max(maxDepth(root.left, depth + 1), maxDepth(root.right, depth + 1))

def main():
    tree = Tree([1, 2, 3])
    print maxDepth(tree.root)

main()
