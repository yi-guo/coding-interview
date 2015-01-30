#!/usr/bin/python

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

from LinkedList import Node


# A straight forward solution that compares while moving foward. O(n)
def mergeTwoLists(l1, l2):
    head = Node(0)
    temp = head
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if l1:
        temp.next = l1
    if l2:
        temp.next = l2
    return head.next

# Mah, do I need test cases for such an easy problem?
