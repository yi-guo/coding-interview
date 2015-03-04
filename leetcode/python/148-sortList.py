#!/usr/bin/python

# Sort a linked list in O(nlog(n)) time using constant space complexity.

from leetcode.python import LinkedList

# Merge sort. Two pointers to partition the list recursively and merge. O(nlog(n)).
def sortList(head):
    return mergeSort(head)

def mergeSort(head):
    if not head or not head.next:
        return head
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        if not fast: break
        slow = slow.next
    temp = slow.next
    slow.next = None
    l1 = mergeSort(head)
    l2 = mergeSort(temp)
    return merge(l1, l2)

def merge(l1, l2):
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

def main():
    L = LinkedList([6, 5, 3, 1, 8, 7, 2, 4])
    print sortList(L.head)

main()
