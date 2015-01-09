#!/usr/bin/python

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is "((()))", "(()())", "(())()", "()(())", "()()()".

import sys

# For every parenthesis of what we have, make new ones by inserting another pair after every possible '('.
# Also append another pair to every parenthesis of what we have.
# Eliminate duplicates using a hash set.
def generateParenthesis(n):
    if n < 1:
        return [str()]
    elif n == 1:
        return ['()']
    exists, parentheses = set(), [str()]
    for i in range(n):
        j, length = 0, len(parentheses)
        while j < length:
            head = parentheses.pop(0)
            if head + '()' not in exists:
                exists.add(head + '()')
                parentheses.append(head + '()')
            for k in range(len(head)):
                if head[k] == '(':
                    new = head[:k + 1] + '()' + head[k + 1:]
                    if new not in exists:
                        exists.add(new)
                        parentheses.append(new)
            j = j + 1
    return parentheses

def main():
    print generateParenthesis(int(sys.argv[1]))

main()
