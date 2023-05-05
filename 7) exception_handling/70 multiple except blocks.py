'''
try:
      operations
      .....
except Exception1:
    If Exception1 occurs, this block will process.
except Exception2:
   If Exception2 occurs, this block will process.
   .......
else:
   If no execution, this block will process.
'''
try:
    var1= int(input("Enter Var-1: "))
    var2= int(input("Enter Var-2: "))
    print(var1/var2)
except ArithmeticError:
    print("Arithmetic error")
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("Only integer")