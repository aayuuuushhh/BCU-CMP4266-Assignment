#3.1 Write a Python program to determine whether a given year is a leap year based on the given workflow for calculating a leap year.
# a) using Nested if
# b) using elif
# c) using Conditional statement

year = int(input("Enter a year:"))
if year % 4 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is a  not leap year")