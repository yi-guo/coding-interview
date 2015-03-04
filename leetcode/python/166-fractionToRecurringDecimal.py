#!/usr/bin/python

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".

def fractionToDecimal(numerator, denominator):
    if denominator == 0:
        return None
    neg = '-' if numerator * denominator < 0 else ''
    i, decimal, remainders = 1, list(), dict()
    numerator, denominator = abs(numerator), abs(denominator)
    while True:
        quotient = numerator / denominator
        remainder = numerator % denominator
        decimal.append(str(quotient))
        if remainder != 0:
            if remainder in remainders:
                start = remainders[remainder]
                return '%s%s.%s(%s)' % (neg, decimal[0], ''.join(decimal[1:start]), ''.join(decimal[start:]))
            remainders[remainder] = i
        else:
            return neg + decimal[0] if len(decimal) == 1 else '%s%s.%s' % (neg, decimal[0], ''.join(decimal[1:]))
        i = i + 1
        numerator = remainder * 10

def main():
    print fractionToDecimal(-0, -7)

main()
