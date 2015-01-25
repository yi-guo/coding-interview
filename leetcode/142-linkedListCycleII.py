#!/usr/bin/python

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Follow up: Can you solve it without using extra space?

# A revised solution for problem "Linked List Cycle".
# Notice that when fast meets slow, set fast to head and let them walk together at the same speed, which gives
# the start of the cycle when they meet again.
def detectCycle(head):
    if not head: return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            fast = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return fast
    return None
