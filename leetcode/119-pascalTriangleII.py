#!/usr/bin/python

# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3, return [1, 3, 3, 1].

# Note: Could you optimize your algorithm to use only O(k) extra space?

import sys

# Generate current one based on the previous one. Do the addition in place from the end.
def getRow(rowIndex):
    if rowIndex == 0: return [1]
    row = [0 for i in range(rowIndex + 1)]
    i, row[0] = 0, 1
    while i < rowIndex:
        for j in range(len(row) - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
        i = i + 1
    return row

def main():
    print getRow(int(sys.argv[1]))

main()
