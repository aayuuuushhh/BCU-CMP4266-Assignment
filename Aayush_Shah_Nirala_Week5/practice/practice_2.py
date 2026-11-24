# 2. Getting started
# 2.1 show the output from the following code:
a = [5, 10, 15, 20, 25]
def first_last(input_list):
    return [input_list[0], input_list[-1]]
print(first_last(a))

# 2.2 Explain what the following code does.
dic = {'Ogerta' : "2003",
'Sara' : "1809",
'Moad' : "1912",
'Aliyuda' : "2003",
'Kurtis' : "9834",
'ALbaarini' : "1990",
'Abdel' : "2001",
'Syed' : "1996",
}
username = input("Enter username :- ")

if username in dic :
    password = input("Enter password :- ")
    if dic[username] == password :
        print ("You are now logged into the system.")
    else :
        print ("Invalid password.")
else :
    print ("You are not valid user.")
    
"""
This code is a simple login system using a Python dictionary as a user database. The dictionary stores usernames as
keys and their corresponding passwords as values. When the program runs, it first asks the user to enter a username.
If the username exists in the dictionary, it then prompts for a password. If the entered password matches the stored 
password for that username, the program prints a success message: "You are now logged into the system." If the password
is incorrect, it prints "Invalid password." If the username is not found in the dictionary at all, it prints 
"You are not valid user." In short, it checks both username validity and password correctness before granting access.
"""