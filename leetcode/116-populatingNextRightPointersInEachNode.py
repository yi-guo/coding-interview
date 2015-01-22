#!/usr/bin/python

# Given a binary tree

#   struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#   }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
# should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:
#   1. You may only use constant extra space.
#   2. You may assume that it is a perfect binary tree (i.e., all leaves are at the same level,
#      and every parent has two children).

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

# Manipulate the next pointer level by level.
def connect(root):
    if not root: return None
    temp = root
    while temp.left:
        curr = temp
        while curr:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        temp = temp.left
    return root
