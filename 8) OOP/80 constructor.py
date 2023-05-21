'''
The _init_() method is automatically executed when an object of a class is created.
The method is useful to declare and initialize the instance variables.
The constructor is only executed once per object and at least one argument has to be provided
PVM will provide the default constructor if the user does not provide the constructor
'''

class A:
    def __init__(self):
        print("Constructor")

    def m1(self):
        print("Method")


a= A()
a.m1()

class B:
    '''''Information here'''
    def __init__(self,a,b):
        self.n = a
        self.r = b

    def m2 (self):
        print("My name is {}\nMy age is {}".format(self.n,self.r))

b = B("Su Su",19)
b.m2()