#!/usr/bin/python

# Validate if a given string is numeric.

# Some examples:
#   "0" => true
#   " 0.1 " => true
#   "abc" => false
#   "1 a" => false
#   "2e10" => true

# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.

import sys

# An automata solution. O(n).
def isNumber(s):
    return s0(s.strip(), 0)

def s0(s, i):
    if i == len(s):
        return False
    if s[i] == '.':
        return s1(s, i + 1)
    elif s[i] == '+' or s[i] == '-':
        return s2(s, i + 1)
    elif s[i].isdigit():
        return s3(s, i + 1)
    else:
        return False

def s1(s, i):
    if i == len(s):
        return False
    if s[i].isdigit():
        return s4(s, i + 1)
    else:
        return False

def s2(s, i):
    if i == len(s):
        return False
    if s[i] == '.':
        return s1(s, i + 1)
    elif s[i].isdigit():
        return s3(s, i + 1)
    else:
        return False

def s3(s, i):
    if i == len(s):
        return True
    if s[i] == '.':
        return s4(s, i + 1)
    elif s[i] == 'e':
        return s5(s, i + 1)
    elif s[i].isdigit():
        return s3(s, i + 1)
    else:
        return False

def s4(s, i):
    if i == len(s):
        return True
    if s[i] == 'e':
        return s5(s, i + 1)
    elif s[i].isdigit():
        return s4(s, i + 1)
    else:
        return False

def s5(s, i):
    if i == len(s):
        return False
    if s[i] == '+' or s[i] == '-':
        return s6(s, i + 1)
    elif s[i].isdigit():
        return s7(s, i + 1)
    else:
        return False

def s6(s, i):
    if i == len(s):
        return False
    if s[i].isdigit():
        return s7(s, i + 1)
    else:
        return False

def s7(s, i):
    if i == len(s):
        return True
    if s[i].isdigit():
        return s7(s, i + 1)
    else:
        return False

def main():
    print isNumber(sys.argv[1])

main()
