#!/usr/bin/python

# Given a binary tree, find the maximum path sum.

# The path may start and end at any node in the tree.

# For example, given the below binary tree,
#       1
#      / \
#     2   3
# return 6.

from leetcode.python import Tree

# Recursively compute the maximum path sum for the subtrees.
# Maximum path sum occurs in the following four cases only:
#   1. current node
#   2. current node + left maximum path sum
#   3. current node + right maximum path sum
#   4. current node + left and right maximum path sum
def maxPathSum(root):
    pathSum = [float('-inf')]
    maxStraightPathSum(root, pathSum)
    return pathSum[0]

def maxStraightPathSum(root, pathSum):
    if not root:
        return 0
    left = maxStraightPathSum(root.left, pathSum)
    right = maxStraightPathSum(root.right, pathSum)
    arch = left + right + root.val
    straight = max(root.val, max(left, right) + root.val)
    pathSum[0] = max(pathSum[0], arch, straight)
    return straight

def main():
    tree = Tree([-1, -2, -5, -3, 3000, '#', '#', '#', '#', 2000, -3000])
    print maxPathSum(tree.root)

main()
