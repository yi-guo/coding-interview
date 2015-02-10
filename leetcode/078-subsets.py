#!/usr/bin/python

# Given a set of distinct integers, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

# For example, if S = [1, 2, 3], a solution is:
# [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]

# BFS.
def subsets(S):
    S.sort()
    i, subset, indices = 1, [[]], dict()
    for j, n in enumerate(S):
        indices[n] = j
        subset.append([n])
    while len(subset[-1]) < len(S):
        curr = subset[i]
        start = indices[curr[-1]] + 1
        for j in xrange(start, len(S)):
            subset.append(curr + [S[j]])
        i = i + 1
    return subset

def main():
    print subsets([2, 7, 3, 5])

main()
