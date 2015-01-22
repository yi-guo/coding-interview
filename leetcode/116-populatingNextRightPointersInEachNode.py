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
    while temp:
        if temp.left or temp.right:
            curr = temp
            prev = curr.left if curr.left else curr.right
            while curr:
                if curr.left and curr.left != prev:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right and curr.right != prev:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            temp = temp.left if temp.left else temp.right
        else:
            temp = temp.next
    return root
