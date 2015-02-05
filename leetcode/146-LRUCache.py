#!/usr/bin/python

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.

# Define ListNode for doubly linked list
class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# Define LRUCache
class LRUCache:

    def __init__(self, capacity):
        self.size = 0
        self.head = None
        self.tail = None
        self.cache = dict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            return node.val
        return -1

    def set(self, key, value):
        if self.get(key) == -1:
            if self.size < self.capacity:
                node = ListNode(value)
                if self.size != 0:
                    self.tail.next = node
                    node.prev = self.tail
                else:
                    self.head = node
                self.tail = node
                self.cache[key] = node
                self.size = self.size + 1
            else:


        else:
            self.cache[key].val = value

