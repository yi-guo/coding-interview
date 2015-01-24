#!/usr/bin/python

# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
#   Only one letter can be changed at a time
#   Each intermediate word must exist in the dictionary

# For example,

# Given:
# start = "hit"
# end = "cog"
# dict = ["hot", "dot", "dog", "lot", "log"]
# return
# [["hit", "hot", "dot", "dog", "cog"],
#  ["hit", "hot", "lot", "log", "cog"]]

# Note:
#   1. All words have the same length.
#   2. All words contain only lowercase alphabetic characters.

import collections

# Same approach as "Word Ladder" except using SET to speed up and DICT to store parent state(s).
def findLadders(start, end, dict):
    dict.add(end)
    paths, currLevel = {}, {start}
    while currLevel and end not in paths:
        nextLevel = set()
        visited = collections.defaultdict(set)
        for word in currLevel:
            for i in range(len(word)):
                temp = list(word)
                for j in map(chr, range(97, 123)):
                    temp[i] = j
                    next = ''.join(temp)
                    if next in dict and next not in paths:
                        nextLevel.add(next)
                        visited[next].add(word)
        paths.update(visited)
        currLevel = nextLevel
    return getPaths(start, end, paths) if end in paths else list()

def getPaths(start, end, paths):
    ret = [[end]]
    while ret[0][0] != start:
        length = len(ret)
        for i in range(length):
            path = ret[i]
            for prev in paths[path[0]]:
                ret.append([prev] + path)
        ret = ret[length:]
    return ret

def main():
    dict = set(["hot", "dot", "dog", "lot", "log"])
    print findLadders('hit', 'cog', dict)

main()
