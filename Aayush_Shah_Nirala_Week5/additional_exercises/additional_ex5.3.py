# 5.3 Write a function named find_greater(x_list, x_num) that expects a list of
# numbers and a number. It returns a new list consisting of all the numbers in the list
# that are greater than the number x_num. For example:
# >>> find_greater( [11, 35, 46, 2, 104, 43, 41,8], 10 )
# [11, 35, 46, 104, 43, 41]

def find_greater(x_list, x_num):
    result = []
    for num in x_list:
        if num > x_num:
            result.append(num)
    return result
print(find_greater([11, 35, 46, 2, 104, 43, 41, 8], 10))
