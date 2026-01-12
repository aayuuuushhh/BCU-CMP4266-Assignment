# 5.4 Create in Python the program Exercise13.8.py containing the tuple: tuplex = (4, 9, ['a','b'], 123.45, 0)
# At the end of the program the tuple must be changed in the following way, applying the changes in the exact
# order given below (remember: tuples cannot be modified, they can only be reassigned, thus a list must be
# used to perform the transition from the initial tuple to the final one):

# 1. add value 7 at the end of the sequence
# 2. add tuple (10, 100, 1000) in the fourth position
# 3. add the string "bob" stored in the position with index 2
# 4. add number 3.5 in first position
# 5. add False in position -1
# 6. delete value 9
# 7. delete the element stored in the position with index -4

# Display each change on the screen (printing each time the intermediate list) and, at last, print the final tuple
# tuplex.

def main():
    tuplex = (4, 9 , ['a','b'], 123.45, 0)
    print("Initial tuple:", tuplex)

    temp_list = list(tuplex)
    print("Converted to list:", temp_list)

    temp_list.append(7)
    print("After adding 7:", temp_list)

    temp_list.insert(3, (10, 100, 1000))
    print("After adding (10, 100, 1000) at index 3:", temp_list)

    temp_list[2].append("bob")
    print("After adding bob at index 2:", temp_list)

    temp_list.insert(0, 3.5)
    print("After adding 3.5 at index 0:", temp_list)

    temp_list.insert(-1, False)
    print("After adding False at index -1:", temp_list)

    temp_list.remove(9)
    print("After removing 9:", temp_list)

    del temp_list[-4]
    print("After deleting element at the end:", temp_list)

    tuplex = tuple(temp_list)
    print("Final tuple:", tuplex)

if __name__ == "__main__":
    main()
