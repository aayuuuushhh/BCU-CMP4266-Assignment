# 5.1 Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel
# value to mark the end of the input. Once all of the values have been read your program should
# display them in reverse order.

def main():
    number = []
    while True:
        num = int(input("Enter an integer (0 to stop):"))
        if num == 0:
            break
        number.append(num)

    print("Numbers in reverse order are:")
    for n in reversed(number):
        print(n)

if __name__ == "__main__":
    main()