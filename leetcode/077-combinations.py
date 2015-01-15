#!/usr/bin/python

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example, if n = 4 and k = 2, a solution is:
# [[2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4]]

# BFS.
def combine(n, k):
    # If either n or k is 0 or smaller, or n < k, then nothing.
    if n < 1 or k < 1 or n < k:
        return [[]]
    # If k is 1, then [[1], [2], ... , [n]]
    elif k == 1:
        return [[i] for i in range(1, n + 1)]
    # If n = k, then [[1, 2, ... , n]]
    elif n == k:
        return [range(1, n + 1)]
    # Otherwise, do BFS until all combinations have the length of k.
    combinations = [[]]
    while len(combinations[0]) < k:
        curr = combinations.pop(0)
        i = 0 if not curr else curr[len(curr) - 1]
        while i < n:
            combinations.append(curr + [i + 1])
            i = i + 1
    return combinations

def main():
    print combine(4, 2)

main()
