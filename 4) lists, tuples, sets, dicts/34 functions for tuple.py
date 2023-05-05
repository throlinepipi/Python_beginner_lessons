'''
1 -- len()
2 -- count()
3 -- index()
4 -- sorted()
5 -- min(), max()
6 -- cmp() -- compares the elements of both tuples -- only in 2 Python2, Python3 doesn't support **
 7 -- tuple comprehsion -- python doesn't support -- will produce the generator object
'''

myTuple = (20, 1, 2, 90, 87)
print(min(myTuple))
print(max(myTuple))

tup1 = 10,20,30
tup2 = 40,50,60
#print(cmp(tup1,tup2))

t = (a**2 for a in range(1,5)) #1,2,3,4 -- 1,4,9,16
print(type(t))