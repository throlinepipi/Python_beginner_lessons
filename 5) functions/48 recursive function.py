'''
Step1 -- Ground floor
Step2 -- Step1 + Ground floor
Step3 -- Step2 + Step1 + Ground floor

factorial(4)

r = 4 *  factorial(3)
r = 4 * 3 * factorial(2)
r = 4 * 3 * 2 * factorial(1)
r = 4 * 3 * 2 * 1 * 1
'''

def factorial(n):
    if n==0:
        r=1
    else:
        r=n*factorial(n-1)
    return r
print("factorial:",factorial(4))
