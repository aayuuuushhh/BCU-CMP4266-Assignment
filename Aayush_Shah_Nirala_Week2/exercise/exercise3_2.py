# 3.2 Write a Python function to check whether three given numbers can form the sides of a triangle.
# If the numbers can form the sides of a triangle, calculate the perimeter and the surface area using Heron’s Formula.

import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print("These sides can form a triangle.")
    
    perimeter = a + b + c
    print("Perimeter is:", perimeter)
    
    s = perimeter / 2
    print("Semi perimeter is: ",s)
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Area is: {area:.2f}")
else:
    print("They are not side of a triangles")

    
    