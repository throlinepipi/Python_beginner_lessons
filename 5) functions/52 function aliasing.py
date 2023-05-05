'''
to give another name to an existing function
'''

def myFunc1(n):
    print(n)
temp = myFunc1

print(id(myFunc1)) #my_function || myFunction || myfunction
print(id(temp))

temp('YMTK')
myFunc1('YMTK')

del myFunc1
temp('YMTK')
myFunc1('YMTK')
