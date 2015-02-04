#!/usr/bin/python

# Define TreeNode
class TreeNode:

    # Two ways to declare a tree node:
    #   1. N = TreeNode(1)
    #   2. N = TreeNode(1, 2, 3), which is equivalent to N = Node(left=2, right=3, val=1)
    # In other words, if only want root and right, issue N = Node(1, right=3).
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = TreeNode(left) if left else left
        self.right = TreeNode(right) if right else right

    # Define the string representation of a tree rooted at this node.
    # Reference: http://stevekrenzel.com/articles/printing-trees
    # Thank Steve Krenzel for coming up with this amazingly clear representation.
    def __repr__(self, depth=0):
        ret = str()
        if self.right:
            ret += self.right.__repr__(depth + 1)
        ret += ' ' * 4 * depth + str(self.val) + '\n'
        if self.left:
            ret += self.left.__repr__(depth + 1)
        return ret if depth else ret.rstrip()

# Define Tree
class Tree:

    # Three ways to declare a tree:
    #   1. T = Tree(1), which creates a tree with root of 1.
    #   2. T = Tree([1, 2, 3, '#', 5]), confused? Check out LeetCode OJ's binary tree serialization.
    #   3. T = Tree(), which creates an empty tree.
    def __init__(self, root=None):
        if type(root) == int:
            self.root = TreeNode(root)
        elif type(root) == list:
            if not root or root[0] == '#':
                self.root = None
                return
            # Check if the given list is consistent.
            for i in range(1, len(root)):
                if root[i] == '#':
                    if (i * 2 + 1 < len(root) and root[i * 2 + 1] != '#') or \
                       (i * 2 + 2 < len(root) and root[i * 2 + 1] != '#'):
                        self.root = None
                        print 'Inconsistent List'
                        return
            # Level-order tree construction.
            self.root = TreeNode(root.pop(0))
            temp, queue = self.root, list()
            while temp:
                # If list has more than 1 element, then construct left and right child.
                if len(root) > 1:
                    left, right = root[0], root[1]
                    if left != '#':
                        temp.left = TreeNode(left)
                        queue.append(temp.left)
                    if right != '#':
                        temp.right = TreeNode(right)
                        queue.append(temp.right)
                    root = root[2:]
                # If list has only one element, then add left child and exit.
                elif len(root) == 1:
                    left = root[0]
                    if left != '#':
                        temp.left = TreeNode(left)
                    break
                # If empty, then exit directly.
                else:
                    break
                temp = queue.pop(0)
        else:
            self.root = None

    # Define the string representation of a tree.
    def __repr__(self):
        return str(self.root)