#!/usr/bin/python

import sys

def compress(str):
    count = 1
    compressed = ''
    for i in range(len(str)):
        if i != len(str) - 1 and str[i] == str[i + 1]:
            count = count + 1
        else:
            compressed = compressed + str[i] + '%d' % count
            count = 1
    if len(str) <= len(compressed):
        return str
    else:
        return compressed

def main():
    print compress(sys.argv[1])

main()
