# # Relationships between objects- Association
# class Student:
#     def __init__(self, name, student_number):
#         self.name = name
#         self.student_number = student_number
#         self.modules_list = []
    
#     def print_student_info(self):
#         print("Students name: %s" %self.name)
#         print("Students ID: %s" %self.student_number)
#         print("modules undertaken by the student:")
#         i = 0
#         for c in self.modules_list:
#             i += 1
#             print("%d %s" %(i,c.print_module_info()))

#     def enrol(self, module_running):
#         self.modules_list.append(module_running)

# class Module:

#     def __init__(self, module_title, module_credits, department):
#         self.module_title = module_title
#         self.credits = module_credits
#         self.department = department

#     def print_module_info(self):
#         return "%s, Credits: %s, Department: %s" %(self.module_title, self.credits, self.department)
    
# # create the module objects
# mo1 = Module("Computer Programming",20, "Cyber Security")
# mo2 = Module("Computer Systems", 20, "Digital Media")
# mo3 = Module("Networking fundamentals", 20, "Networking and Distributed Systems")

# # create the students objects
# st1 = Student("Adam","ID2324")
# st2 = Student("Olivia","ID995")

# # enroll student 1 in Computer Programming module and Networkung fundamentals
# st1.enrol(mo1)
# st2.enrol(mo3)

# # enroll student 1 in Computer Programming module and Networkung fundamentals
# st1.enrol(mo3)
# st2.enrol(mo2)

# # print all students information
# st1.print_student_info()
# print() #print empty line
# st2.print_student_info()


# 1.3 Inheritance

# class Person:
#     def __init__(self, name, phone_numer):
#         self.name = name
#         self.phone_number = phone_numer


#     def get_profile_info(self):
#         return "Name: %s, Phone number: %s" %(self.name, self.phone_number)
    
# class Student(Person):
#     def __init__(self, course, *args, **kwargs):
#         self.course = course
#         self.classes = []
#         super(). __init__(*args, **kwargs)

#     def enrol(self, module):
#         self.classes.append(module)

# class StaffMember(Person):
#     def __init__(self, *args, **kwargs):
#         self.courses = []
#         super().__init__(*args, **kwargs)

#     def administrator_for(self, module):
#         self.courses.append(module)

#     def get_salary(self):
#         return self.salary

# # example usage
# st1 = Student("Computer Science", "Aayush", "9800000000")
# print(st1.get_profile_info())
# st1.enrol("Python Programming")
# print(st1.classes)

# staff1 = StaffMember("Shah", "9811111111")
# staff1.administrator_for("AI Systems")
# print(staff1.get_profile_info())
# print(staff1.courses)


# Getting started
# 2.1 What will be output for the following code?
class A:
    def __init__(self, x= 3):
        self.x = x
        
class der(A):
    def __init__(self,y = 4):
        super().__init__()
        self.y = y

def main():
    obj = der()
    print(obj.x, obj.y)
main()

# Output: 3 4

# 2.2 What will be the output of the following code?
class Sports:
    def Play(self):
        print("Play Games")

    def showResult(self):
        print("Result of Sports")

class Study:
    def Exam(self):
        print("Appear to Exam")

    def showResult(self):
        print("Result of Exam")

class Student(Sports,Study):
    def show(self):
        self.Play()
        self.Exam()
        super().Exam()  # can call like this
        self.showResult()  # Left to Right Search in Parent Classes
        Study().showResult() # can call like this

S = Student()
S.show()

# output: Play Games
# Appear to Exam
# Appear to Exam
# Result of Sports
# Result of Exam