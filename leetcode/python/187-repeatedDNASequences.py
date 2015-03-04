#!/usr/bin/python

# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# For example, given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", return ["AAAAACCCCC", "CCCCCAAAAA"].

from collections import defaultdict

# Use hash table to keep track of the number of every 10-letter sequence.
def findRepeatedDnaSequences(s):
    sequences, existed = list(), defaultdict(int)
    for i in xrange(len(s) - 9):
        sequence = s[i : i + 10]
        if existed[sequence] == 1:
            sequences.append(sequence)
        existed[sequence] += 1
    return sequences

def main():
    s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    print findRepeatedDnaSequences(s)

main()
