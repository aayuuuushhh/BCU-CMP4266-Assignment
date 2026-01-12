# 5.2 Create in Python the program which must:
# a. show the contents of the math module
# b. show the help of the functions used to perform the following calculations:
# • round up
# • exponentiation
# • logarithm
# • square root
# • absolute value

# c. ask the user for an integer value (positive, zero or negative)
# d. display the following calculation table:
# Entered value: xxx
# # Calculations #
# - Absolute value: xxx
# - Squared: xxx
# - Cube: xxx
# - Square root: xxx
# - Natural logarithm: xxx
# - Base 10 logarithm: xxx


import math
def main():
    print("Contents of the math module:")
    print(dir(math))

    print("Help for math.ceil (round up):")
    help(math.ceil)

    print("Help on exponentiation function (pow):")
    help(pow)

    print("Help for math.log (logarithm):")
    help(math.log)

    print("Help for sqaure root function (sqrt):")
    help(math.sqrt)

    print("Help on absolute value function (abs):")
    help(abs)

n = int(input("Enter an integer value (positive, zero or negative): "))

print(f"Entered value: {n}")
print("# Calculations #")

print(f"- Absolute value: {abs(n)}")
print(f"- Squared: {n**2}")
print(f"- Cube: {n**3}")

if n >= 0:
    print(f"- Square root: {math.sqrt(n)}")
else:
    print("- Square root: Cannot be calculated.")

if n > 0:
    print(f"-Natural logarithm:,{math.log(n)}")
else:
    print("-Natural logarithm: Cannot be calculated.")

if n > 0:
    print(f"- Base 10 logarithm: {math.log10(n)}")
else:
    print("-Base 10 logarithm: Cannot be calculated.")

if __name__ == "__main__":
    main()