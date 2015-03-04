#!/usr/bin/python

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right,
# then right to left for the next level and alternate between).

# For example, given binary tree {3, 9, 20, #, #, 15, 7},
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its zigzag level order traversal as [[3], [20, 9], [15, 7]].

from leetcode.python import Tree

# Level order traversal with flag controling the insertion position of each level.
def zigzagLevelOrder(root):
    if not root: return list()
    flag, tree, queue = True, list(), [root]
    while queue:
        level, length = list(), len(queue)
        for i in range(length):
            # If flag, insert at the end; otherwise, the front.
            level.insert(flag * (length - 1), queue[i].val)
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)
        flag = not flag
        tree.append(level)
        queue = queue[length:]
    return tree

def main():
    tree = Tree([3, 9, 20, '#', '#', 15, 7])
    print zigzagLevelOrder(tree.root)

main()
