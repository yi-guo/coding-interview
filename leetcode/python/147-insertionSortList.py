#!/usr/bin/python

# Sort a linked list using insertion sort.

from leetcode.python import LinkedList


def insertionSortList(head):
    if not head: return head
    prev = head
    curr = head.next
    while curr:
        if curr.val < prev.val:
            # Insert before head.
            if curr.val < head.val:
                next = curr.next
                curr.next = head
                prev.next = next
                head = curr
                curr = next
                continue
            # Insert somewhere.
            else:
                insert = head
                # Locate where to be inserted.
                while insert.next.val < curr.val:
                    insert = insert.next
                inext = insert.next
                cnext = curr.next
                insert.next = curr
                curr.next = inext
                prev.next = cnext
                curr = cnext
                continue
        prev = prev.next
        curr = curr.next
    return head

def main():
    L = LinkedList([3, 4, 1, 2, 6, 5, 7])
    print insertionSortList(L.head)

main()
