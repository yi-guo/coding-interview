#!/usr/bin/python

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example, [1, 1, 2] has the following unique permutations:
# [1, 1, 2], [1, 2, 1], and [2, 1, 1].

# For every number in num, insert it to current permutations at all possible positions.
# Sort the array first and use hash set to eliminate duplicates.
def permuteUnique(num):
    if not num:
        return num
    elif len(num) < 2:
        return [num]
    num.sort()
    existed = set()
    permutations = [[]]
    for i in range(len(num)):
        j, length = 0, len(permutations)
        while j < length:
            permutation = permutations.pop(0)
            for k in range(len(permutation) + 1):
                if k != 0 and permutation[k - 1] == num[i]:
                    continue
                new = list(permutation)
                new.insert(k, num[i])
                permu = tuple(new)
                if permu not in existed:
                    existed.add(permu)
                    permutations.append(new)
            j = j + 1
    return permutations

def main():
    print permuteUnique([1, 1, 2, 2])

main()
