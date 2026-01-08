# 3.1 A positive whole number n > 2 is prime if no number between 2 and √n (inclusive) evenly
# divides n. Write a program that accepts a value of n as input and determines if the number is
# prime. If n is not prime, your program should print all the divisors of n.

n =int(input("Enter a positive number greater than 2:"))
if n <= 2:
    print("Number must be greater than 2")
else:
    is_prime = True
    div = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            div.append(i)
            div.append(n//i)
    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
        print("Divisors are:",div)
                