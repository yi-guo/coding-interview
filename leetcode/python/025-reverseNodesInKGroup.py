#!/usr/bin/python

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example, given this linked list: 1 -> 2 -> 3 -> 4 -> 5,
#   for k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5
#   for k = 3, you should return: 3 -> 2 -> 1 -> 4 -> 5

from leetcode.python import LinkedList

# Reverse every k nodes recursively. Each node is accessed once, thus O(n).
def reverseKGroup(head, k):
    if k < 2 or not head or not head.next:
        return head
    i, temp = 0, head
    while i < k and temp:
        i = i + 1
        temp = temp.next
    if i < k:
        return head
    else:
        rest = reverseKGroup(temp, k)
        revs = reverse(head, temp)
        revs[1].next = rest
        return revs[0]

# Return (head, tail) of the reversed list.
def reverse(head, end):
    if head.next == end:
        return (head, head)
    else:
        rest = reverse(head.next, end)
        rest[1].next = head
        head.next = None
        return (rest[0], head)

def main():
    print "Given: %s" % LinkedList([1, 2, 3, 4, 5])
    print "k = 2: %s" % reverseKGroup(LinkedList([1, 2, 3, 4, 5]).head, 2)
    print "k = 3: %s" % reverseKGroup(LinkedList([1, 2, 3, 4, 5]).head, 3)

main()
