#!/usr/bin/python

# Given a collection of candidate numbers C and a target number T, find all unique combinations in C
# where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
#   All numbers (including target) will be positive integers.
#   Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (i.e., a1 <= a2 <= ... <= ak).
#   The solution set must not contain duplicate combinations.

# For example, given candidate set 10, 1, 2, 7, 6, 1, 5 and target 8, a solution set is:
#   [1, 7]
#   [1, 2, 5]
#   [2, 6]
#   [1, 1, 6]

def combinationSum2(candidates, target):
    candidates.sort()
    queue, indices = [[]], [-1]
    combinations, combinationsum = [], [0]
    while queue:
        size = len(queue)
        for i in xrange(size):
            for j in xrange(indices[i] + 1, len(candidates)):
                if j != indices[i] + 1 and candidates[j] == candidates[j - 1]:
                    continue
                sum = combinationsum[i] + candidates[j]
                if sum < target:
                    indices.append(j)
                    combinationsum.append(sum)
                    queue.append(queue[i] + [candidates[j]])
                elif sum == target:
                    combinations.append(queue[i] + [candidates[j]])
                else:
                    break
        queue = queue[size:]
        indices = indices[size:]
        combinationsum = combinationsum[size:]
    return combinations

def main():
    print combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print combinationSum2([8, 7, 4, 3], 11)
    print combinationSum2([2, 5, 2, 1, 2], 5)

main()
