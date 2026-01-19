class Animal:
    def sound(self):
        print("Animals makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")

onbj =[Dog(), Cat()]
for i in onbj:
    i.sound()