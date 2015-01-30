#!/usr/bin/python

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is "((()))", "(()())", "(())()", "()(())", "()()()".

import sys
import collections


# For every parenthesis of what we have, make new ones by inserting another pair after every possible '('.
# Also append another pair to every parenthesis of what we have.
# Eliminate duplicates using a hash set.
def generateParenthesis(n):
    if n < 1: return list()
    existed = set()
    queue = collections.deque(['()'])
    while len(queue[0]) < n * 2:
        curr = queue.popleft()
        new = curr + '()'
        if new not in existed:
            queue.append(new)
            existed.add(new)
        for i in xrange(len(curr)):
            if curr[i] == '(':
                new = curr[:i + 1] + '()' + curr[i + 1:]
                if new not in existed:
                    queue.append(new)
                    existed.add(new)
    return list(queue)

def main():
    print generateParenthesis(int(sys.argv[1]))

main()
