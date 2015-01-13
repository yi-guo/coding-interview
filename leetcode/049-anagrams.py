#!/usr/bin/python

# Given an array of strings, return all groups of strings that are anagrams.

# Note: All inputs will be in lower-case.

# For every given string, use the sorted string as a key to group anagrams together in a hash table.
def anagrams(strs):
    if not strs or len(strs) < 2:
        return list()
    hashmap = dict()
    for s in strs:
        key = ''.join(sorted(s))
        if key in hashmap:
            hashmap[key].append(s)
        else:
            hashmap[key] = [s]
    anagrams = list()
    for key in hashmap:
        if len(hashmap[key]) > 1:
            anagrams.extend(hashmap[key])
    return anagrams

def main():
    print anagrams(["cab", "pug", "pei", "nay", "ron", "rae", "ems", "ida", "mes"])

main()
