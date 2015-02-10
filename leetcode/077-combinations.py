#!/usr/bin/python

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example, if n = 4 and k = 2, a solution is:
# [[2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4]]

from collections import deque

# BFS.
def combine(n, k):
    if n < k or k == 0:
        return list()
    combinations = deque()
    combinations.append([])
    while len(combinations[0]) < k:
        curr = combinations.popleft()
        start = 1 if not curr else curr[-1] + 1
        for i in xrange(start, n + 1):
            combinations.append(curr + [i])
    return list(combinations)

def main():
    print combine(4, 2)

main()
