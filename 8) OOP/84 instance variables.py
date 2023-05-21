''''
The ones whose value varies from object-to-object.
For each object, a distinct copy of the instance variable will be produced.
Known as object level variables.

Declarations:
1) In the constructor by self keyword
2) In the instance method by self keyword
3) Outside the class by object reference variable

Accessing:
Within the class by the self variable
Outside the class by object reference

Deleting:
1) within the class: del self.variable_name
2) outside the class: del obje
 '''


#Declarations: In the constructor by self keyword
class A:
    def __init__(self):
        self.name = 'Parth'
        self.age = 23
a = A()
print (a.__dict__)

#Declarations: In the instance method by self keyword
class B:
    def __init__(self):
        self.a = 100
    def m1(self):
        self.b = 300
b1 = B()
b1.m1()
print(b1.__dict__)

#Declarations: Outside the class by object reference variable
class C:
    def __init__(self):
        self.c = 10
    def m2(self ):
        self.d = 20
c1 = C()
c1.m2()
c1.e = 30
print(c1.__dict__)

#Accessing
class D:
    def __init__(self):
        self.f = 3
        self.g = 4
    def m3(self):
        print(self.f)
        print(self.g)
d1 = D()
d1.m3()
print(d1.__dict__)