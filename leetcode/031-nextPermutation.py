#!/usr/bin/python

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in 
# ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and their corresponding outputs are in the right-hand column.
# 1, 2, 3 -> 1, 3, 2
# 3, 2, 1 -> 1, 2, 3
# 1, 1, 5 -> 1, 5, 1

# The algorithm goes as follows.
#   1. Find the largest index i such that A[i - 1] < A[i].
#   2. Find the largest index j >= i such that A[j] > A[i - 1].
#   3. Swap A[i - 1] and A[j].
#   4. Reverse A starting at index i.
def nextPermutation(num):
    if not num or len(num) < 2:
        return num
    elif len(num) == 2:
        num[0], num[1] = num[1], num[0]
        return num
    i = len(num) - 1
    while i > 0:
        if num[i - 1] < num[i]:
            break 
        i = i - 1
    if i == 0:
        return sorted(num)
    j = len(num) - 1
    while j > i - 1:
        if num[j] > num[i - 1]:
            break
        j = j - 1
    num[i - 1], num[j] = num[j], num[i - 1]
    j = len(num) - 1
    while i < j:
        num[i], num[j] = num[j], num[i]
        i = i + 1
        j = j - 1
    return num

def main():
    print nextPermutation([1, 2, 3])

main()
