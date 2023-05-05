'''
It gets executed only when the try block is free from exception.

Syntax
try:
        Risky code
except:
        execute when exception occurs
else:
        execute when no exception occurs
finally:
        always executes
'''

try:
    print("try")
except:
    print("except")
else:
    print("else")
finally:
    print("finally")

try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print("except")
else:
    print("else")
finally:
    print("finally")

