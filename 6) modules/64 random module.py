'''
generate vavrious random number

random() -- produce any float value in the range 0 to 1, without the inclusive of 0 and 1
randint() -- produce any random integer between specified numbers with including them
uniform() -- produce any random float values between specified numbers without including  them
randrange([begin],end,[step]) -- produce any random number froom the defined range.
choice() -- produce a random object from a specified list or tuple.

'''

import random

for v in range (6):
    print(random.random())

for a in range(5):
     print(random.randint(1,10))

for b in range(5):
    print(random.uniform(1,6))

for c in range(5):
    print(random.randrange(1,9,2))

tup2 =( 30,40,50,60)
m = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for d in range(5):
    print(random.choice(m))
