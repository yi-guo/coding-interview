#!/usr/bin/python

# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1 -> 1 -> 2, return 1 -> 2.
# Given 1 -> 1 -> 2 -> 3 -> 3, return 1 -> 2 -> 3.

from leetcode.python import LinkedList

# Traverse the list and manipulate the pointer to avoid duplicates. One pass, thus O(n).
def deleteDuplicates(head):
    if not head or not head.next:
        return head
    curr, temp = head, head.next
    while temp:
        if temp.val != curr.val:
            curr.next = temp
            curr = curr.next
        temp = temp.next
    # Eliminate the trailing duplicates as in [2, 3, 3]
    if curr.next and curr.val == curr.next.val:
        curr.next = None
    return head

def main():
    lst = [1, 1, 2, 3, 3]
    print "Before: %s" % lst
    print " After: %s" % deleteDuplicates(LinkedList(lst).head)

main()
