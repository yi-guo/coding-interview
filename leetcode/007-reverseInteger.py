#!usr/bin/python

# Reverse digits of an integer.

# Example: x = 123, return 321
# Example: x = -123, return -321

# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# Convert the integer into a list of digits and reverse
def reverse(x):
    neg = -1 if x < 0 else 1
    x, num = abs(x), 0
    while x != 0:
        digit = x % 10
        num = num * 10 + digit
        x /= 10
    num *= neg
    if num < -2147483648 or num > 2147483647:
        return 0
    return num


def main():
    x = 100003
    print reverse(x)


main()
