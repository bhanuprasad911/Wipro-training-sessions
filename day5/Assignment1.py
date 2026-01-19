#1. Create a base class Vehicle with a method start()
class Vehicle:
    #3. Add a class variable to track the number of vehicles created
    created_vehicles = 0
    def __init__(self, name):
        self.name = name
        Vehicle.created_vehicles+=1
        
    def start(self):
        print(f"{self.name}'s engine started")
# 2. Create a derived class Car that inherits from Vehicle
class Car(Vehicle):
    def horn(self):
        print(f"{self.name} is sounding poom..!!, poom..!!")

virtus = Car("Virtus")
virtus.start()
virtus.horn()

print(f"Total vehicles: {Vehicle.created_vehicles}") #Number of vehicle objects created

# 4. Demonstrate single inheritance and multilevel inheritance with appropriate classes
#Single Inheritance

print("------------------Single Inheritance-------------------")
class Calculator:
    
    def add(self, Number_1, Number_2):
        print(Number_1+Number_2)
        
    def sub(self, Number_1, Number_2):
        print(Number_1-Number_2)
        
class extendedCalculator(Calculator):
    
    def mul(self, Number_1, Number_2):
        print(Number_1*Number_2) 
        
    def div(self, Number_1, Number_2):
        print(Number_1//Number_2)  
    
calci=extendedCalculator()
calci.add(1,2)
calci.sub(2,1)
calci.mul(3,2)
calci.div(4,2)   

#Multilevel inheritance
print("------------------Multilevel inheritance-------------------")  
class Bhanu:
    def show1(self):
        print("Bhanu")
class Srujan(Bhanu):
    def show2(self):
        print("Srujan")
class Sri(Srujan):
    def show3(self):
        print("Sri")

friends = Sri()
friends.show3()
friends.show2()
friends.show1()