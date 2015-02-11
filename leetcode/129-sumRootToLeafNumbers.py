#!/usr/bin/python

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# For example,
#    1
#   / \
#  2   3

# The root-to-leaf path 1 -> 2 represents the number 12.
# The root-to-leaf path 1 -> 3 represents the number 13.

# Return the sum = 12 + 13 = 25.

from Tree import Tree

# Get the list of numbers recursively from left and right subtrees and return the sum.
def sumNumbers(root, num=0):
    if not root:
        return 0
    num = num * 10 + root.val
    if not root.left and not root.right:
        return num
    return sumNumbers(root.left, num) + sumNumbers(root.right, num)

def main():
    tree = Tree([5, 3, 2, 7, 0, 6, '#', '#', '#', 0])
    print sumNumbers(tree.root)

main()
