# 5.5. Create in Python a program which receives a positive integer number from the user and displays the list
# of prime numbers smaller than the given value. The program must follow these guidelines:

# a. it must manage the entry of invalid inputs
# b. even numbers should be excluded from the check, since they cannot be prime numbers

# E.g., if the user enters number 10, the result must be: “Prime list: 1, 2, 3, 5, 7”.

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Invalid input.")
            return
    except ValueError:
        print("Invalid input.")
        return
    
    primes = [1, 2]
    for num in range(3, n):
        if num % 2 == 0:
            continue
        is_prime = True
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print("Prime list:", ', '.join(map(str, primes)))

if __name__ == "__main__":
    main()