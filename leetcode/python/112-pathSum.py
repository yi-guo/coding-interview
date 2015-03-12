#!/usr/bin/python

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# For example, given the below binary tree and sum = 22,
#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \      \
#        7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

from Tree import Tree

# Recursively check if any of the subtrees has sum of sum - root.val
def hasPathSum(root, sum):
    if not root:
        return False
    elif root.val == sum and not root.left and not root.right:
        return True
    else:
        return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)

def main():
    tree = Tree([5, 4, 8, 11, '#', 13, 4, 7, 2, '#', 1])
    print hasPathSum(tree.root, 22)

main()
