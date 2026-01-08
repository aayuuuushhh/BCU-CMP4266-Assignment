#1.1 While loop
# count = 0
# while (count<5):
#     print("The count is:",count)
#     count += 1
#     print("Done!")
    
# count = 0
# while (count<5):
#     print("The count is:",count)
#     count -= 1
#     print("Done!")

# count = 0
# while count < 3:
#     print (count,"is less than 3")
#     count = count + 1
# else:
#     print (count,"is not less than 3")4

# While loops with sentinel values
# score = int(input("enter a test score, use -1 to stop "))
# total = 0
# scoreCounter = 0
# while score != -1:  
#     total = total + score
#     scoreCounter = scoreCounter + 1
#     score = int(input("enter a test score, use -1 to stop "))
# print ("The total of the score is ",total)
# print("Number of scores:", scoreCounter)

#1.2 For Loop
# for num in [0, 1, 2, 3, 4]:
#     print(num, end='')
    
# for num in range(5):
#     print(num, end='')

# # Prints out 0,1,2,3,4
# for x in range(5):
#     print(x)
# # Prints out 3,4,5
# for x in range(3, 6):
#     print(x)
# # Prints out 3,5,7
# for x in range(3, 8, 2):
#     print(x)
    
# # 1.3 Jump Statements
# for letter in 'Python':
#     if letter == 't':
#         continue
#     if letter == 'o':
#         break
#     print('Current Letter : ' + letter)
    
# # 1.4 Nested loops
# rows = 6
# # outer loop
# for i in range(1, rows + 1):
#     # inner loop
#     for j in range(1, i + 1):
#         print("#", end=" ")
#     print('')
    
# 2 Getting started
# 2.1 The following fragment of code is written using a for loop. 
# Re-write it using a while loop.
# sum = 0
# for k in range(1, 10, 3):
#     sum = sum + k
# print(sum)

# rewriting using a while loop
# sum = 0
# k = 1
# while k < 10:
#     sum = sum + k
#     k = k + 3
# print(sum)

# 2.2 Show the output from the following code:
# for i in range(-10):
#     print(i * i)
# Output: No output

# total = 0
# for number in range(9, 20):
#     if number % 2 == 0 or number % 3 == 0:
#         total = total + 1
# print(total)

# Output: 7