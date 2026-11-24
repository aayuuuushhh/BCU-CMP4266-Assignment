# 3.2 Create a Python program to manage the guest list for a party. The program should allow you to add guests,
# remove guests, and print the current guest list.

guest_list = []

def add_guest():
    name = input("Enter the name of the guest to add: ")
    guest_list.append(name)
    print(f"{name} has been added to the guest list.")
    
def remove_guest():
    name = input("Enter the name of the guest to remove: ")
    if name in guest_list:
        guest_list.remove(name)
        print(f"{name} has been removed from the guest list.")
    else:
        print(f"{name} is not no the guest list.")
    
def print_guest_list():
    if len(guest_list) == 0:
        print("Guest list is empty.")
    else:
        print("Current Guest List:")
        for guest in sorted(guest_list):
            print(guest)
            
while True:
    print("Options:")
    print("A - Add a guest")
    print("R - Remove a guest")
    print("P - Print a guest")
    print("Q - Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "A":
        add_guest()
    elif choice == "R":
        remove_guest()
    elif choice =="P":
        print_guest_list()
    elif choice == "Q":
        print("Total number of guests: ",len(guest_list))
        print("Goodbye! See you in the party!")
        break
    else:
        print("Invalid choice. Please choose a valid option (A,R,P or Q).")
