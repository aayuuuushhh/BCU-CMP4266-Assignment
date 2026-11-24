# 3.1 Write a menu-driven program that allows the user to make transactions to a bank account. The options of the menu are:  Option 1: Make a Deposit  Option 2: Make a Withdrawal  Option 3: Obtain a Balance  Option 4: Quit
# - First the program asks the user for his/her name.
# - The user can make many interactions as they wish until they decide to quit by pressing Q or q from the keyboard. (Hint: while loop)
# - Assume that the account initially has a balance of £1000.
# - If the user tries to withdraw an amount more than the total balance, the program should print ‘It is not possible to withdraw beyond the account balance.
# - Ask the user to select from the menu options.
# - Make sure the user enters a proper menu number.
# - If option one is selected, allow the addition of funds to the balance.
# - If option two is selected, subtract the amount from the balance.
# - If option three is selected, display the total balance of the checking account


print("*******WELCOME TO OUR BANK*******")
user_name = input("Please enter your name:")
balance = 1000
op = True

while op:
    print("\n Choose 1 for Deposit")
    print("Choose 2 for Withdraw")
    print("Choose 3 for Check Balance")
    print("Choose Q or q to Exit")
    
    choice = input("Please choose transactions:")
    if choice =="1":
        amount =float(input("Enter amount to deposit:"))
        balance += amount
        print("Deposited successfully.")
        print("New balance:", balance)
    elif choice =="2":
        amount = float(input("Enter amount to withdraw:"))
        if amount > balance:
            print("Sorry! It is not possible to withdraw beyond the account balance.")
        else:
            balance -= amount
            print("Withdrawal successful")
            print("New balance:",balance)
    elif choice == "3":
        print("Your current balance is:",balance)
        
    elif choice =="Q" or choice == "q":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        op = False
    else:
        print("Wrong transaction! Try again.")
            
        
    
    