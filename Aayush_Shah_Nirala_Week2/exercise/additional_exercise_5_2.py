# 5.2 Write a program that tests if a 5-digit number is a palindrome. A palindrome is a
# number that remains the same when its digits are reversed (e.g., 12621).

n = input("Enter a five-digit number:")
if len(n) == 5:
    if n == n[::-1]:
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")
else:
    print("Invalid input! Please input five digit number.")
    