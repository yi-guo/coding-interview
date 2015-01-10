from cStringIO import StringIO

# Define Node
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Define LinkedList
class LinkedList:
    def __init__(self, head=None):
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
        while temp:
            output.write(str(temp.val))
            if temp.next:
                output.write(', ')
            temp = temp.next
        output.write(']')
        return output.getvalue()

# Return list as a formatted string given head
def toString(head):
    temp = head
    output = StringIO()
    output.write('[')
    while temp:
        output.write(str(temp.val))
        if temp.next:
            output.write(', ')
        temp = temp.next
    output.write(']')
    return output.getvalue()