'''
add()
update() -- add number of items to the set
copy() -- it produces the coned copy of the set
pop () -- deletes and returns the arbitary element from the set
remove() -- deletes the specified element from the set, if the elements is not available in the set and an error message will be raised
discard() -- deletes the specified element from the set, if the elements is not available in the set, no error message will be raised
clear()
'''

mySet = {1,2,3,4,5}

print(mySet)
mySet.add(100)
print(mySet)
mySet.update(mySet,range(5))
print(mySet)

copySet = mySet.copy()
print(copySet)

mySet.pop()
print(mySet)
mySet.remove(3)
print(mySet)
mySet.remove(200)
print(mySet)
mySet.discard(2)
print(mySet)
mySet.discard(300)
print(mySet)

mySet.clear()
print(mySet)