#!/usr/bin/python

# Implement atoi to convert a string to an integer

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
# what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (i.e., no given input specs). You are responsible
# to gather all the input requirements up front.

def atoi(str):
    if not str:
        return 0
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    start = -1
    for i, c in enumerate(str):
        if c.isdigit() or c == '-' or c == '+':
            start = i
            break
        if not c.isspace():
            return 0
    if start == -1:
        return 0
    i = start + 1
    while i < len(str):
        if not str[i].isdigit():
            break
        i = i + 1
    num = str[start:i]
    if num == '+' or num == '-':
        return 0
    num = int(num)
    if num > INT_MAX:
        return INT_MAX
    elif num < INT_MIN:
        return INT_MIN
    else:
        return num

def main():
    print atoi(' \t -003073-\nab42')

main()
