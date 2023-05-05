'''
rstrip() = returns the output with the trailing white space characters eliminated
lstrip() =  returns the output with the leading white space characters eliminated
strip() = returns the output with the trailing and leading white space characters eliminated
'''

s = input("Enter the string: ")
m = s.strip()
if m == 'Myanmar':
    print("Welcome to Myanmar")
elif m == "England":
    print("Welcome to England")
else:
    print("Sorry")
