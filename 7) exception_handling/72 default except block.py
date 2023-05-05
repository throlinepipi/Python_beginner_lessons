'''
default except block can be used for handling any variety of exceptions
'''

try:
    var1= int(input("Enter Var-1: "))
    var2= int(input("Enter Var-2: "))
    print(var1/var2)
except ZeroDivisionError:
    print("division by zero")
except:
    print("Default exception")