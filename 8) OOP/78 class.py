'''
Syntax
class class_name:
            ''document string''

document string -- shows the description of a class
string is optional in the doc class
doc string -- can be accessed bt the following techniques:
1)  print (class_name.__doc__)
2)  help (class_name)

animal
color
species
gender
'''

# Create a simple class in Python.
class A:
    '''''Document Information'''
print(A.__doc__)
help(A)

# Create a simple Python class and an object of the class
class Python:
    '''''Python programming approach '''
    def __init__(self):
        self.n ="Hello"
        self.r = 40
    def m1(self):
        print("Name: " , self.n)
        print("Size: " , self.r)
p = Python()
print(p.m1())
