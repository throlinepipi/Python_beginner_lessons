#integer, float, complex
a = 10j+0B10
print (a)
print (type (a))

#boolean
b = True
print (b)
print (type (b))

#string
c = "1"
print (c)
print (type(c))

#bytes
x1 = [3, 6, 8, 10]
x2 = bytes(x1)
print(type(x2))
print(x2[0])
print(x2[-1])
for i in x2:
    print(i)

# bytearray()

#none data type
def m1():
    x = 10
print (m1())

#binary
print(bin(30))

#octal
print (oct(30))

#hexadecimal
print(hex(30))