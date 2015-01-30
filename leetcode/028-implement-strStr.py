#!/usr/bin/python

# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# For each character in haystack, if it matches the first character of needle, start checking the rest.
# Do so until there are fewer characters left in haystack than needle.
# Since each character in haystack could possibly be visited twice, the algorithm takes O(n^2).
# This solution passes the OJ; however, check out KMP algorithm for smarter solution, which completes in O(n)!
def strStr(haystack, needle):
    if not needle or haystack == needle:
        return 0
    for i in xrange(len(haystack) - len(needle) + 1):
        index = i
        for j in xrange(len(needle)):
            if haystack[index] != needle[j]:
                break
            else:
                if j == len(needle) - 1:
                    return i
                index = index + 1
    return -1


def main():
    print strStr("ABC ABCDAB ABCDABCDABD", "ABCDABD")


main()
