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

from collections import deque

# Breath-first search all posible states until target is found.
def ladderLength(start, end, dict):
    dict.add(end)
    queue = deque()
    queue.append(start)
    length, visited = 1, {start}
    while queue:
        size = len(queue)
        for i in xrange(size):
            word = queue.popleft()
            if word == end:
                return length
            for j in xrange(len(word)):
                for k in xrange(97, 123):
                    newWord = word[:j] + chr(k) + word[j + 1:]
                    if newWord in dict and newWord not in visited:
                        visited.add(newWord)
                        queue.append(newWord)
        length += 1
    return 0

def main():
    dict = set(['hot', 'dot', 'dog', 'lot', 'log'])
    print ladderLength('hit', 'cog', dict)

main()
