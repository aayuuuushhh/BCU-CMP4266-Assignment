#5.4 Modify exercise 3.1
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def display_menu():
    print("Select an option:")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("q Quit")
def run_calculator():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/q): ")

        if choice == 'q':
            print("You selected q.")
            print("Bye!")
            break
        elif choice in ['1', '2', '3', '4']:
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number:"))

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
    
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error:cannot divide by 0.")
                else:
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")

        else:
            print("Error! Invalid choice.")

if __name__ == "__main__":
    run_calculator()