'''
takes a function and a list of all items as input
a new list as output that possess the list of items given by the defined function

map(function,seq)
map(lambda p,q:p*q,p1,q2 where p is from p1 and q is from q2
'''

#without lambda
list1 = [11,22,33,44]
def function1(a):
    return 2*a
list2 = list(map(function1,list1))
print (list2)

#with lambda
list3=[11,22,33,44]
list4 = list(map(lambda a:2*a,list3))
print(list4)

list5 = [11,22,33,44]
list6 = [2,3,4,2]
list7 = list(map(lambda x,y:x*y,list5,list6))
print(list7)