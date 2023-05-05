'''
parenthesized tuple
'''

try:
    var1 = int(input("Enter Var-1: "))
    var2 = int(input("Enter Var-2: "))
    print(var1 / var2)
except (ZeroDivisionError, ValueError) as msg:
    print("Invalid", msg)