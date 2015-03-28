#!/usr/bin/python

# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

from Tree import TreeNode

# In-order traversal and trace the violation of the increasing order.
class Solution:

    def __init__(self):
        self.prev = TreeNode(-999)
        self.first = self.second = None

    def recoverTree(self, root):
        self.inorderTraversal(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            if not self.first and self.prev.val >= root.val:
                self.first = self.prev
            if self.first and self.prev.val >= root.val:
                self.second = root
            self.prev = root
            self.inorderTraversal(root.right)
