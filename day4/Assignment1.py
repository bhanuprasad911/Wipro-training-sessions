class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def display_details(self):
        print(f"Name:{self.name}, Roll No: {self.roll_no}")

S1 = Student("Bhanu", 101)
s2=Student("Sravan", 102)
S1.display_details()
s2.display_details()

