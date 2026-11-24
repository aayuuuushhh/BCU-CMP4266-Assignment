# 2. Getting started
# 2.1 Consider the following Python program. Find potential sources of errors in this code (Hint:3
# errors).

x = float(input("Please enter x: "))
y = float(input("Please enter y: "))
if y != 0:
    z = x / y
    z_rounded = round(z, 2)
    print("Rounded result: ",z_rounded)
else:
    print("Error! Division by zero is not allowed.")
    
    
# 2.2 Consider the following Python program. Find potential sources of errors in this code.

x = 1
for i in range(5):
    x *= 2 

sum_squares = 0
for i in range(5):
    i_sq = i**2
    sum_squares += i_sq
    
total = 0
for i in range(10):
    total += i

print("x: ",x)
print("Sum of sqaures: ", sum_squares)
print("Total: ",total)
    
