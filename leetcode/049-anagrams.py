#!/usr/bin/python

# Given an array of strings, return all groups of strings that are anagrams.

# Note: All inputs will be in lower-case.

from collections import defaultdict

# For every given string, use the sorted string as a key to group anagrams together in a hash table.
def anagrams(strs):
    hashmap = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        hashmap[key].append(s)
    anagram = list()
    for key in hashmap:
        if len(hashmap[key]) > 1:
            anagram.extend(hashmap[key])
    return anagram

def main():
    print anagrams(["cab", "pug", "pei", "nay", "ron", "rae", "ems", "ida", "mes"])

main()
