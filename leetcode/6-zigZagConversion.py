#!/usr/bin/python

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
# display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);

# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 


# Each character will be visited once ONLY, thus O(n)
def convert(s, nRows):
    if len(s) <= nRows or nRows == 1:
        return s
    if not s or nRows <= 0:
        return None
    zigzag = list()
    for i in range(nRows):
        if i == 0 or i == nRows - 1:
            for j in range(i, len(s), nRows * 2 - 2):
                zigzag.append(s[j])
        else:
            j, flag = i, True
            while j < len(s):
                zigzag.append(s[j])
                if flag:
                    j = j + (nRows - i - 1) * 2
                else:
                    j = j + i * 2
                flag = not flag
    return ''.join(zigzag)

def main():
    print convert("PAYPALISHIRING", 3)
    print convert("AB", 1)

main()
