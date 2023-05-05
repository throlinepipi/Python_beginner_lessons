'''
1) len()
2) clear()
3) get() -- variable.get(key) -- if the key is present, it will return the associated value, otherwise it will return default value.
            -- variable.get(key,defaultvalue)
4) pop() -- variable.pop(key) -- delete the value of specified key
5) popitem -- variable.popitem() -- delete the value of random key -- while deleting from the empty dictionary, an error message will be raised
6) keys() -- return all keys in the dictionary
7) values() -- return all values in the dictionary
8) items() -- return the list of tuples showing the keys-values pairs
9) copy() -- used to construct the cloned copy -- if the key is not present, then the mentioned (key-value) will be appended as a new element to the dictionary
                  -- new_variable = variable.copy();
                                                    set.default():'
                                                    d.setdefault(key,value)
10) update() -- elements in dicitonary x will be appended to the given dictionary d-- d.update(x)
'''

myDict = {10: 'James', 20:'Alice', 30:'Bob'}

print(myDict.get(10))
print(myDict.get(50))
print(myDict.get(50,"Myanmar"))

myDict.pop(20)
print(myDict)

myDict.popitem()
print(myDict)

myDict = {10: 'James', 20:'Alice', 30:'Bob'}

print(myDict.keys())

print(myDict.values())

print(myDict.items())

print(myDict.setdefault(40,"Carles"))
print(myDict)
myxDict = {60: 'James', 70:'Alice', 80:'Bob'}
myDict.update(myxDict)
print(myDict)