class Student:
    name="Bhanu"
    age=25
s1=Student()
print(s1.name)
print(s1.age)

class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
E1=Employee("Bhanu", 22)
print(E1.name, E1.age)