# 2. Getting started
# 2.1 Consider the following Python program. What output will this code produce?
def f(x):
    x=10
x=5
f(x)
print(x)


# # 2.2 Consider the following Python program. What output will this code produce when run?
def mystery1(a, b):
    return a + b

def mystery2(a, b):
    if a > b:
        return a
    else:
        return b

def mystery3(a, b):
    if a < b:
        print(a)
        a = a + 2
        mystery3(a, b)

y = mystery1(10, 8)
print(y)

y = mystery2(10, 8)
print(y)

mystery3(10, 22)

# Output:
# 5
# 18
# 10
# 10
# 12
# 14
# 16
# 18
# 20