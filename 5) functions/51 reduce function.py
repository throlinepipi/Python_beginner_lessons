'''
reduce(function, sequence)
continuously applied to the function of the sequence and produces a single value as an output.
'''

from functools import *
list1 = [1,2,3,4,]
r1 = reduce(lambda a,b: a + b, list1)
print(r1)