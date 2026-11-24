# 5.4 Write a program that accepts integer inputs from a user as long as the word stop is not input. Compute and print the minimum of these integers.
min = None
while  True:
      user_input = input ("Enter an integer (or type 'stop' to finish):")
      if user_input.lower() == 'stop':
            break
      num = int(user_input)

      if min is None or num < min:
            min = num
print("The minimum number is:", min)