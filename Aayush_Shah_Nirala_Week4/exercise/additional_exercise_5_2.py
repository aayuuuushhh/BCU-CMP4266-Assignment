# 5.2 Write a function named digits that takes one parameter that is a number (int) and returns a count of
# even digits, a count of odd digits and a count of zero digit. For example: digit (1234567890123) returns
# (5, 7, 1).

def digits(num):
    even = 0
    odd = 0
    zero = 0
    
    for digits in str(num):
        d = int(digits)
        if d == 0:
            zero += 1
        elif d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd, zero)

result = digits(1234567890123)
print(result)
        