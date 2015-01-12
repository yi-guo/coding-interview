#!/usr/bin/python

# Given two numbers represented as strings, return multiplication of the numbers as a string.

# Note: The numbers can be arbitrarily large and are non-negative.

# Digit by digit multiplication.
def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    elif num1 == '1':
        return num2
    elif num2 == '1':
        return num1
    product = [0] * (len(num1) + len(num2))
    for i, n2 in enumerate(num2):
        for j, n1 in enumerate(num1):
            product[i + j + 1] += int(n1) * int(n2)
    carry = 0
    for i in range(len(product) - 1, -1, -1):
        product[i] += carry
        num = str(product[i])
        if len(num) > 1:
            carry = int(num[:len(num) - 1])
            product[i] = int(num[len(num) - 1])
        else:
            carry = 0
    if product[0] == 0:
        return ''.join(str(n) for n in product[1:])
    else:
        return ''.join(str(n) for n in product)

def main():
    print multiply('999', '999')

main()
