#/usr/bin/python

# Merge k sorted linked lists and return it as one sorted list.

# Analyze and describe its complexity.

from LinkedList import *

def mergeKLists(lists):
    if not lists:
        return None
    elif len(lists) == 1:
        return lists[0]
    elif len(lists) == 2:
        l1, l2 = lists[0], lists[1]
        if not l1:
            return l2
        elif not l2:
            return l1
        head = None
        if l1.val < l2.val:
            head = Node(l1.val)
            l1 = l1.next
        else:
            head = Node(l2.val)
            l2 = l2.next
        temp = head
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = Node(l1.val)
                l1 = l1.next
            else:
                temp.next = Node(l2.val)
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        return head
    else:
        q = len(lists) / 2
        return mergeKLists([mergeKLists(lists[:q]), mergeKLists(lists[q:])])

def main():
    print display(mergeKLists([LinkedList([2,3,4]).head, LinkedList([4,5,6]).head, LinkedList([7,8,9,10]).head, LinkedList([11,12]).head, LinkedList([13,14,15,16,17]).head]))

main()
