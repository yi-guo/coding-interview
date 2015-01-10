#!/usr/bin/python

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example, given this linked list: 1 -> 2 -> 3 -> 4 -> 5,
#   for k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5
#   for k = 3, you should return: 3 -> 2 -> 1 -> 4 -> 5

from LinkedList import Node, LinkedList, display

def reverseKGroup(head, k):
    i, temp = 0, head
    while i < k and temp:
        i = i + 1
        temp = temp.next
    if i < k:
        return head
    else:
        rest = reverseKGroup(temp.next, k)

def reverse(head):
    if not head.next:
        print head.val
        return (head, head)
    else:
        rest = reverse(head.next)
        rest[1].next = head
        return (rest[0], head)




def main():
    print display(reverse(LinkedList([1, 2, 3, 4]).head)[0])

main()
