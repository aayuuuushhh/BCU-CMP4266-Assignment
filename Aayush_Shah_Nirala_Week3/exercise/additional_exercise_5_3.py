# 5.3 Write a loop that computes the sum of all the odd digits in a non-negative integer n.
n = int(input("Enter a non-negative integer: "))
sum_odd = 0
for digit in str(n):
      digit = int(digit)

      if digit % 2 == 1:
            sum_odd += digit

print("Sum of odd digits = ", sum_odd)