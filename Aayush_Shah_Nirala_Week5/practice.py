# #1. Tuples, Collection Types, Lists, Dictionaries
# # 1.1 Tuples, type evaluation and comparison
# import math
# print(type(("a",10.5)))
# print(type((0)))
# print(type((0,)))
# print(type(()))
# print(type("hello"))
# print(type(10.5))
# print(type(math.pi)==type(10.5))
# print(type(10.5)==type("hello"))

# # 1.2 Lists
# print(type([]))
# print(type([2,4]))
# print(type(['hello',10.5]))

# # 1.2.1 Manipulating a list
# l = [2,3]
# l.append(5)
# print(l)
# l.insert(0,1)
# print(l)
# l.insert(2,4)
# print(l)
# print(l[1])
# print(l[4])

# # 1.2.2 Measuring length, sorting and reversing a list
# print(len(l))
# print(len("this"))
# print(len((0,)))

# l.reverse()
# print(l)

# l.sort()
# print(l)

# del l[1]
# print(l)

# del l[3]
# print(l)

# # 1.2.3 Generating a list using the list() and range() function
# print(list(range(1,10)))
# print(list(range(1,20,2)))
# print(list(range(3,20,3)))
# print(list(range(20,0,-1)))

# # 1.2.4 Slicing a list
# a = list(range(1,11))
# print(a)
# print(a[3:5])
# print(a[:])
# print(a[:6])
# print(a[6:])

# b = a
# c = a[:]
# a.remove(3)
# print(a)
# print(b)
# print(c)

# 1.3 Dictionaries
# 1.3.6 When we iterate through a dictionary using a for loop, we actually iterate over the keys:
d = { "key1":1, "key2":2, "key3":1, "key4":3, "key5":1, "key6":4, "key7":2 }
for k in d :
    print("key=", k, " value=", d[k], sep="")

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