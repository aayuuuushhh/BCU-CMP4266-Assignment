#  Find the minimum of three given numbers.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a<=b and a <=c:
    print("Minimum number is:",a)
elif b<=a and b<=c:
    print("Minimum number is:",b)
else:
    print("Minimum number is:",c)