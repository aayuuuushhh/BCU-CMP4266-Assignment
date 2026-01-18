# Exercise 3.1

# 1. Follow lecture 9 notes to create the Vehicle, Bus, Car classes and save them into
# lab9_vehicles.py.
# 2. For the Bus class:
# • Add a new public method get_route() which returns the following route (as
# string): New Street - Bullring - Moor Street - BCU.
# • Hint. For the following tasks, you might need to make changes to the Vehicle
# class. Please note, for what ever changes you would like to make, it should not
# change the behaviours of existing methods.
# • Update the constructor and set the state to "Not in use".
# • Override the move() method. It should set the state to the next stop and print out
# the following message: "The bus was at {previous_stop} and is
# moving to {next_stop}. ".
# 1. E.g., the bus will be at New Street at the beginning. When move() is
# called, it should print out: "The bus was at New Street and is
# moving to Bullring.".
# 2. Once the move() method is call, the bus will move to the next stop.
# 3. If the bus is at the final stop BCU and move() is called, it should print out
# this message instead: I am finished for today!.
# • Override the stop() method. It will no long change the state but only print out a
# message:
# "I am a non-stop bus."

class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model
        self._state = "stopped"
    
    def move(self):
        print("I am moving!")
        self._state = "moving"

    def stop(self):
        print("I have stopped.")
        self._state = "stopped"

    def get_make(self):
        return self._make
    
    def get_model(self):
        return self._model
    
    def get_state(self):
        return self._state
    
    def __str__(self):
        return f"{self.get_make()} {self.get_model()} is {self.get_state()}"
    
class Bus(Vehicle):
    def __init__(self, make, model, decks=1):
        Vehicle.__init__(self, make, model)
        self._decks_no = decks
        self.route = ["New Street", "Bullring", "Moor Street", "BCU"]
        self._state = "stoppped"
        self.current_stop = 0
    
    def get_route(self):
        return " - ".join(self.route)
    
    def move(self):
        if self.current_stop < len(self.route) - 1:
            previous_stop = self.current_stop
            self.current_stop += 1
            next_stop = self.route[self.current_stop]
            print(f"The bus was at {previous_stop} and is moving to {next_stop}.")
        else:
            print("I am finished for today!")
        
    def stop(self):
        print("I am a non-stop bus.")

