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

def findLadders(start, end, dict):
    if start == end: return [[start]]
    flag = False
    paths, queue, visited = [], [[start]], set([start])
    while queue:
        length = len(queue)
        print length, queue
        for i in range(length):
            if queue[i][-1] == end:
                flag = True
                paths.append(queue[i])
            for j in range(len(queue[i][-1])):
                word = list(queue[i][-1])
                for k in map(chr, range(97, 123)):
                    print j, word
                    word[j] = k
                    next = ''.join(word)
                    if next in dict or next == end:
                        queue.append(queue[i] + [next])
        if flag: return paths
        queue = queue[length:]
    return paths


def main():
    dict = ["hot", "dog"]
    print findLadders('hot', 'dog', dict)

main()
