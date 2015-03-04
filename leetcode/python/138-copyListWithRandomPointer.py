#!/usr/bin/python

# A linked list is given such that each node contains an additional random pointer which could point to any node
# in the list or null.

# Return a deep copy of the list.

# Hashmap. One pass, thus O(n).
def copyRandomList(head):
    if not head: return None
    temp, clone = head, RandomListNode(head.label)
    hashmap = {head : clone}
    while temp:
        if temp.next:
            if temp.next in hashmap:
                clone.next = hashmap[temp.next]
            else:
                clone.next = RandomListNode(temp.next.label)
                hashmap[temp.next] = clone.next
        if temp.random:
            if temp.random in hashmap:
                clone.random = hashmap[temp.random]
            else:
                clone.random = RandomListNode(temp.random.label)
                hashmap[temp.random] = clone.random
        temp = temp.next
        clone = clone.next
    return hashmap[head]
