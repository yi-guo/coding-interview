#!/usr/bin/python

# Given a collection of numbers, return all possible permutations.

# For example, [1, 2, 3] has the following permutations:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

# For every number in num, insert it to current permutations at all possible positions.
def permute(num):
    if not num: return list()
    permutations = [[]]
    for n in num:
        size = len(permutations)
        for i in xrange(size):
            curr = permutations[i]
            permutations.append(curr + [n])
            for j in xrange(len(curr)):
                permutations.append(curr[:j] + [n] + curr[j:])
        permutations = permutations[size:]
    return permutations

def main():
    print permute([1, 2, 3])

main()
