# exercise 3.2
def view_contacts(contacts):
    print("------ View_contacts ------")
    for i, (name, num) in enumerate(contacts, start=1):
       print(f"{i}. {name} - {num}")

def add_contact(contacts):
    print("------ add_contact ------")
    name = input("Enter contact name: ")
    num = input("Enter contact number: ")
    contacts.append((name, num))
    print(f"Contact {name} added.")

def delete_contact(contacts):
    print("-----delete_contacts-----")
    view_contacts(contacts)
    if len(contacts) == 0:
        return
    
    try:
        choice = int(input("Enter the contact number to delete: "))
        if 1 <= choice <= len(contacts):
            removed_contact = contacts.pop(choice - 1)
            print(f"Contact {removed_contact[0]} deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main(contacts=[("Stish","123"),("Rita","321")]):
         while True:
            print("\nChoose an option:")
            print("v - View contacts")
            print("a - Add contact")
            print("d - Delete contact")
            print("q - Quit")
            choice = input("Your choice: ").lower()

            if choice == 'v':
                view_contacts(contacts)
            elif choice == 'a':
                add_contact(contacts)
            elif choice == 'd':
                delete_contact(contacts)
            elif choice == 'q':
                print("-----Goodbye!-----")
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()