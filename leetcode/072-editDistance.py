#!/usr/bin/python

# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
# (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:
# a) Insert a character
# b) Delete a character
# c) Replace a character

# Dynamic programming. O(mn).
def minDistance(word1, word2):
    # If same, then no need to do anything
    if word1 == word2:
        return 0
    # If one is an empty string, return the length of the other.
    if not word1 or not word2:
        return len(word1) if word1 else len(word2)
    # If one is a substring of the other, return the difference in length.
    if word1 in word2 or word2 in word1:
        return abs(len(word1) - len(word2))
    l1, l2 = len(word1), len(word2)
    # Maintain a matrix where d[i][j] is the minimum steps to convert word1 up to index i to word2 up to index j.
    d = [range(l2 + 1) for i in range(l1 + 1)]
    # d[i][0] and d[0][j] are base cases.
    for i in range(1, l1 + 1):
        d[i][0] = d[i - 1][0] + 1
    # Update matrix where d[i][j] is the minimum of
    # 1. d[i - 1][j] + 1, where an insertion is needed.
    # 2. d[i][j - 1] + 1, where a deletion is needed.
    # 3. d[i - 1][j - 1] + 1 if word1[i - 1] != word2[i - 2], where a replace is needed.
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + int(word1[i - 1] != word2[j - 1]))
    return d[l1][l2]

def main():
    print minDistance('sea', 'eat')

main()
