#!/usr/bin/python

# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

# Count the number of five in n!.
def trailingZeroes(n):
    num, powerOfFive = 0, 5
    while powerOfFive <= n:
        num += n / powerOfFive
        powerOfFive *= 5
    return num

def main():
    for i in xrange(101):
        print trailingZeroes(i)

main()