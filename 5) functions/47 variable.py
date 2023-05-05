x = 15 #global variable
def a1():
    y = 10
    print(x)
    print(y) #local variable
def a2():
    print(x)
    print(y)

a1()
a2()