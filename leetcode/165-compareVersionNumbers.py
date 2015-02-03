#!/usr/bin/python

# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision
# of the second first-level revision.

# Here is an example of version numbers ordering:

# 0.1 < 1.1 < 1.2 < 13.37

# Split the version strings with '.' and make them the same length by adding 0's before comparisons.
def compareVersion(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    version1 = version1 + ['0'] * (len(version2) - len(version1))
    version2 = version2 + ['0'] * (len(version1) - len(version2))
    for i in xrange(len(version1)):
        if int(version1[i]) < int(version2[i]):
            return -1
        elif int(version1[i]) > int(version2[i]):
            return 1
    return 0

def main():
    print compareVersion('1.2.1', '1.11')

main()
