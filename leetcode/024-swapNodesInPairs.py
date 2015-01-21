#!/usr/bin/python

# Given a linked list, swap every two adjacent nodes and return its head.

# For example, given 1 -> 2 -> 3 -> 4, you should return the list as 2 -> 1 -> 4 -> 3.

# Your algorithm should use only constant space. You may not modify the values in the list.
# Only nodes itself can be changed.

from LinkedList import LinkedList

# Recursively traverse to the end of the list and start swapping backward.
# T(n) = T(n-2) + O(1), thus O(n).
def swapPairs(head):
    if not head or not head.next:
        return head
    else:
        rest = swapPairs(head.next.next)
        temp = head.next
        temp.next = head
        head.next = rest
        return temp

def main():
    print swapPairs(LinkedList([1, 2, 3, 4]).head)

main()
