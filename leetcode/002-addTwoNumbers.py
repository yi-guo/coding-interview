#!/usr/bin/python

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

from cStringIO import StringIO

# Define Node
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# Define LinkedList
class LinkedList:
    def __init__(self, head = None):
        if type(head) == int:
            self.head = Node(head)
        elif type(head) == list:
            self.head = None
            for val in head:
                self.insert(val)
        else:
            self.head = None

    def insert(self, val):
        if self.isEmpty():
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(val)

    def isEmpty(self):
        return self.head is None

    def toString(self):
        temp = self.head
        output = StringIO()
        output.write('[')
        while temp is not None:
            output.write(str(temp.val))
            if temp.next is not None:
                output.write(', ')
            temp = temp.next
        output.write(']')
        return output.getvalue()

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

# Display list given head
def toString(head):
    temp = head
    output = StringIO()
    while temp:
        output.write(str(temp.val))
        if temp.next is not None:
            output.write(' -> ')
        temp = temp.next
    return output.getvalue()

def main():
    l1 = LinkedList([9, 9])
    l2 = LinkedList([1])
    print toString(addTwoNumbers1(l1.head, l2.head, 0))
    print toString(addTwoNumbers2(l1.head, l2.head))

main()
