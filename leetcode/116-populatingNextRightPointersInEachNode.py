#!/usr/bin/python

# Given a binary tree

#   struct TreeLinkNode {
#       TreeLinkNode *left;
#   	TreeLinkNode *right;
#   	TreeLinkNode *next;
#   }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
# should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:
#   1. You may only use constant extra space.
#   2. You may assume that it is a perfect binary tree (i.e., all leaves are at the same level,
#	   and every parent has two children).

# For example, given the following perfect binary tree,
#         1
#       /  \
#      2    3
#     / \  / \
#    4  5  6  7

#After calling your function, the tree should look like:
#         1 -> NULL
#       /  \
#      2 -> 3 -> NULL
#     / \  / \
#    4->5->6->7 -> NULL

from Tree import Tree

# Level-order traversal and manipulate the next pointer to its right except the last one in current level.
def connect(root):
    if not root: return None
    queue = [root]
    while queue:
        length = len(queue)
        for i in range(length):
            if i == length - 1:
                queue[i].next = None
            else:
                queue[i].next = queue[i + 1]
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)
        queue = queue[length:]
    return root

def main():
    tree = Tree([1, 2, 3, 4, 5, 6, 7])
    print connect(tree.root)

main()
