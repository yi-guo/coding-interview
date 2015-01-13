#!/usr/bin/python

# Implement pow(x, n)

# x^n = x^(n/2) * x^(n/2) * x^(n%2). Pay attention to n < 0.
def pow(x, n):
    if x == 0 or x == 1:
        return x
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        sqrt = pow(x, abs(n) / 2)
        if n % 2 != 0:
            if n < 0:
                return 1 / float(sqrt * sqrt * pow(x, abs(n) % 2))
            return sqrt * sqrt * pow(x, abs(n) % 2)
        if n < 0:
            return 1 / float(sqrt * sqrt)
        return sqrt * sqrt 

def main():
    print pow(2, -3)

main()
