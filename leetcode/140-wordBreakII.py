#!/usr/bin/python

# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence
# where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

# Recursion with dynamic programming.
# Maintain an array breakable such that breakable[i] is true if s[i:] is breakable.
def wordBreak(s, dict):

    def nextBreak(s, index, dict, words):
        if index == len(s):
            res.append(' '.join(words))
        else:
            for i in range(index, len(s)):
                # Only attempt to search breakable solutions when it is breakable.
                if s[index : i + 1] in dict and breakable[i]:
                    originalSize = len(res)
                    words.append(s[index : i + 1])
                    nextBreak(s, i + 1, dict, words)
                    # No solution added, which means s[i:] is not breakable
                    if len(res) == originalSize:
                        breakable[i] = False
                    words.pop()

    res = []
    breakable = [True for c in s]
    nextBreak(s, 0, dict, list())
    return res

def main():
    s = 'catsanddog'
    dict = ["cat", "cats", "and", "sand", "dog"]
    print wordBreak(s, dict)

main()