#!/usr/bin/python

# Given a collection of integers that might contain duplicates, S, return all possible subsets.

# Note:
#   1. Elements in a subset must be in non-descending order.
#   2. The solution set must not contain duplicate subsets.

# For example, if S = [1,2,2], a solution is:
#   [[2], [1], [1, 2, 2], [2, 2], [1, 2], []]

# BFS as in "Subsets" with non-distinct number only appended once.
def subsetsWithDup(S):
    S.sort()
    i, indices, subsets = 0, [0], [[]]
    while i < len(subsets):
        subset = subsets[i]
        for j in range(indices[i], len(S)):
            if j == indices[i] or S[j] != S[j - 1]:
                indices.append(j + 1)
                subsets.append(subset + [S[j]])
        i = i + 1
    return subsets

def main():
    print subsetsWithDup([1, 1, 2, 3])

main()
