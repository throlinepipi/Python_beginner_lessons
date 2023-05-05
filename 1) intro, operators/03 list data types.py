#list[]
m = [11, 11.6, "python", 12]
print (m)
print(m[0])
print(m[-1])
print(m[1:3])
m[0] = 300
print(m)

#list slicing
s = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i']
print (s[:]) #items beginning to end
print (s[1:4])
print(s[4:])

#increase, decrease list
m1 = [11, 22, 33, 44]
m1.append("python")
print (m1)
m1.remove(22)
print (m1)
m2 = m1*2
print (m2)

