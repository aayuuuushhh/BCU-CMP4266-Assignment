class Customer:
    def __init__(self, cID, first_name, second_name, address, balance):
        # todo1
        self._cID = cID
        self._first_name = first_name
        self._second_name = second_name
        self._address = address
        self._balance = balance
        
    def get_cID(self):
        # todo2
        return self._cID
    
    def set_cID(self, c_ID):
        # todo3
        self._cID = c_ID

    def get_first_name(self):
        # todo4
        return self._first_name
    
    def set_(self, f_name):
        # todo5
        self._first_name = f_name
    
    def get_second_name(self):
        # todo6
        return self._second_name
    
    def set_second_name(self, s_name):
        # todo7
        self._second_name = s_name

    def get_address(self):
        return self._address
    def set_address(self, addObj):
        self.__address = addObj

    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        self._balance = value

    def deposite(self, value):
        self._balance += value
    
    def withdraw(self, value):
        self._balance -= value
    
    def check_balance(self):
        return self._balance

    def __str__(self):
        return f"{self._cID},{self._first_name},{self._second_name},{self._address},{self._balance}"

class Address:
    # todo8
    def __init__(self, number, street, town, post_code):
        self._number = number
        self._street = street
        self._town = town
        self._post_code = post_code

    def get_number(self):
        return self._number
    
    def set_number(self, value):
        self._number = value

    def get_street(self):
        return self._street
    
    def set_street(self, value):
        self._street = value

    def get_town(self):
        return self._town
    
    def set_town(self, value):
        self._town = value

    def get_post_code(self):
        return self._post_code
    
    def set_post_code(self, value):
        self._post_code = value

    def change_address(self, new_address):
        self._number = new_address.get_number()
        self._street = new_address.get_street()
        self._town = new_address.get_town()
        self._post_code = new_address.get_post_code
    
    def __str__(self):
        return f"{self._number},{self._street},{self._town},{self._post_code}"
    
    
def new_customer():
    cid = int(input("Enter customer id number:"))
    f_name = input("Enter first name:")
    s_name = input("Enter second name:")
    adres = input("Enter address (number, street, town, postCode): ")
    while len(adres.split(",")) != 4:
        adres = input("Please re-enter address (number, street, town, postCode): ")
        a = adres.split(",")
        print(a)
        balance = float(input("Enter balance:"))
        # todo9
        addr_obj = Address(a[0], a[1], a[2], a[3])
        return Customer(cid, f_name, s_name, addr_obj, balance)
    
def save_cRecords(lst):
    # todo10
    try:
        with open("CustomerList.txt", "w") as f:
            for c in lst:
                f.write(str(c)+"\n")
            return True
    except Exception as e:
        print("Error saving records:", e)
    return False

def read_customerRecords():
    # todo11
    customers = []
    try:
        with open("CustomerList.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 8:
                    cid, fname, sname, number, street, town, post_code, balance = (
                        parts[0],
                        parts[1],
                        parts[2],
                        parts[3],
                        parts[4],
                        parts[5],
                        parts[6],
                        float(parts[7]),
                    )
                    addr = Address(number, street, town, post_code)
                    customers.append(Customer(cid, fname, sname, addr, balance))
    except FileNotFoundError:
        print("CustomerList.txt not found.")
    return customers

                    
if __name__ == "__main__":
    c1 = Customer("12A", "Rea", "Koci", Address("42", "Curzon Street", "Birmingham", "B4 2SU"), 888)
    c2 = Customer("11A", "Liora", "Koci", Address("42b", "Curzon Street2", "Birmingham2", "B4 2SU"), 33)

    save_cRecords([c1, c2])

    customers = read_customerRecords()   
    for c in customers:
        print(c.get_cID(), c.get_first_name(), c.get_second_name(), c.get_balance())
