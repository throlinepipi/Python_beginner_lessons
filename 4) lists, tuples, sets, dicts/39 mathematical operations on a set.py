'''
union() -- x.union(y) OR x|y
intersect() -- x.intersection(y) OR x&y
different() -- x.difference(y) OR x-y
symmetric_difference() -- x.symmetric_difference(y) OR x^y -- a set that contains elements from either set but not in both sets

membership operators -- in/ not in
'''

p = {1,2,3,4,5}
q = {5,6,7,8}

print(p.union(q))
print(p|q)

print(p.intersection(q))
print(p&q)

print(p.difference(q))
print(p-q)

print(p.symmetric_difference(q))
print(p^q)

print(2 in p)
print(2 not in p)