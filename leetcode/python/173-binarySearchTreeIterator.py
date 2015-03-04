#!/usr/bin/python

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

from leetcode.python import Tree

# Iterative in-order traversal.
class BSTIterator:

    def __init__(self, root):
        self.stack = list()
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) != 0

    def next(self):
        next = self.stack.pop()
        if next.right:
            temp = next.right
            while temp:
                self.stack.append(temp)
                temp = temp.left
        return next.val

def main():
    tree = Tree([9, 6, 12, 2, 7, 10, 14, 1, 4, '#', 8, '#', 11, 13, 15, '#', '#', 3, 5])
    iter = BSTIterator(tree.root)
    while iter.hasNext():
        print iter.next()

main()
