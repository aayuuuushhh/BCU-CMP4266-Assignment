# 5.1 Write a loop that computes the sum of the squares of the numbers between 1 and 100, inclusive.
num = 0
for i in range(1,101):
    num = num + i**2
print("The sum of squares from 1 to 100 is:",num)