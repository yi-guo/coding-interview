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
def sumNumbers(root):
    if not root:
        return 0
    return sum([int(''.join(n)) for n in pathSums(root)])
    
def pathSums(root):
    if root.left and root.right:
        return [[str(root.val)] + n for n in pathSums(root.left) + pathSums(root.right)]
    if root.left:
        return [[str(root.val)] + n for n in pathSums(root.left)]
    if root.right:
        return [[str(root.val)] + n for n in pathSums(root.right)]
    return [[str(root.val)]]

def main():
    tree = Tree([5, 3, 2, 7, 0, 6, '#', '#', '#', 0])
    print sumNumbers(tree.root)

main()
