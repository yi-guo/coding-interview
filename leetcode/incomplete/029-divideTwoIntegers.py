#!/usr/bin/python

# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.

import sys

def divide(dividend, divisor):
	if divisor == 0:
		return None
	if dividend == 0:
		return 0
	elif divisor == 1:
		return dividend

def main():
	print int(sys.argv[1]) / int(sys.argv[2])

main()
