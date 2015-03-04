#!/usr/bin/python

# Implement atoi to convert a string to an integer

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
# what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (i.e., no given input specs). You are responsible
# to gather all the input requirements up front.

def atoi(str):
    str = str.lstrip()
    if not str: return 0
    neg, num = 1, 0
    if str[0] == '+' or str[0] == '-':
        neg = -1 if str[0] == '-' else 1
        str = str[1:]
    for c in str:
        if not c.isdigit():
            break
        num = num * 10 + ord(c) - ord('0')
    return max(min(neg * num, 2147483647), -2147483648)

def main():
    print atoi(' \t -003073-\nab42')

main()
