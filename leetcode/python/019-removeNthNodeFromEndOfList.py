#!/usr/bin/python

# Given a linked list, remove the nth node from the end of list and return its head.

# For example, given linked list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, after removing the second node from the end,
# the linked list becomes 1 -> 2 -> 3 -> 5.

# Note: Given n will always be valid, try to do this in one pass.

from LinkedList import LinkedList

# Two points move ahead. The second one starts moving when the first one is at the nth position. O(n).
def removeNthFromEnd(head, n):
    # If n = 0 or empty list, then do nothing.
    if n == 0 or not head:
        return head
    count = 0
    lead, rear = head, None
    while lead:
        if count == n:
            rear = head
        elif count > n:
            rear = rear.next
        lead = lead.next
        count = count + 1
    # If n is out of bound, then do nothing.
    if n > count:
        return head
    if not rear:
        head = head.next
    else:
        rear.next = rear.next.next
    return head

def main():
    lst = LinkedList([1, 2, 3, 4, 5])
    print lst
    print removeNthFromEnd(lst.head, 2)

main()
