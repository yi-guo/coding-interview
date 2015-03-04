#/usr/bin/python

# Merge k sorted linked lists and return it as one sorted list.

# Analyze and describe its complexity.


import heapq

from leetcode.python.LinkedList import ListNode
from leetcode.python import LinkedList



# Divide and conquer. T(n) = 2T(n/2) + O(m), thus O(mn).
def mergeKLists1(lists):
    if not lists:
        return None
    elif len(lists) == 1:
        return lists[0]
    elif len(lists) == 2:
        head = temp = ListNode(0)
        l1, l2 = lists[0], lists[1]
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return head.next
    else:
        length = len(lists) / 2
        return mergeKLists1([mergeKLists1(lists[:length]), mergeKLists1(lists[length:])])


# Priority queue.
def mergeKLists2(lists):
    head = temp = ListNode(0)
    lists = [(node.val, node) for node in lists if node]
    heapq.heapify(lists)
    while lists:
        temp.next = heapq.heappop(lists)[1]
        temp = temp.next
        if temp.next:
            heapq.heappush(lists, (temp.next.val, temp.next))
    return head.next


def main():
    print mergeKLists2([LinkedList([1, 2, 2]).head, LinkedList([1, 1, 2]).head])


main()
