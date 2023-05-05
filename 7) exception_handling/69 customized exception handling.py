'''
Syntax:
try:
       risky code
except:
              handling the encountered exception

try:
      statement
except ExceptionName:
      statement


control flow of try-except:
try:
        statement-a
        statement-b
        statement-c
except:
         statement-d
         statement-e

case 1 -- When there is no exception raised then statement a, b, c, e will terminate normally.
case 2 -- When there is an exception raised in statement-b and its associated except block matches,then statement a, d, e will terminate normally.
case 3 -- When there is an exception raised in statement-b and its associated except block does not  match,,then statement-a will terminate normally.
case 4 -- When an exception is raised at statement-d and statement-e then it will terminate abnormally.
'''

#without try-except
print("First-1")
print(10/0)
print("Second-2")

#with try-except
print("First-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("Second-2")

#to print the exception information
try:
    print(10/0)
except ArithmeticError as zde:
    print("exception occurs:",zde)
