'''
used for loop
'''

def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(10,22,33))
print(mysum(10,22,33,100,100))