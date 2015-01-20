#!/usr/bin/python

# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# For example, given n = 3, your program should return all 5 unique BST's shown below.

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

# Generate the left and right subtrees recursively, then take the combinations.
def generateTrees(n):
    return generateTrees(1, n)

def generate(start, end):
    if start > end:
        return [None]
    trees = list()
    for i in range(start, end + 1):
        left = generateTrees(start, i - 1)
        right = generateTrees(i + 1, end)
        for l in left:
            for r in right:
                root = TreeNode(i)
                root.left = l
                root.right = r
                trees.append(root)
    return trees