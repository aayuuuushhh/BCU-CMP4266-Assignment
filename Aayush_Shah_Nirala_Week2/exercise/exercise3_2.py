# 3.2 Write a program to determine whether a given year is a leap year. A year is a leap year if
# any of the following conditions are satisfied:
# The year is multiple of 400 (e.g., 2000).
# The year is a multiple of 4 and not a multiple of 100 (eg. 2032)

year = int(input("Enter a year:"))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is  a leap year")
else:
    print(f"{year} is a  not leap year")