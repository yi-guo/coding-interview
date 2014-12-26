#!/usr/bin/python

import sys

# Sort the string and check neighboring chars
# O(nlog(n))
def hasUniqueChar1(str):
    if len(str) > 128:
        return False
    lst = sorted(str)
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False
    return True 

# Construct a hash table for all ASCII chars
# O(n)
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

# Construct a hash set of all chars in the string and compare the length
# O(n)
def hasUniqueChar3(str):
    if (len(str)) > 128:
        return False
    return len(set(str)) == len(str)

def main():
    print hasUniqueChar1(sys.argv[1])
    print hasUniqueChar2(sys.argv[1])
    print hasUniqueChar3(sys.argv[1])


main()