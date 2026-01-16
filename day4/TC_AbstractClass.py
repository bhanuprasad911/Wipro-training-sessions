from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class ExtendedShape(Shape):
    def area(self, length, width):
        print(length*width)
        print("Area method implemented")
s1 = ExtendedShape()
s1.area(2,4)