#!/usr/bin/python

# Determine whether an integer is a palindrome. Do this without extra space.

def isPalindrome(x):
    if x < 0:
        return False
    if x < 10:
        return True
    elif x < 100:
        return x % 11 == 0
    n = 3
    while x - pow(10, n) >= 0:
        n = n + 1
    while x != 0:
        ls = x % 10
        ms = x / pow(10, n - 1)
        if ls != ms:
            return False
        x = x % pow(10, n - 1) / 10
        n = n - 2
    return True

def main():
    print isPalindrome(1000021)

main()
