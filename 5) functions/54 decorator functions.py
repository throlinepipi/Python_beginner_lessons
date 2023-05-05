'''
used to add new functionalities to the existing code
meta-programming
'''

def decor(fun):
    def func1(n):
        if n == "Myanmar":
            print("This is Myanmar")
        else:
            fun(n)
    return func1
#@decor

def func2(n):
    print(n,"Welcome")

d = decor(func2)

func2("Italy") #decorator wont be excuted
func2("Myanmar") #decorator wont be excuted
d("Italy") #decorator will be excuted
d("Myanmar") #decorator will be excuted
