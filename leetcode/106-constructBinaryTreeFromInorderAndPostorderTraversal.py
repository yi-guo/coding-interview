#!/usr/bin/python

# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note: You may assume that duplicates do not exist in the tree.

from Tree import Node, Tree

# The last element in postorder is the root.
# The root in inorder divides the list into halves, a.k.a., left and right.
# Find left and right in postorder, and build tree recursively following this property.
def buildTree(inorder, postorder):
    return build(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

def build(inorder, postorder, ip, ir, pp, pr):
    if ip > ir: return None
    root = Node(postorder[pr])
    index = inorder.index(postorder[pr])
    root.left = build(inorder, postorder, ip, index - 1, pp, pp - ip + index - 1)
    root.right = build(inorder, postorder, index + 1, ir, pr - ir + index, pr - 1)
    return root

def main():
    print buildTree([10, 30, 40, 50, 60, 70, 90], [10, 40, 30, 60, 90, 70, 50])

main()
