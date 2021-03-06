#!/usr/bin/python

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

import sys

# Dynamic programming. O(n).
def climbStairs(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    d = [1, 2]
    for i in xrange(2, n):
        d.append(d[i - 1] + d[i - 2])
    return d[-1]

def main():
    print climbStairs(int(sys.argv[1]))

main()
