'''
def m1(x,y): #x,y are formal arguments

m1(11,22) #11,22 are actual arguments

positional arguments -- passed to the function at a proper positional order
keyword argument
'''

def m1(a,b):
    print(a/b)
m1(20,5)
m1(5,20)

m1(b=20,a=5) #keyword argument

def p1(*c):
    s=0
    for q1 in c:
        s=s+q1
    print("Addition=",s)

p1()
p1(10)
p1(2,3) #variable length argument
p1(2,3,4) #variable length argument


