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
    # Filter any candidate that is already greater or equal to (which is a solution) the target.
    temp = list()
    S, Q = [], [([], 0)]
    for c in candidates:
        if c < target:
            temp.append(c)
        elif c == target:
            S.append([c])
    # Sort the candidates to efficiently avoid duplicates.
    candidates = sorted(temp)
    # Start BFS
    while Q:
        head = Q.pop(0)
        for c in candidates:
            # No need to try candidate that is smaller than the largest in a possible solution.
            if not head[0] or head[0][len(head[0]) - 1] <= c:
                sum = head[1] + c
                if sum < target:
                    Q.append((head[0] + [c], sum))
                elif sum == target:
                    head[0].append(c)
                    S.append(head[0])
                    break
                else:
                    break
    return S

def main():
    print combinationSum([2, 3, 6, 7], 7)

main()
