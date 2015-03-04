#!/usr/bin/python

# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:
#   1. You may only use constant extra space.

# For example, given the following binary tree,
#         1
#       /  \
#      2    3
#     / \    \
#    4   5    7

# After calling your function, the tree should look like:
#         1 -> NULL
#       /  \
#      2 -> 3 -> NULL
#     / \    \
#    4-> 5 -> 7 -> NULL


# A revised version of the solution to problem "Populating Next Right Pointers in Each Node".
def connect(root):
    if not root:
        return None
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