#!/usr/bin/python

# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

import sys

# Traverse and count the characters in the (n-1)th say.
def countAndSay(n):
    if n == 1:
        return '1'
    prevSay = countAndSay(n - 1) + '\n'
    say = list()
    currChar, count = prevSay[0], 1
    for i in range(1, len(prevSay)):
        if prevSay[i] == currChar:
            count = count + 1
        else:
            say.append(str(count) + currChar)
            currChar, count = prevSay[i], 1
    return ''.join(say)

def main():
    print countAndSay(int(sys.argv[1]))

main()
