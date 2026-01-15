def add(a,b):
    print(a+b)

def sub(a,b):
    return a-b, a
add(10,20)
print(sub(100, 20))

def hello(Greeting = "Hello", name= "World"):
    print('%s,%s'%(Greeting, name))
hello()

def print_params(*params):
    print(params)
print_params("testing")
print_params(1,2)

def print_params1(**params):
    print(params)
print_params1(x=1,y=2)
