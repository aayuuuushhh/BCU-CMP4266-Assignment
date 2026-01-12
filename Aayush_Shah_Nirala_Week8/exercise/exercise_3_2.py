# exercise 3.2
class BMI:
    def __init__(self):
        self.weight = 0
        self.height = 0

    def set_weight(self,w):
        self.weight = w 
    
    def set_height(self,h):
        self.height = h

    def __call_BMI(self):
        if self.height <= 0:
            return 0
        return self.weight / (self.height ** 2)
    
    def display_BMI(self):
        bmi = self.__call_BMI()
        print(f"BMI is: {bmi:.2f}")

if __name__ == "__main__":
    person = BMI()
    person.set_weight(70)  
    person.set_height(1.9) 
    person.display_BMI()