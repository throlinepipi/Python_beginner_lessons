'''
membership operators -- in, not in -- used with strings to determine whether a string is present in another string
'''
str1 = 'vijay'
print('j' in str1)
print('w' in str1)

str1 = input("Enter String - 1: ")
substring = input("Enter substring : ")
if substring in str1:
    print(substring, "Matched string-1")
else:
    print(substring,"Unmatched string-1")