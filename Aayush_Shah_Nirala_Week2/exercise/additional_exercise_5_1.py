# 5.1 Write a program that finds the minimum of three given numbers.
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))

if a<=b and a <=c:
    print("Minimum number is:",a)
elif b<=a and b<=c:
    print("Minimum number is:",b)
else:
    print("Minimum number is:",c)