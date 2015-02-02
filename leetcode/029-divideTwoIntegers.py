#!/usr/bin/python

# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.

import sys

# Bit operation.
def divide(dividend, divisor):
    if divisor == 0: return None
    # Determine positive or negative.
    neg = -1 if dividend < 0 else 1
    neg = -neg if divisor < 0 else neg
    res, temp = 0, abs(divisor)
    divisor, dividend = abs(divisor), abs(dividend)
    while divisor <= dividend:
        quotient = 1
        while divisor <= dividend:
            divisor = divisor << 1
            quotient = quotient << 1
        dividend = dividend - (divisor >> 1)
        res = res + (quotient >> 1)
        divisor = temp
    return max(min(res * neg, 2147483647), -2147483648)

def main():
    print divide(int(sys.argv[1]), int(sys.argv[2]))

main()
