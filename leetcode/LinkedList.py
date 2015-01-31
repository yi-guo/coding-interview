#!/usr/bin/python


# Define Node
class ListNode:

    # To declare a linked list node, issue N = Node(1).
    def __init__(self, val):
        self.val = val
        self.next = None

    # Define the string representation of a linked list with this node as head.
    def __repr__(self):
        ret, temp = '[%d' % self.val, self.next
        while temp:
            ret += ', %d' % temp.val
            temp = temp.next
        return ret + ']'


# Define LinkedList
class LinkedList:

    # Three ways to declare a linked list:
    #   1. L = LinkedList(1), which creates a linked list with head of 1.
    #   2. L = LinkedList([1, 2, 3, 4, 5]), which creates a linked list 1 -> 2 -> 3 -> 4 -> 5.
    #   3. L = LinkedList(), which creates an empty linked list.
    def __init__(self, head=None):
        if type(head) == int:
            self.head = ListNode(head)
        elif type(head) == list:
            self.head = None
            for val in head:
                self.insert(val)
        else:
            self.head = None

    # Define the string representation of a linked list.
    def __repr__(self):
        return str(self.head)

    def insert(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = ListNode(val)