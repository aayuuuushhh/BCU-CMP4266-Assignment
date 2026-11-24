# simple types and conversions between types
i = int(input("enter a whole number"))
print(i)

s = input("enter a whole number")
i = int(s)
print(i)

# Converting numbers as strings into integers and floats
int('10.9')

f = float('10.9')
int(f)
print(f)

# Converting between floats and ints
int(9.6)
float(8)
print(8*1.0)

# Converting numbers into string format
str(8.5)
str(3)
s = "an int %d number" %10
print(s)

s = "a float %f number"%3.3
print(s)

s = "a flaot %.2f number"%3.3
print(s)

s = "a float %10.2f"%123456789.01
print(s)

s = "a float %14.2f"%123456789.01
print(s)

a = 10
b = 3.6
print("a float %f and an int %d"%(b,a))

# 2. Getting started
# 2.1 Fill in the unshaded cells in the table below by constructing the variable trace for each line
# below and predicting the output.

amount1 = 10.0
amount2 = 40.0
amount1 *= 0.8
amount2 *= 0.9
tax = amount1 * 0.3 + amount2 * 0.2
total = amount1 + amount2 + tax
print(tax)
print(f"Total Cost:${total}")

# 2.1.2. What is the print out of the following. Fill in the table below and check your answer in Python.

print(3*'Yes',2*'!') 
print(3*'Yes'+2*'!')
print(2**2**3) 
print(2**(2**3)) 
print(10//3**2+(2%3)) 

# 2.1.3 Evaluate the following expressions and note the data type of the result. Fill in the table
# below with the output you got and its data type:

print(3*2) 
print('3'+'2') 
print('3'*2) 
print(3/2) 
print(3//2) 
print(3+2.0) 
print(3>2) 
print(3!=2) 
print(4==2**2) 
print(3>2 and 10>11) 
print(3>2 and not(10>11)) 
print(format(5.1,'.2f')) 
print(not(3>2 and 5<4)) 