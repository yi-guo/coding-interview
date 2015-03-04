# -*- coding: utf-8 -*-

#!/usr/bin/python

# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3

# begin to intersect at node c1.

# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Get the difference in length of the two lists, and traverse the lists concurrently starting from the head
# of the shorter one and the kth node of the longer one where k = abs(diff). Terminate when they intersect.
def getIntersectionNode(headA, headB):
    lengthA = getLength(headA)
    lengthB = getLength(headB)
    diff = lengthA - lengthB
    if diff > 0:
        headA = getKthNode(headA, abs(diff))
    elif diff < 0:
        headB = getKthNode(headB, abs(diff))
    while headA:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

# Return the kth node in the given list.
def getKthNode(head, k):
    i, temp = 0, head
    while i < k:
        i = i + 1
        temp = temp.next
    return temp

# Return the length of the given list.
def getLength(head):
    temp, length = head, 0
    while temp:
        length += 1
        temp = temp.next
    return length
