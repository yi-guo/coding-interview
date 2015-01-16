#!/usr/bin/python

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
#	S = "ADOBECODEBANC"
#   T = "ABC"
# Minimum window is "BANC".

# Note:
# 1. If there is no such window in S that covers all characters in T, return the emtpy string "".
# 2. If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# Two pointers with a hashmap keeping track of how many chars in T have been found in S. One pass, thus O(n).
def minWindow(S, T):
    if not S or not T or len(S) < len(T):
        return str()
    count = {c : T.count(c) for c in T}
    i, length, window, next = 0, 0, str(), list()
    while i < len(S):
        j = i + 1
        if S[i] in count:
            count[S[i]] -= 1
            while j < len(S):
                if S[j] in count:
                    next.append(j)
                    count[S[j]] -= 1
                    covered = all([x < 1 for x in count.values()])
                    while covered:
                        window = S[i : j + 1] if not window else min(window, S[i : j + 1], key=len)
                        count[S[i]] += 1
                        covered = True if count[S[i]] < 1 else False
                        i = next.pop(0) if len(next) > 0 else j
                j = j + 1
            if all([x < 1 for x in count.values()]):
                window = S[i : i + 1]
        i = j
    return window

def main():
    print minWindow("ADABOBECAODEBANC", "ABC")

main()
