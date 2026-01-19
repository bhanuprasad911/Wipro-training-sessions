class parent:
    def parent1(self):
        print("Parent")
class child1(parent):
    def child1(self):
        print("child 1")
class child2(parent):
    def child2(self):
        print("Child 2")

c1 = child1()
c2 = child2()
c1.child1()
c1.parent1()
c2.parent1()
c2.child2()
