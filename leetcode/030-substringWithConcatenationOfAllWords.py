#!/usr/bin/python

# You are given a string S and a list of words L that are all of the same length.
# Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once
# and without any intervening characters.

# For example, given
#   S: "barfoothefoobarman"
#   L: ["foo", "bar"]

# You should return the indices: [0, 9].
# (order does not matter).

# For each character c in S, check if it starts a substring that matches any concatenation of L.
# Do so until there are fewer characters in S left than concatenation of L.
# Since each character may be examined twice, the algorithm terminates in O(n^2).
def findSubstring(S, L):
    if not L:
        return list()
    length = len(L) * len(L[0])
    if not S or len(S) < length:
        return list()
    exists = dict()
    for word in L:
        if word in exists:
            exists[word] += 1
        else:
            exists[word] = 1
    i, indices = 0, list()
    while i < len(S) - length + 1:
        temp = dict(exists)
        substring = S[i : i + length]
        for j in range(0, len(substring), len(L[0])):
            word = substring[j : j + len(L[0])]
            if word not in temp or temp[word] == 0:
                break
            else:
                temp[word] -= 1
        if sum(temp.values()) == 0:
            indices.append(i)
        i = i + 1
    return indices

def main():
    S = 'abababab'
    L = ['a', 'b', 'a']
    print findSubstring(S, L)

main()
