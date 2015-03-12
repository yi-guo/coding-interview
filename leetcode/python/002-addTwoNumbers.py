#!/usr/bin/python

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

from LinkedList import ListNode

# Method 1: Terminate after one traversal. O(n).
def addTwoNumbers1(l1, l2, flag=0):
    if l1 and l2:
        l = ListNode(l1.val + l2.val + flag)
        if l.val > 9:
            l.val -= 10
            l.next = addTwoNumbers1(l1.next, l2.next, 1)
        else:
            l.next = addTwoNumbers1(l1.next, l2.next, 0)
        return l
    elif l1 and not l2:
        l = ListNode(l1.val + flag)
        if l.val > 9:
            l.val -= 10
            l.next = addTwoNumbers1(l1.next, l2, 1)
        else:
            l.next = addTwoNumbers1(l1.next, l2, 0)
        return l
    elif not l1 and l2:
        l = ListNode(l2.val + flag)
        if l.val > 9:
            l.val -= 10
            l.next = addTwoNumbers1(l1, l2.next, 1)
        else:
            l.next = addTwoNumbers1(l1, l2.next, 0)
        return l
    else:
        return ListNode(flag) if flag else None

# Method 2: Iterative one pass.
def addTwoNumbers2(l1, l2):
    head = ListNode(0)
    carry, temp = 0, head
    while l1 or l2 or carry:
        if l1:
            temp.val += l1.val
            l1 = l1.next
        if l2:
            temp.val += l2.val
            l2 = l2.next
        carry = temp.val / 10
        temp.val %= 10
        if l1 or l2 or carry:
            temp.next = ListNode(carry)
            temp = temp.next
    return head

def main():
    l1 = LinkedList([9, 9])
    l2 = LinkedList([1])
    print addTwoNumbers1(l1.head, l2.head)
    print addTwoNumbers2(l1.head, l2.head)

main()
