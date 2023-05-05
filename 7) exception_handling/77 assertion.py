'''
Syntax
assert expression [,arguments]

AssertionError is not handled by the program, the program will be terminated.
'''

#Write a program to calculate the square of any number using an assert command.

def funn(b):
    return b ** b
assert funn(5) == 25, "Square of 5: 25"
print(funn(5))

def fun(a):
    return a * a
assert fun(5) == 25, "Square of 5: 25"
print(fun(5))