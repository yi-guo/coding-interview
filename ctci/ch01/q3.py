#!/usr/bin/python

import sys

def isPermutation1(str1, str2):
	if len(str1) != len(str2):
		return False
	lst1 = sorted(str1)
	lst2 = sorted(str2)
	for i in range(len(str1)):
		if lst1[i] != lst2[i]:
			return False
	return True

def isPermutation2(str1, str2):
	if len(str1) != len(str2):
		return False
	lst = [0 for i in range(128)]
	for i in range(len(str1)):
		lst[ord(str1[i])] = lst[ord(str1[i])] + 1
		lst[ord(str2[i])] = lst[ord(str2[i])] - 1
	return not all(lst)

def main():
	print isPermutation1(sys.argv[1], sys.argv[2])
	print isPermutation2(sys.argv[1], sys.argv[2])


main()