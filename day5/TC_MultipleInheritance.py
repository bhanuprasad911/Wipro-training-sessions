class A:
    def showA(self):
        print("A")
class B:
    def showB(self):
        print("B")
    def showA(self):
        print("A in b")

class C(B, A):
    pass
c = C()
c.showA()
c.showB()

