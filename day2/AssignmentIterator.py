#1. Create a custom iterator class that iterates over numbers from 1 to N

class numberIterator:
    def __init__(self, limit):
        self.limit=limit
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <=self.limit:
            value = self.current
            self.current+=1
            return value
        else:
            raise StopIteration
customIteration = numberIterator(100)
for i in customIteration:
    print(i)
    

#2Create a class Employee with attributes:
# name
# salary
# Implement a descriptor that:
# 1. Ensures salary is always a positive number
# 2. Raises a ValueError if a negative salary is assigned
# 3. Demonstrates the descriptor by creating multiple Employee objects

class positiveSalary:
    def __set_name__(self, owner, salary):
        self.public_salary = salary
        self.private_salary = '_'+salary
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_salary)
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.public_salary} should be a number")
        if value<0:
            raise ValueError(f"{self.public_salary} must be greater than 0")
        setattr(instance, self.private_salary, value)
class Employee:
    salary = positiveSalary()
    def __init__(self, name, salary):
        self.name=name;
        self.salary=salary
    def __repr__(self):
        return f"Employee(Name:{self.name}, salary:{self.salary})"

print("1. Creating valid employees:")
emp1 = Employee("Bhanu", 50000)
emp2 = Employee("Sravan", 60000)
print(emp1)
print(emp2)

print("\n2. Updating salary (Valid):")
emp1.salary = 55000
print(f"Bhanu's new salary: {emp1.salary}")
try:
    emp3 = Employee("Test", -1000)
    print(emp3)
except ValueError as e:
    print(f"Error caught: {e}")

try:
    emp1.salary = "High"
except TypeError as e:
    print(f"Error caught: {e}")
            