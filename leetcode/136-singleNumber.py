#!/usr/bin/python

# Given an array of integers, every element appears twice except for one. Find that single one.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Bit manipulation. One pass, thus O(n).
# A XOR A = 0
# A XOR B XOR A = B
def singleNumber(A):
    num = A[0]
    for i in range(1, len(A)):
        num = num ^ A[i]
    return num

def main():
    print singleNumber([2, 3, 4, 3, 5, 1, 5, 4, 1])

main()
