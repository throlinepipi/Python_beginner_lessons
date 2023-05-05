'''
forward direction = find(), index()
backward direction = rfind(), rindex()
p.find(.substring)/ p.rfind(.substring) -- returns index of first occurrence// return -1 if no such occurrence2
index() / rindex() -- if the mention substring is not available, then the ValueError is raised
'''
from turtle import position

p = "Paragraph on importance of good reading habits"
print(p.find("on"))
print(p.find("w"))
print(p.find('i',7,15))
print(p.find('b',7,15))
print(p.find('b'))

str1 = input("Enter main string: ")
substring = input("Enter substring: ")
try:
    n = str1.index(substring)
except ValueError:
    print("Substring is not matching.")
else:
    print("Substring matches")

a = input("Enter main string: ") #vimalv
b = input("Enter substring: ") #v
flag = False
position = -1
m = len(a)
print(m) #6
while True:
    position = a.find(b, position+1,m) #('v',0,6)
    if position== -1:
        break
    print("Position is ", position)
    flag = True
if flag == False:
    print ("sorry")