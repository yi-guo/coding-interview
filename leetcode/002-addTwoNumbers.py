#!/usr/bin/python

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

from LinkedList import Node, LinkedList, toString

# Method 1: Terminate after one traversal; O(n)
def addTwoNumbers1(l1, l2, flag):
    if l1 and l2:
        l = Node(l1.val + l2.val + flag)
        if l.val > 9:
            l.val = l.val - 10
            l.next = addTwoNumbers1(l1.next, l2.next, 1)
        else:
            l.next = addTwoNumbers1(l1.next, l2.next, 0)
        return l
    elif l1 and not l2:
        l = Node(l1.val + flag)
        if l.val > 9:
            l.val = l.val - 10
            l.next = addTwoNumbers1(l1.next, l2, 1)
        else:
            l.next = addTwoNumbers1(l1.next, l2, 0)
        return l
    elif not l1 and l2:
        l = Node(l2.val + flag)
        if l.val > 9:
            l.val = l.val - 10
            l.next = addTwoNumbers1(l1, l2.next, 1)
        else:
            l.next = addTwoNumbers1(l1, l2.next, 0)
        return l
    else:
        if flag:
            return Node(flag)
        else:
            return None

# Method 2: Post-processing after one traversal; O(2n)
def addTwoNumbers2(l1, l2):
    l, flag = add(l1, l2), 0
    temp = l
    while temp:
        temp.val = temp.val + flag
        if temp.val > 9:
            temp.val = temp.val - 10
            flag = 1
        else:
            flag = 0
        if not temp.next and flag:
            temp.next = Node(flag)
            break
        temp = temp.next
    return l

def add(l1, l2):
    if l1 and l2:
        l = Node(l1.val + l2.val)
        l.next = add(l1.next, l2.next)
        return l
    elif l1 and not l2:
        return l1
    elif not l1 and l2:
        return l2
    else:
        return None

# Method 3: Iterative one pass.
def addTwoNumbers(l1, l2):
    head = Node(0)
    carry, temp = 0, head
    while l1 or l2 or carry:
        if l1:
            temp.val += l1.val
            l1 = l1.next
        if l2:
            temp.val += l2.val
            l2 = l2.next
        carry = temp.val / 10
        temp.val = temp.val % 10
        if l1 or l2 or carry:
            temp.next = Node(carry)
            temp = temp.next
    return head

def main():
    l1 = LinkedList([9, 9])
    l2 = LinkedList([1])
    print toString(addTwoNumbers1(l1.head, l2.head, 0))
    print toString(addTwoNumbers2(l1.head, l2.head))

main()
