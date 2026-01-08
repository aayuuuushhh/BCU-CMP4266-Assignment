# # 2.1.1 Construct the variable trace and predict the output
amount1 = float(input("Enter amount1:"))
amount2 = float(input("Enter amount2:"))
amount1 *= 0.8
amount2 *= 0.9
tax = amount1 * 0.3 + amount2 * 0.2
total = amount1 + amount2 + tax
print(tax)
print(f"Total Cost:${total}")

# amoun1    amount2     tax     total
# 10          20        6.0     $32.0
# 50          40        19.2    $95.2
# 35          60        19.20   $101.2
  
# 2.1.2. What is the print out of the following? Check your answer in python
print(3*'Yes',2*'!') #YesYesYes !!
print(3*'Yes'+2*'!') #YesYesYes !!
print(2**2**3) #256
print(2**(2**3)) #256
print(10//3**2+(2%3)) #3

# 2.1.3 Evaluate the following expressions and note the data type of the result:
print(3*2) #6 #int
print('3'+'2') #32  #str
print('3'*2) #33  #str
print(3/2) #1.5   #float
print(3//2) #1    #int
print(3+2.0) #5.0  #float
print(3>2) #True  #bool
print(3!=2) #True  #bool
print(4==2**2) #True  #bool
print(3>2 and 10>11) #False  #bool
print(3>2 and not(10>11)) #True  #bool
print(format(5.1,'.2f')) #5.10  #str
print(not(3>2 and 5<4)) #True  #bool


# 1. What is syntax error? Give an example of one in Python.
# Answer: The error which occurs when  Python cannot understand the code due to incorrect syntax is called syntax error.
# Example :
# if True
#     print("Hello")
# Output: SyntaxError: expected ':'


# 2. What is run-time error? Give an example of one in Python.
# Answer: The error that occurs during program execution when Python encounters an unexpected situation is known as run-time error.
# Example:
# x = 10 / 0
# Output: ZeroDivisionError: division by zero


# 3. What is a logic error? Give an example of one in Python.
# Answer: The error that occurs when the program runs without crashing, but the output is incorrect is called logic error.
# Example:
# x = 10
# y = 5
# result = x - y  # Intended to add
# print(result)
# Output: 5
    