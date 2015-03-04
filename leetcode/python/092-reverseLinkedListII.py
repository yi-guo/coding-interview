#!/usr/bin/python

# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example: given 1 -> 2 -> 3 -> 4 -> 5 -> NULL, m = 2 and n = 4, return 1 -> 4 -> 3 -> 2 -> 5 -> NULL.

# Note: m, n satisfy the following condition: 1 <= m <= n <= length of list.

from leetcode.python import LinkedList

# A recursive approach. Strictly one pass, thus O(n).
def reverseBetween(head, m, n):
    if not head or not head.next or m == n:
        return head
    return reverse(head, m, n, 1)[0]

# Recursively return (head, tail, tail.next) for the ith node.
def reverse(head, m, n, i):
    if i < m:
        rest = reverse(head.next, m, n, i + 1)
        head.next = rest[0]
        return (head, rest[1], None)
    elif i == m:
        rest = reverse(head.next, m, n, i + 1)
        rest[1].next = head
        head.next = rest[2]
        return (rest[0], head, None)
    elif i < n:
        rest = reverse(head.next, m, n, i + 1)
        rest[1].next = head
        return (rest[0], head, rest[2])
    elif i == n:
        return (head, head, head.next)

def main():
    lst = LinkedList([1, 2, 3, 4, 5])
    print reverseBetween(lst.head, 2, 3)

main()
