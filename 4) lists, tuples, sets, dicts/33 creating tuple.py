'''
1 -- p =():  -- Am empty tuple
2 -- p = (22,) // p = 22,  -- A single-valued tuple
3 -- p = (11,22,33) // p = 11,22,33 -- A multi-valued tuple
4 -- by using tuple() function
'''
test= [20,32,12,33]
print(test)
print(type(test))
test = tuple(test)
print(test)
print(type(test))