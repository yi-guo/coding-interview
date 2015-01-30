#!/usr/bin/python

# Implement pow(x, n)


# x^n = x^(n/2) * x^(n/2) * x^(n%2). Pay attention to n < 0.
def pow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return pow(1 / x, abs(n))
    else:
        halfPow = pow(x, n / 2)
        return halfPow * halfPow if n % 2 == 0 else halfPow * halfPow * x


def main():
    print pow(2.0, -3)

main()
