#!/usr/bin/python

# Determine whether an integer is a palindrome. Do this without extra space.

def isPalindrome(x):
    if x < 0:
        return False
    div = 1
    while x / div >= 10:
        div *= 10
    while x != 0:
        ms = x / div
        ls = x % 10
        if ms != ls:
            return False
        x = x % div / 10
        div /= 100
    return True

def main():
    print isPalindrome(1000021)

main()
