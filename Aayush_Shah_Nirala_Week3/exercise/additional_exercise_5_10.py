# 5.10 Modify your exercise 5.8 The Goldbach conjecture asserts that every even number is the sum of
# twoprime numbers. Modify the program that gets a number from the user, checks to make sure that it is
# even, and then finds two prime numbers that add up to it.

num = int(input("Enter an even number: "))

if num % 2 !=0:
    print("Please enter an even number.")
else:
    for a in range(2, num):
        prime1 = True
        for i in range(2, a):
            if a % i == 0:
                prime1 = False
                break
            
        b = num - a
        prime2 = True
        for j in range(2, b):
            if b % j == 0:
                prime2 = False
                break
        if prime1 and prime2:
            print(f"Two prime numbers are: {a} and {b}")
            break