#!/usr/bin/python

# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# For each character in haystack, if it matches the first character of needle, start checking the rest.
# Do so until there are fewer characters left in haystack than needle.
# Since each character in haystack could possibly be visited twice, the algorithm takes O(n^2).
# This solution passes the OJ; however, check out KMP algorithm for smarter solution, which completes in O(n)!
def strStr(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    elif not needle or haystack == needle:
        return 0
    i, index = 0, -1
    while i < len(haystack) - len(needle) + 1:
        if haystack[i] == needle[0]:
            index, j = i, i + 1
            for k in range(1, len(needle)):
                if haystack[j] == needle[k]:
                    j = j + 1
                else:
                    index = -1
                    break
            if index != -1:
                return index
        i = i + 1
    return index

def main():
    print strStr("ABC ABCDAB ABCDABCDABD", "ABCDABD")

main()
