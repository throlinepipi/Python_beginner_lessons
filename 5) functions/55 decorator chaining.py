'''
declare various decorators for similar functions
'''

def decor1(func):
    def func1():
        f = func()
        return  f*f
    return func1

def decor2(func):
    def func1():
        f = func()
        return f
    return func1

@decor1
@decor2

def func2():
    return 5
print(func2())