# 5.4 Write a function named sum(list_x, list_y) that expects two lists of numbers
# and returns a new list containing the sums of those lists' members. For example:
# >>> sum( [2,4,7],[1,2,3] ,[3, 6, 10])

def sum_lists(list_x, list_y):
    result = []
    for a, b in zip(list_x, list_y):
        result.append(a + b)
    return result

# example used
print(sum_lists([2, 4, 7], [3, 5, 9]))