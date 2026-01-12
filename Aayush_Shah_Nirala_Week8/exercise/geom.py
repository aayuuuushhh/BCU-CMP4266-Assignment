# 5.1 The archive contains geometry module (i.e. geom.py) that contains two classes, Coordinate and
# Rectangle. The Coordinate class models a geometric point by representing the x and y coordinates of the
# point. The rectangle class models a rectangle by accepting the top left point and bottom right point of a
# rectangle. In your test function you need to create instances of two points by using the coordinate class and
# then create an instance of a rectangle by using the two points. Your test function then should call different
# methods of the rectangle and points to test those.

class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x  
    
    def get_y(self):
        return self.y
    
    def display(self):
        print(f"Coordinate: ({self.x}, {self.y})")

class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def width(self):
        return self.bottom_right.get_x() - self.top_left.get_x()

    def height(self):
        return self.bottom_right.get_y() - self.top_left.get_y()

    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return 2 * (self.width() + self.height())

    def display(self):
        print("Rectangle:")
        print("Top Left : ", end="")
        self.top_left.display()
        print("Bottom Right : ", end="")
        self.bottom_right.display()
        