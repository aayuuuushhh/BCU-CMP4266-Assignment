from lab9_vehicles import Vehicle, Bus


def main():
    v1 = Vehicle("BMW", "Z3")
    print(v1)
    v1.move()
    print(v1)
    v1.stop()
    print(v1)

    b1 = Bus("Mercedes", "1")   
    print(f"Route: {b1.get_route()}")
    print(f"Initial bus state: {b1.get_state()}")
    b1.move()
    print(f"Bus state: {b1.get_state()}")
    b1.move()
    print(f"Bus state: {b1.get_state()}")
    b1.move()
    print(f"Bus state: {b1.get_state()}")
    b1.move()
    b1.stop()

if __name__ == "__main__":
    main()

