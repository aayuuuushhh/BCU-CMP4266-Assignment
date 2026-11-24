# 5.2 Write a Rectangle class in Python language, allowing you to build a rectangle with length and width
# attributes. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to
# calculate the area of the rectangle. Create a method display() that display the length, width, perimeter and
# area of an object created using an instantiation on rectangle class.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")
# Example usages
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    rect.display()