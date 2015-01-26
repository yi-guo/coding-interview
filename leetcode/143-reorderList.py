#!/usr/bin/python

# Given a singly linked list L: L0 -> L1 -> ... -> Ln-1 -> Ln, reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

# You must do this in-place without altering the nodes' values.

# For example, given [1, 2, 3, 4], reorder it to [1, 4, 2, 3].

from LinkedList import LinkedList

# 1. Divide the list into halves.
# 2. Reverse the second half.
# 3. Merge the two lists.
def reorderList(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return merge(head, reverse(slow))

def reverse(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def merge(l1, l2):
    head = l1
    while l1 and l2:
        n1 = l1.next
        n2 = l2.next
        l1.next = l2
        l1 = n1
        l2.next = l1
        l2 = n2
    if l1: l1.next = None
    return head

def main():
    L = LinkedList(range(1, 5))
    print reorderList(L.head)

main()
