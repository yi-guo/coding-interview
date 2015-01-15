#!/usr/bin/python

# Given a set of distinct integers, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

# For example, if S = [1, 2, 3], a solution is:
# [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]

# BFS.
def subsets(S):
    # If S is empty, then nothing.
    if not S:
        return [S]
    # If S has one element, then return empty set and the element itself.
    elif len(S) == 1:
        return [[], S]
    # Sort to eliminate duplicates.
    S.sort()
    # Keep expanding current subsets until S itself is added.
    i, subsets = 0, [[]]
    while i < len(subsets):
        curr = subsets[i]
        # If empty set as a subset, make new sets by having every number in S as a set.
        if not curr:
            subsets.extend([[n] for n in S])
        # Otherwise, for current subset, make new sets by adding a number in S that is not in current subset.
        else:
            j = S.index(curr[-1]) + 1
            for n in S[j:]:
                subsets.append(curr + [n])
        i = i + 1
    return subsets

def main():
    print subsets([2, 7, 3, 5])

main()
