#/usr/bin/python

# Merge k sorted linked lists and return it as one sorted list.

# Analyze and describe its complexity.

from LinkedList import LinkedList

# Divide and conquer. T(n) = 2T(n/2) + O(m), thus O(mn).
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
        head = min(l1, l2, key=lambda n : n.val)
        while l1 and l2:
            if l1.val <= l2.val:
                while l1.next and l1.next.val <= l2.val:
                    l1 = l1.next
                temp = l1.next
                l1.next = l2
                l1 = temp
            else:
                while l2.next and l2.next.val <= l1.val:
                    l2 = l2.next
                temp = l2.next
                l2.next = l1
                l2 = temp
        return head
    else:
        q = len(lists) / 2
        return mergeKLists([mergeKLists(lists[:q]), mergeKLists(lists[q:])])

def main():
    print mergeKLists([LinkedList([1, 2, 2]).head, LinkedList([1, 1, 2]).head])

main()
