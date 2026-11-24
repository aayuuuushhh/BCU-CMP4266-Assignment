def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def calculator(num1,num2,operator):
    if operator == '+':
        print(f"Adding {num1} and {num2} is:",add(num1,num2))
    elif operator == '-':
        print(f"Subtracting {num1} and {num2} is:",subtract(num1,num2))
    elif operator == '*':
        print(f"Multiplying {num1} and {num2} is:",multiply(num1,num2))
    elif operator =='/':
        print(f"Dividing {num1} and {num2} is:",divide(num1,num2))
    else:
        print("Invalid operator.")
        
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
operator = input("Select an operator(+, -, *, /):")
calculator(num1, num2, operator)
        


