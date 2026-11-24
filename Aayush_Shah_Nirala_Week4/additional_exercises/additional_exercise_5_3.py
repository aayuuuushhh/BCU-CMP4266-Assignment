# 5.3 Write a Python function to check whether a number is perfect or not. (A perfect number is a positive
# integer that is equal to the sum of its proper positive divisors ex. 28 = 1 + 2 + 4 + 7 + 14)

def perfect(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i 
    
    if total == n:
        return True
    else:
        return False
    
n = int(input("Enter a number: "))
if perfect(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")