# Check if a given number is a one-digited or two digited or three digited or more than three digited.
n = int(input("Enter a number:"))
if -9 <= n <= 9:
    print("It is a one-digited number.")
elif -99 <= n <= 99:
    print("It is a two-digited number.")
elif -999 <= n <= 999:
    print("It is a three-digited number.")
else:
    print("It is more than three digits.")