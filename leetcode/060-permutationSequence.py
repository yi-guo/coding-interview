#!/usr/bin/python

# The set [1, 2, 3, ... , n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence (i.e., for n = 3):
#   "123"
#   "132"
#   "213"
#   "231"
#   "312"
#   "321"

# Given n and k, return the kth permutation sequence.

# Note: n will be between 1 and 9 inclusive.

# Catch the pattern for every digit. O(n).
def getPermutation(n, k):
    # A list of factorials [n!, (n-1)!, ... , 2!, 1!]
    factorial = range(n, 0, -1)
    for i in range(n - 3, -1, -1):
        factorial[i] = factorial[i] * factorial[i + 1]
    # A list to store the result digit by digit
    permutation = list()
    # A list of digits from which the result retrieves
    numbers = [str(i) for i in range(1, n + 1)]
    # Compute the kth permutation digit by digit starting from the most significant bit.
    for i in range(n - 1):
        permutation.append(numbers.pop(((k - 1) % factorial[i]) / factorial[i + 1]))
    permutation.append(numbers.pop())
    return ''.join(permutation)

def main():
    print getPermutation(int(sys.argv[1]), int(sys.argv[2]))

main()
