#!/usr/bin/python

# Source: Magnitude Capital Online Assessment

# You are given a year Y and two months A and B, where Y is an integer and A and B are strings.
# You are also given a day W indicating the day of the first day of year Y.
# Write a program to calculate the number of whole weeks inclusively from the first day of A to the last day of B,
# where a whole week is defined as a week that starts on Monday and ends on Sunday.

# You may assume that
#   - Y is a leap year if and only if Y is divisible by 4.
#   - A in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
#           'September', 'October', 'November', 'December']
#   - B in [A, 'December']
#   - W in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Your program should return an integer.

# For example, given Y = 2015, A = 'February', B = 'March', and W = 'Thursday', you program should return 8 since
# we have the week of 2/2, 2/9, 2/16, 2/23, 3/2, 3/7, 3/9, 3/16, 3/23.

def numOfWholeWeeks(Y, A, B, W):
    # Look-up table that maps a month in string to its integer representation
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
              'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    # Look-up table that maps a day in string to its integer representation
    days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    # Look-up table that gives the number of days in month i + 1 where 0 <= i <= 11.
    numOfDaysInMonth = [31, 28 if Y % 4 != 0 else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Get the number of days from the first day of A to the last day of B.
    numOfDaysBetweenAB = 0
    for i in xrange(months[A], months[B] + 1):
        numOfDaysBetweenAB += numOfDaysInMonth[i - 1]
    # Get the number of days before the first dat of A.
    numOfDaysBeforeA = 0
    for i in xrange(1, months[A]):
        numOfDaysBeforeA += numOfDaysInMonth[i - 1]
    # Get the day of the first day of A; 0 if Sunday otherwise as what it is in the look-up table.
    firstDayInA = (numOfDaysBeforeA + days[W]) % 7
    # Get the day of the last day of B;  0 if Sunday otherwise as what it is in the look-up table.
    lastDayInB = (numOfDaysBeforeA + numOfDaysBetweenAB - 1 + days[W]) % 7
    # Eliminate the days that do not belong to a whole week, i.e., the first few days in A and the last few days in B.
    numOfDaysBetweenAB = numOfDaysBetweenAB - (1 - firstDayInA if firstDayInA < 2 else 8 - firstDayInA) - lastDayInB
    # Return the number of whole weeks.
    return numOfDaysBetweenAB / 7

def main():
    print numOfWholeWeeks(2016, 'March', 'April', 'Friday')

main()
