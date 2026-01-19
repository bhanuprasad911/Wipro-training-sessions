# 1. Create a class Calculator that demonstrates method overriding

class Calculator:
    def calculate(seelf, a, b):
        print(a+b)
class advanceCalculator(Calculator):
    def calculate(self, a, b):
        print(a*b)

cal=Calculator()
cal.calculate(2,3)
cal2=advanceCalculator()
cal2.calculate(2,3)


# 3. Implement operator overloading by overloading the + operator to add two objects of a custom class

class number:
    def __init__(self, value):
        self.value=value
    def __add__(self, other):
        return (self.value+other.value)

number1=number(10)
number2=number(20)
print(number1+number2)

# 4. Demonstrate polymorphism using the same method name with different behaviors

class base:
    def behave(self):
        print("Behaves as a base class")

class derived(base):
    def behave(self):
        print("Behaves as a derived class")

obj = derived()
objbase = base()
objbase.behave()
obj.behave()
        