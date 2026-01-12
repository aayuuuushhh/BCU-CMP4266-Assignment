from geom import coordinate, Rectangle
def test():
    p1 = coordinate(2,5)
    p2 = coordinate(8,1)

    rect = Rectangle(p1, p2)

    rect.display()
    print(f"Width: {rect.width()}")
    print(f"Height: {rect.height()}")
    print(f"Area: {rect.area()}")

if __name__ == "__main__":
    test()