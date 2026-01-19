class Box:
    def __init__(self, value):
        self.value =value
    def __add__(self,other):
        return self.value+other.value
b1=Box(10)
b2=Box(20)
print(b1+b2)
        