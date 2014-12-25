#!/usr/bin/python

import sys

def hasUniqueChar1(str):
    if len(str) > 128:
        return False
    lst = list(sorted(str))
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False
    return True 

def hasUniqueChar2(str):
    if len(str) > 128:
        return False
    lst = [False for i in range(128)]
    for c in str:
        if lst[ord(c)]:
            return False
        else:
            lst[ord(c)] = True
    return True

def main():
    print hasUniqueChar1(sys.argv[1])
    print hasUniqueChar2(sys.argv[1])


main()
