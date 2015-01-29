#!/usr/bin/python

# Implement atoi to convert a string to an integer

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
# what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (i.e., no given input specs). You are responsible
# to gather all the input requirements up front.

def atoi(str):
    str = str.strip()
    if not str: return 0
    neg = 1
    i = num = 0
    if str[i] == '+' or str[i] == '-':
        neg = -1 if str[i] == '-' else 1
        i = i + 1
    while i < len(str):
        if not str[i].isdigit():
            break
        num = num * 10 + ord(str[i]) - ord('0')
        i = i + 1
    return max(min(num * neg, 2147483647), -2147483648)

def main():
    print atoi(' \t -003073-\nab42')

main()
