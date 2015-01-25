#!/usr/bin/python

# Given an array of integers, every element appears three times except for one. Find that single one.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Represent the number with a 32-bit binary.
# Count 1's for every bit and see if it apprears three times.
def singleNumber(A):
    num = 0
    neg = -1 if sum(n < 0 for n in A) % 3 else 1
    for i in range(32):
        n, count = 1 << i, 0
        for j in range(len(A)):
            if abs(A[j]) & n:
                count += 1
        if count % 3 == 1:
            num = n | num
    return neg * num

def main():
    print singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])

main()
