#!/usr/bin/python

# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

# Breath-first search to traverse the graph and use a hashmap to map a node to its copy.
def cloneGraph(node):
    if not node: return None
    queue = [node]
    clone = UndirectedGraphNode(node.label)
    hashmap = {node : clone}
    while queue:
        curr = queue.pop(0)
        temp = hashmap[curr]
        for neighbor in curr.neighbors:
            if neighbor not in hashmap:
                hashmap[neighbor] = UndirectedGraphNode(neighbor.label)
                queue.append(neighbor)
            temp.neighbors.append(hashmap[neighbor])
    return clone