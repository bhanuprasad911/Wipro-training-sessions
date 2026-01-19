class A:
    def showA(self):
        print("A")
class B(A):
    def showB(self):
        print("B")
class c(B):
    def showC(self):
        print("C")

obj=c()
obj.showA()
obj.showB()
obj.showC()