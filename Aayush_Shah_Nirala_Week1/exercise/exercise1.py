import math
A = float(input("Enter the value of A: "))
B= float(input("Enter the value of B: "))
C = float(input("Enter the value of C: "))
print(f"The value of A is {A}, B is {B} and C is {C}")
d=math.sqrt(B*B-4*A*C)
root1 = (-B+d)/(2*A)
root2 = (-B-d)/(2*A)
print(f"The value of root1 is: {root1}")
print(f"The value of root2 is: {root2}")

# Enter the value of A: 1
# Enter the value of B: 0
# Enter the value of C: -4
# The value of A is 1.0, B is 0.0 and C is -4.0
# The value of root1 is: 2.0
# The value of root2 is: -2.0


# Enter the value of A: 1
# Enter the value of B: 5
# Enter the value of C: -36
# The value of A is 1.0, B is 5.0 and C is -36.0
# The value of root1 is: 4.0
# The value of root2 is: -9.0

# Enter the value of A: 2
# Enter the value of B: 7.5
# Enter the value of C: 6
# The value of A is 2.0, B is 7.5 and C is 6.0
# The value of root1 is: -1.1569296691827464
# The value of root2 is: -2.5930703308172536

# A=0, B=3.5, C=8
# This test case fails and generates an error beacuse value of A is 0