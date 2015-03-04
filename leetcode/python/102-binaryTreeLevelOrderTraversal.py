#!/usr/bin/python

# Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# For example, given binary tree [3, 9, 20, #, #, 15, 7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its level order traversal as [[3], [9, 20], [15, 7]].

from leetcode.python import Tree

# Use queue to conduct level-order traversal. One pass, thus O(n).
def levelOrder(root):
    if not root: return list()
    tree, queue = list(), [root]
    while queue:
        level, length = list(), len(queue)
        for i in range(length):
            level.append(queue[i].val)
            if queue[i].left: queue.append(queue[i].left)
            if queue[i].right: queue.append(queue[i].right)
        tree.append(level)
        queue = queue[length:]
    return tree

def main():
    tree = Tree([3, 9, 20, '#', '#', 15, 7])
    print levelOrder(tree.root)

main()
