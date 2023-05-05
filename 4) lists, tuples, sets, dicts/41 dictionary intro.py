'''
collection that stores values along with keys.
sequences of keys and values pairs are separated by commas
pairs are sometimes called entries

create -- { } OR dict()

access data -- using key (error message when the mentioned key is not  present)
update -- variable[key] = value
delete -- del variable[key] || variable.clear() -- remove all entries || del variable -- remove all entries and cannot access that object
'''

myDict = {10: 'James', 20:'Alice', 30:'Bob'}
print(myDict[10])
#print(myDict[50])

myDict[50] = 'Carles'
print(myDict)

del myDict[20]
print(myDict)
mySecondDict = {10: 'James', 20:'Alice', 30:'Bob'}
mySecondDict.clear()
print(mySecondDict)
myThirdDict = {10: 'James', 20:'Alice', 30:''}
del myThirdDict
print(myThirdDict)

