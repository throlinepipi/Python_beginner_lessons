'''
 1 -- to get the information of list -- len(), count(), index()
2 --  manipulating elements of a list -- append(), insert(), extend(), remove(), pop()
3 -- oredering elements of a list -- reverse(), sort() #same data type
 4 --aliasing and cloning of list objects -- slice operator, copy()
 5 -- using mathematical operators for  list objects -- +, *
 6 -- comparing lsit objects -- relational operators
 7 -- membership operators -- in, not in
 8 -- clear function -- clear()
 9 -- nested list
 10 -- list comprehensions -- list = [expression in list if condition)
'''

mylist = [11,22,33,44,44, 22]

print(len(mylist))
print(mylist.count(44))
print(mylist.index(33))

mylist.append("hello")
print(mylist)
mylist.insert(2,"Myanmar")
print(mylist)
mysecondList = [99, 88]
mylist.extend(mysecondList)
print(mylist)
mylist.remove(88)
print(mylist)
mylist.pop()
print(mylist)

mylist.reverse()
print(mylist)
listNum = [11,23,12,4,23,2,6]
print(listNum)
listNum.sort()
print(listNum)

aliaNum = listNum[:]
print(aliaNum)
copyNum = listNum.copy()
print(copyNum)

addNum = aliaNum + copyNum
print(addNum)
repNum = aliaNum * 3
print(repNum)

print (aliaNum == copyNum)
print(addNum == repNum)
print (aliaNum != copyNum)

print(2 in aliaNum)
print(100 in aliaNum)
print(100 not in aliaNum)

print(repNum)
repNum.clear()
print(repNum)

nestlist = [1,2,[3,4]]
print(nestlist[2][0])

#print different vowels avaible in the given word
vowels = ['a', 'e', 'i', 'o', 'u']
w = input("Enter the String: ")
f = []
for i in w:
    if i in vowels:
        if i not in f:
            f.append(i)
print(f)
print("Vowels ",w, "is",len(f))