#!/usr/bin/python

# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Easy question. No need to explain.
def plusOne(digits):
    carry = 0
    digits[len(digits) - 1] += 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] = digits[i] + carry
        if digits[i] < 10:
            return digits
        digits[i] = digits[i] - 10
        carry = 1
    return [1] + digits

def main():
    digits = [9, 9, 9]
    print plusOne(digits)

main()
