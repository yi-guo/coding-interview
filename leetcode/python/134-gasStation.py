#!/usr/bin/python

# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i + 1).
# You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note: The solution is guaranteed to be unique.

# Start is not in [i, j] if the sum of gas - cost between [i, j] is smaller than 0.
def canCompleteCircuit(gas, cost):
    i = start = 0
    # Tells if the given gas and cost can complete the circuit.
    gasLeftIfStartsFromBeginning = 0
    # Tells where if the given gas and cost can complete the circuit.
    gasLeftIfStartsFromSomewhere = 0
    while i < len(gas):
        gasLeftIfStartsFromBeginning += gas[i] - cost[i]
        gasLeftIfStartsFromSomewhere += gas[i] - cost[i]
        if gasLeftIfStartsFromSomewhere < 0:
            gasLeftIfStartsFromSomewhere = 0
            start = i + 1
        i = i + 1
    return -1 if gasLeftIfStartsFromBeginning < 0 else start