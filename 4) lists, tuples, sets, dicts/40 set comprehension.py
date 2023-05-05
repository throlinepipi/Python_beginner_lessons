'''
indexing, slicing operations are not supported by set.
Set comprehension is possible.
'''

s = {x*x for x in range(5)}
print(s)
