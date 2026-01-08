# 5.2 Write a program that get two lists as input and check if they have at least one common
# member.

def have_common_num(list1, list2):
    for item in list1:
        if item in list2:
            return True
        return False
list1 = input("Enter the first list:").split()
list2 = input("Enter the second list:").split()

if have_common_num(list1, list2):
    print("The lists have at least one common member.")
else:
    print("The lists have no common members.")