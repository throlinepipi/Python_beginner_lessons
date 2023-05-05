'''
list -- mutability
'''

mylist = ["Hello", "Welcome"]
print(mylist)
print(type(mylist))

x = "Hello, Welcome from Myanmar"
l = x.split()
print(l)
print(type(x))
print(type(l))

m = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(m[2:6:3])

multilist = [['Dog','Terrier','Royal',1],['Cat','Scottish',2]]
print(multilist[0][3])
print(multilist[1][0])