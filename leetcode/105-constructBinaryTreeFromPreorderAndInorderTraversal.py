#!/usr/bin/python

# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note: You may assume that duplicates do not exist in the tree.

from Tree import Node, Tree

# The first element in preorder is the root.
# The root in inorder divides the list into halves, a.k.a., left and right.
# Find left and right in preorder, and build tree recursively following this property.
def buildTree(preorder, inorder):
    return build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

def build(preorder, inorder, pp, pr, ip, ir):
    if pp > pr: return None
    root = Node(preorder[pp])
    index = inorder.index(root.val)
    root.left = build(preorder, inorder, pp + 1, pp - ip + index, ip, index - 1)
    root.right = build(preorder, inorder, pr - ir + index + 1, pr, index + 1, ir)
    return root

def main():
    print buildTree([1, 2, 3], [1, 2, 3])

main()
