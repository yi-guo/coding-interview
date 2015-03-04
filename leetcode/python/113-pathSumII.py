#!/usr/bin/python

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example, given the below binary tree and sum = 22,
#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \    / \
#        7    2  5   1
# return [[5, 4, 11, 2], [5, 8, 4, 5]]

from leetcode.python import Tree


def pathSum(root, sum):
    if not root:
        return list()
    elif root.val == sum and not root.left and not root.right:
        return [[root.val]]
    else:
        left = pathSum(root.left, sum - root.val)
        right = pathSum(root.right, sum - root.val)
        for path in left + right:
            path.insert(0, root.val)
        return left + right

def main():
    tree = Tree([5, 4, 8, 11, '#', 13, 4, 7, 2, '#', '#', 5, 1])
    print pathSum(tree.root, 22)

main()
