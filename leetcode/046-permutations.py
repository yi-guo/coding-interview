#!/usr/bin/python

# Given a collection of numbers, return all possible permutations.

# For example, [1, 2, 3] has the following permutations:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

# For every number in num, insert it to current permutations at all possible positions.
def permute(num):
    if not num:
        return num
    elif len(num) == 1:
        return [num]
    elif len(num) == 2:
        return [[num[0], num[1]], [num[1], num[0]]]
    permutations = [[]]
    for n in num:
        i, length = 0, len(permutations)
        while i < length:
            permutation = permutations.pop(0)
            for j in range(len(permutation) + 1):
                new = list(permutation)
                new.insert(j, n)
                permutations.append(new)
            i = i + 1
    return permutations

def main():
    print permute([1, 2])

main()
