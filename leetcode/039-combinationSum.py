#!/usr/bin/python

# Given a set of candidate numbers C and a target number T, find all unique combinations in C
# where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
#   All numbers (including target) will be positive integers.
#   Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (i.e., a1 <= a2 <= ... <= ak).
#   The solution set must not contain duplicate combinations.

# For example, given candidate set [2, 3, 6, 7] and target 7, a solution set is: 
#   [7]
#   [2, 2, 3]

# A simple BFS solution.
def combinationSum(candidates, target):
    candidates.sort()
    queue, indices = [[]], [0]
    combinations, combinationsum = [], [0]
    while queue:
        size = len(queue)
        for i in xrange(size):
            for j in xrange(indices[i], len(candidates)):
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
    print combinationSum([2, 3, 6, 7], 7)

main()
