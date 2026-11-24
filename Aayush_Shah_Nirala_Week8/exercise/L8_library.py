class BankAccount:
    def __init__(self, acc_number,balance=0):
        self.acc_number = acc_number
        self._balance = balance

    def get_account(self):
            return self.acc_number
        
    def get_balance(self):
            return self._balance
        
    def deposit(self, amount):
            self._balance += amount  

    def withdraw(self, amount):
            if amount <= self._balance:
                self._balance -= amount
            else:
                print("Insufficient amount!")

    def transfer(self, amount, acc):
            if amount <= self._balance:
                self._balance -= amount
                acc.deposit(amount)
        