'''
used to list all the available members of the specified module.

dir(module_name)
'''

import calculator
print(dir(calculator))

print(__builtins__)

#Special variables
def m1():
    if __name__ == '__main__':
         print("Run program part")
    else:
        print("Other program runs as module")

m1()