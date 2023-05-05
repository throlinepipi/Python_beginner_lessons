'''
optional block

Syntax:
try:
     risky code
except:
    handling code
finally:
    clean_up code

control flow of try-except-finally:
try:
        statement-a
        statement-b
        statement-c
except:
         statement-d
finally:
         statement-e
         statement-f

case 1 -- When there is no exception raised then statement a, b, c, e , f  will terminate normally.
case 2 -- When there is an exception raised in statement-b and its associated except block matches,then statement a, d, e , f  will terminate normally.
case 3 -- When there is an exception raised in statement-b and its associated except block does not  match,,then statement a ,e will terminate normally.
case 4 -- When there is an exception raised in statement-d, then it will always terminate abnormally but before terminating the finally block will be processed.
case 5 -- When an exception is raised at statement-e and statement-f then it will terminate abnormally.
'''

#Case 1: When no exception occurs
try:
    print("try")
except:
    print("except")
finally:
    print("finally")

#Case 2: When an exception is occurred but is handled
try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")

#Case 3: When an exception is occurred but is not handled
try:
    print("try")
    print(10/0)
except NameError:
    print("except")
finally:
    print("finally")