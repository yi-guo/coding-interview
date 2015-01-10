#!/usr/bin/python

# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    index = -1
    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:
            index = i
            print index
            for j in range(len(needle)):
                print i, j
                if haystack[i] != needle[j]:
                    index = -1
                    break
                else:
                    i = i + 1
            if index != -1:
                return index
        i = i + 1
    return index





def main():
    print strStr("ABC ABCDAB ABCDABCDABDE", "ABCDABD")

main()
