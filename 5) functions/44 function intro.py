'''
built-in functions

user-defined functions -- def funtion_name(parameters) // optional keyword -- return

local namespace
global namespace
built-in namespace
'''

def add(x,y):
    print(x+y)

add(4,5)

name1 = 5 #global namespace
def outer_fun():
    name2 = 6 #local namespace
    def inner_fun():
        name3 = 7 #inner local namespace