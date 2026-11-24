from L8_library import BankAccount

acc1 = BankAccount(101)
acc2 = BankAccount(102)

accounts = [acc1, acc2]

for acc in accounts:
    acc.deposit(100)

for acc in accounts:
    acc.withdraw(40)

print("Balances after withdrawal")
for acc in accounts:
    print(f"Account {acc.get_account()} balance: {acc.get_balance()}")

for acc in accounts:
    acc.deposit(20)

print("Balances after deposit")
for acc in accounts:
    print(f"Account {acc.get_account()} balance: {acc.get_balance()}")

acc2.transfer(20, acc1)
print("Balances after transfer")
for acc in accounts:
    print(f"Account {acc.get_account()} balance: {acc.get_balance()}")