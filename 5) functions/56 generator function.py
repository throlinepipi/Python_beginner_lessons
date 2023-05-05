'''
simplifies the job of writing the iterators
'''

def genFunc():
    yield 'P'
    yield 'Q'
    yield 'R'

m = genFunc()
print(type(m))
print(next(m))
print(next(m))
print(next(m))
#print(next(m))

def method1(n):
    print("Numbers")
    while(n>0):
        yield n
        n = n-1
v1 = method1(4)
for i in v1:
    print(i)