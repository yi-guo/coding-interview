#!/usr/bin/python

# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.

# For example,
# Given 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, return 1 -> 2 -> 5.
# Given 1 -> 1 -> 1 -> 2 -> 3, return 2 -> 3.

from leetcode.python import LinkedList

# Modified from "Remove Duplicates from Sorted List". Still one pass, thus O(n).
def deleteDuplicates(head):
    if not head or not head.next:
        return head
    # Indicates if head needs to be relocated later.
    flag = head.val == head.next.val
    prev, curr, temp = head.val, head, head.next
    while temp.next:
        # Safe to move curr when temp is not its next nor the previous value.
        if temp.val != temp.next.val and temp.val != prev:
            curr.next = temp
            curr = curr.next
        prev = temp.val
        temp = temp.next
    # If the last element is distinct, append it; otherwise, close.
    if temp.val != prev:
        curr.next = temp
    else:
        curr.next = None
    # Increment head if flag; otherwise, return head.
    return head.next if flag else head

def main():
    lst = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    print deleteDuplicates(LinkedList(lst).head)

main()
