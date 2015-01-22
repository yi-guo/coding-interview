#!/usr/bin/python

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right,
# level by level from leaf to root).

# For example, given binary tree [3, 9, 20, #, #, 15, 7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its bottom-up level order traversal as [[15, 7], [9, 20], [3]]

from Tree import Tree

# Same approach as "Binary Tree Level Order Traversal", with front insertion of each level.
def levelOrderBottom(root):
    if not root: return list()
    tree, queue = list(), [root]
    while queue:
        level, length = list(), len(queue)
        for i in range(length):
            level.append(queue[i].val)
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)
        tree.insert(0, level)
        queue = queue[length:]
    return tree

def main():
    tree = Tree([3, 9, 20, '#', '#', 15, 7])
    print levelOrderBottom(tree.root)

main()
