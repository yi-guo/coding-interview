#!/usr/bin/python

# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example, given 1 -> 2 -> 3 -> 4 -> 5 -> NULL and k = 2, return 4 -> 5 -> 1 -> 2 -> 3 -> NULL.

from LinkedList import LinkedList, toString

# Two pointers with the seconding one moving when the leading one is k nodes ahead.
def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
    i = 0
    curr = lead = head
    while lead.next:
        if i > k - 1:
            curr = curr.next
        lead = lead.next
        i = i + 1
    if k < i + 1:
        lead.next = head
        head = curr.next
        curr.next = None
        return head
    elif k > i + 1:
        return rotateRight(head, k % (i + 1))
    else:
        return head

def main():
    lst = LinkedList([1, 2, 3, 4, 5])
    print toString(rotateRight(lst.head, 6))

main()
