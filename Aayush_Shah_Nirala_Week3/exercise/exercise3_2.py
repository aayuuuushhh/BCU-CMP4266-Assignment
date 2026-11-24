# 3.2 Create a Python program that prompts the user for a password. It will keep asking for the
# password until either the correct password "test100" is provided or the user attempts to enter
# the password up to 5 times.
# The program will continuously request the user to input a password until either of the
# following scenarios occurs:
# The user enters the correct password "test100," the program should print "You are
# logged in."
# The user reaches the maximum number of allowed attempts (5 attempts), the program
# should print " You’ve reached the maximum logon attempts."

correct_password = "test100"
attempts = 0
max_attempts = 5

while attempts <= max_attempts:
    password = input("Enter password: ")
    attempts += 1
    
    if password == correct_password:
        print("You are logged in.")
        break
    else:
        print("Incorrect password.")
        
if attempts == max_attempts and password != correct_password:
    print("You've reached the maximum login attempts.")