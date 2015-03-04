#!/usr/bin/python

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

def convertToTitle(num):
    title = list()
    while num != 0:
        curr = num % 26
        if curr == 0:
            curr, num = 26, num - 1
        title.append(chr(curr + 64))
        num = num / 26
    return ''.join(title[::-1])

def main():
    for i in xrange(1, 1000):
        print convertToTitle(i)

main()
