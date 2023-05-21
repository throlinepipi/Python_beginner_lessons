"""
Object is the physical existence of a class.
Reference variable is the one that is used to refer to the object, method, and its properties.

Syntax
ref_variable = class_name()
p = Stdnt()
"""
class A:
    def __init__(self, n):
        self.n = n
    def m1(self):
        print("Name:", self.n)
a = A("Shadow")
a.m1()

def hello(a,b):
    print(a+b)

