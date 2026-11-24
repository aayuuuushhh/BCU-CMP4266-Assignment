# 5.4 Write a program that checks whether a given number is one digit, two digits, three
# digits, or more than three digits.

n = int(input("Enter a number:"))
if -9 <= n <= 9:
    print("It is a one-digited number.")
elif -99 <= n <= 99:
    print("It is a two-digited number.")
elif -999 <= n <= 999:
    print("It is a three-digited number.")
else:
    print("It is more than three digits.")