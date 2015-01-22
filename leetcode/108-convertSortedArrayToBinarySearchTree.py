#!/usr/bin/python

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

from Tree import Node, Tree

# Select the median as the root and recursively build the tree.
def sortedArrayToBST(num):
    if not num: return None
    mid = len(num) / 2
    root = Node(num[mid])
    root.left = sortedArrayToBST(num[:mid])
    root.right = sortedArrayToBST(num[mid + 1:])
    return root

def main():
    print sortedArrayToBST([1, 2, 3, 4, 5])

main()
