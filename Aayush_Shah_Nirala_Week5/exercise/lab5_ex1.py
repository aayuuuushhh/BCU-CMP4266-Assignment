# Create a script named lab5_ex1.py.
#  Before attempting this task, make sure you have tried all the codes from the lecture notes
# if you are new to Python programming.

def create_list():
    return ['PlayStation', 'Xbox', 'Steam', 'iOS','Google Play']

def get_info(my_list):
    return (my_list[0], my_list[-2], len(my_list))

def get_partial(my_list):
    return my_list[1:4]

def get_last_three(my_list):
    return my_list[-3:][::-1]

def double_list(my_list):
    return my_list + my_list

def amend(my_list):
    new_list = my_list.copy()
    new_list[1] = "None"

    new_list.append("Bye")
    
    return new_list

if __name__ == "__main__":
    test_list = create_list()
    print(test_list)
    print(get_info(test_list))
    print(get_partial(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))
