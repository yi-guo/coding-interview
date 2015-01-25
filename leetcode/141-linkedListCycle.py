#!/usr/bin/python

# Given a linked list, determine if it has a cycle in it.

# Follow up: Can you solve it without using extra space?

# Two pointers fast and slow with fast moving two nodes per iteration.
# If at any time fast meets slow, then the list has a cycle.
def hasCycle(head):
    if not head: return False
    slow, fast = head, head.next
    while fast and fast.next:
        if fast == slow:
            return True
        slow = slow.next
        fast = fast.next.next
    return False