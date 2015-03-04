#!/usr/bin/python

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

from leetcode.python import Tree

# Level order traversal with depth incremented upon each level.
# Return depth immediately when a leaf node occurs.
def minDepth(root):
    if not root: return 0
    depth, queue = 1, [root]
    while queue:
        length = len(queue)
        for i in range(length):
            # Leaf node, return depth immediately.
            if not queue[i].left and not queue[i].right:
                return depth
            # Otherwise, keep searching.
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)
        depth = depth + 1
        queue = queue[length:]
    return depth

def main():
    tree = Tree([1, 2, 3, 4, '#', '#', 5])
    print minDepth(tree.root)

main()
