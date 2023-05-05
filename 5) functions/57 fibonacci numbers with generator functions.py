'''
0 1 2 3 5 8 13 21
'''

def fib():
    x,y =0,1
    while True:
        yield x
        x,y = y,x+y
for f in fib():
    if f > 30:
        break
    print(f)