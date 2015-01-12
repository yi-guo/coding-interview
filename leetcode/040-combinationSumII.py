#!/usr/bin/python

# Given a collection of candidate numbers C and a target number T, find all unique combinations in C
# where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
#   All numbers (including target) will be positive integers.
#   Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (i.e., a1 <= a2 <= ... <= ak).
#   The solution set must not contain duplicate combinations.

# For example, given candidate set 10,1,2,7,6,1,5 and target 8, a solution set is: 
#   [1, 7]
#   [1, 2, 5]
#   [2, 6]
#   [1, 1, 6]

def combinationSum2(candidates, target):
    candidates = sorted(filter(lambda c : c <= target, candidates))
    S, Q = [], [([], 0)]
    while Q:
        head = Q.pop(0)
        for i, c in enumerate(candidates):
            if not head[0]:
                if i > 0 and c == candidates[i - 1]:
                    continue
            else:
                if head[0][len(head[0]) - 1] >= i:
                    continue
                elif i > 0 and c == candidates[i - 1]:
                    if i - 1 > head[0][len(head[0]) - 1]:
                        continue
            sum = head[1] + c
            if sum < target:
                Q.append((head[0] + [i], sum))
            elif sum == target:
                head[0].append(i)
                S.append([candidates[head[0][i]] for i in range(len(head[0]))])
                break
            else:
                break
    return S

def main():
    print combinationSum2([10,1,2,7,6,1,5], 8)
    print combinationSum2([8,7,4,3],11)
    print combinationSum2([2,5,2,1,2], 5)

main()
