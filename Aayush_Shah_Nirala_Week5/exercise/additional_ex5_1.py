# 5.1 Create a function named print_full_pyramid(level, symbol), which takes two parameters: level and
# symbol.

def print_full_pyramid(level, symbol):
    for i in range(1,level + 1):
        spaces = ' ' * (level - i)
        symbols = (symbol + ' ') * i
        print(spaces + symbols.strip())
if __name__ == "__main__":
    # print_full_pyramid(6, "*")
    # print_full_pyramid(6,"#")
    # print_full_pyramid(9,"Hi")
    print_full_pyramid(4, "It's hard")