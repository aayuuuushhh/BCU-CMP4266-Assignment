# 5.3 Create a Person class with the following features:
# a. in the method (__init__) the name attribute (mandatory) and the age attribute (optional, to be set
# equal to -1 by default) must be defined
# b. it contains a method, called hello, which:
# 1. receives the name of the friend you want to greet as a mandatory parameter
# 2. converts the name of the friend to upper case
# 3. prints the following message: Hello FRIEND, I am XXX and I’m YY years old (the last part
# of the sentence must be omitted if the age is not defined, i.e. it is equal to -1)

class Person:
    def __init__(self, name, age=-1):
        self.name = name
        self.age = age

    def hello(self, friend_name):
        friend_name= friend_name.upper()
        if self.age == -1:
            print(f"Hello {friend_name}, I am {self.name}.")
        else:
            print(f"Hello {friend_name}, I am {self.name} and I'm {self.age} years old.")

# Example usages
man_1 = Person("Al", 31)
girl_1 = Person("Wanda")

man_1.hello("Jack")
girl_1.hello("Jack")