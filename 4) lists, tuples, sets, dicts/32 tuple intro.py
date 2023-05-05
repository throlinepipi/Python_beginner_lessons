'''
special-valued tuple -- must terminate with a comma

accessing elements -- using index, slice operator

concatenation operator and multiplication operators
'''

tup1 = 30,40,50,60
print(tup1)
print(type(tup1))
print(tup1[2])
print(tup1[1:4:2])

tup2 =( 30,40,50,60)
print(tup2)
print(type(tup2))

tup3 = ()
print(tup3)
print(type(tup3))

specTup = (40)
print(type(specTup))
specTup = (40,)
print(type(specTup))