#!/usr/bin/python

# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example, given 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, return 1 -> 2 -> 2 -> 4 -> 3 -> 5.

from LinkedList import ListNode
from LinkedList import LinkedList

# Two dummy nodes. One pass. O(n) in time and O(1) in space.
def partition(head, x):
    curr = head
    head = tempHead = ListNode(0)
    pivot = tempPivot = ListNode(x)
    while curr:
        if curr.val < x:
            tempHead.next = curr
            tempHead = tempHead.next
        else:
            tempPivot.next = curr
            tempPivot = tempPivot.next
        curr = curr.next
    tempHead.next = pivot.next
    tempPivot.next = None
    return head.next

def main():
    lst = LinkedList([1, 4, 3, 2, 5, 2])
    print partition(lst.head, 3)

main()
