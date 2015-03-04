#!/usr/bin/python

import timeit

# Return the elapsed time of a section of code.
def test():
    test = [0 for i in range(1000000)]

def main():
    start = timeit.default_timer()
    for i in range(1000):
        test()
    end = timeit.default_timer()
    print end - start

main()
