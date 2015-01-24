#!/usr/bin/python

# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence
# from start to end, such that:

# Only one letter can be changed at a time. Each intermediate word must exist in the dictionary.

# For example,

# Given:
# start = "hit"
# end = "cog"
# dict = ["hot", "dot", "dog", "lot", "log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
#   1. Return 0 if there is no such transformation sequence.
#   2. All words have the same length.
#   3. All words contain only lowercase alphabetic characters.

# Breath-first search all posible states until target is found.
def ladderLength(start, end, dict):
    if start == end: return 1
    steps, queue, visited = 1, [start], set([start])
    while queue:
        steps = steps + 1
        length = len(queue)
        for i in range(length):
            for j in range(len(queue[i])):
                word = list(queue[i])
                for k in map(chr, range(97, 123)):
                    word[j] = k
                    next = ''.join(word)
                    if next == end:
                        return steps
                    if next in dict and next not in visited:
                        queue.append(next)
                        visited.add(next)
        queue = queue[length:]
    return 0

def main():
    dict = ["hot", "dot", "dog", "lot", "log"]
    print ladderLength('hit', 'cog', dict)

main()
