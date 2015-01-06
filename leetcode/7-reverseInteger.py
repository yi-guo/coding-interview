#!usr/bin/python

# Reverse digits of an integer.

# Example: x = 123, return 321
# Example: x = -123, return -321

# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# Convert the integer into a list of digits and reverse
def reverse(x):
    if abs(x) < 10:
        return x
    l = [i for i in str(abs(x))]
    i, j = 0, len(l) - 1
    while i < j:
        l[i], l[j] = l[j], l[i]
        i = i + 1
        j = j - 1
    r = int(''.join(l))
    if x < 0:
        r = 0 - r
    if r < -2147483648 or r > 2147483647:
        return 0
    return r

def main():
    x = 1000000003
    print reverse(x)

main()
