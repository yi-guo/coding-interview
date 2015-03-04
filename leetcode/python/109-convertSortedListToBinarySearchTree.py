#!/usr/bin/python

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

from leetcode.python.Tree import TreeNode
from leetcode.python import LinkedList

# Initialize curr to keep a pointer of the current position in the list.
curr = None

# Get the size of the list first and then construct the tree bottom-up. Two passes, thus O(n).
def sortedListToBST(head):
    # Assign the global curr to head
    global curr 
    curr = head
    return convert(length(head))

# Return the size of the list.
def length(head):
    temp, size = head, 0
    while temp:
        size = size + 1
        temp = temp.next
    return size

# Construct BST bottom-up following an inorder traversal.
def convert(size):
    if size < 1: return None
    global curr
    # Recursively construct the left subtree of half size of the current tree.
    left = convert(size / 2)
    # Create the root for the current tree.
    root = TreeNode(curr.val)
    root.left = left
    # Move the pointer and recursively construct the right subtree.
    curr = curr.next
    root.right = convert(size - size / 2 - 1)
    return root

def main():
    lst = LinkedList([1, 2, 3, 4, 5])
    print sortedListToBST(lst.head)

main()
