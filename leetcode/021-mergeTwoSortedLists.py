#!/usr/bin/python

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# A straight forward solution that compares while moving foward. O(n)
def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    head = None
    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next
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
    elif l2:
        temp.next = l2
    return head

# Mah, do I need test cases for such an easy problem?
