# Test if a 5-digit number is a palindrome.
# (A palindromic number (such as 16461) that remains the same when its digits are reversed.

n = input("Enter a five-digit number:")
if len(n) == 5:
    if n == n[::-1]:
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")
else:
    print("Invalid input! Please input five digit number.")
    