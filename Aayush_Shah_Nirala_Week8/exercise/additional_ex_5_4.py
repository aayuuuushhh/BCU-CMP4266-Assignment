# 5.4 Create a class Person with the following features:

# a. In the method (__init__) the name, surname, birthdate, address, telephone and email.
# b. Calculate the age of the person based on the current date (import datetime)

from datetime import datetime

class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def calculate_age(self):
       birth = datetime.strptime(self.birthdate, "%Y-%m-%d")
       today = datetime.today()
       age = today.year - birth.year
       if (today.month, today.day) < (birth.month, birth.day):
           age -= 1
           return age
       
    def display_info(self):
        print(f"Name: {self.name} {self.surname}")
        print(f"Birthdate: {self.birthdate}")
        print(f"Address: {self.address}")
        print(f"Telephone: {self.telephone}")
        print(f"Email: {self.email}")
        print(f"Age: {self.calculate_age()}")

# Example usage
if __name__ == "__main__":
    p = Person(
        name = "Aayush",
        surname = "Shah",
        birthdate = "2005-10-04",
        address  = "Kathmandu, Nepal",
        telephone = "1234567890",
        email = "aayush@gmail.com"
    )

    p.display_info()