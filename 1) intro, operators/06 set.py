#cannot be accessed using an index
s = {11, 22, 23, 24, 25, 26, 27, 28}
#print (s[0])
s.add(80)
print(s)
s.remove(11)
print(s)

# Frozenset -- immutable
x = {1, 2, 3, 4}
y = frozenset(x)
print (type(y))
#no add, remove