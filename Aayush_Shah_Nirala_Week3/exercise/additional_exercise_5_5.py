# 5.5 Write a program that loads an integer and prints its second digit from the left, third digit from the
# right. The digits will be printed if the given number has three digits, otherwise a message should be printed.

n = input("Enter an integer:")
if len(n) ==3:
    sec_left = n[1]
    third_left = n[-3]
    
    print("Second digit from left is:",sec_left)
    print("Third digit from right is:",third_left)
else:
    print("Error! Please input three digit number.")