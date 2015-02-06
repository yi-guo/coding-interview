#!/usr/bin/python

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.

# Define ListNode for doubly linked list
class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        ret, temp = '[%d' % self.val, self.next
        while temp:
            ret += ', %d' % temp.val
            temp = temp.next
        return ret + ']'

# Define LRUCache
class LRUCache:

    # Doubly linked list and hash table.
    def __init__(self, capacity):
        self.size = 0
        self.head = None
        self.tail = None
        self.cache = dict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            if node == self.tail:
                return node.val
            node.next.prev = node.prev
            if node == self.head:
                self.head = self.head.next
            else:
                node.prev.next = node.next
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            return node.val
        return -1

    def set(self, key, value):
        if self.get(key) == -1:
            if self.size < self.capacity:
                node = ListNode(key, value)
                if self.size != 0:
                    self.tail.next = node
                    node.prev = self.tail
                else:
                    self.head = node
                self.tail = node
                self.cache[key] = node
                self.size = self.size + 1
            else:
                head = self.head
                del self.cache[head.key]
                if self.head.next:
                    self.head = head.next
                    self.head.prev = None
                head.key = key
                head.val = value
                self.cache[key] = head
                self.tail.next = head
                head.prev = self.tail
                head.next = None
                self.tail = head
        else:
            self.cache[key].val = value

def main():
    cache = LRUCache(2)
    cache.set(2, 1)
    cache.set(3, 2)
    print cache.get(3)
    print cache.get(2)
    cache.set(4, 3)
    print cache.get(2)

main()
