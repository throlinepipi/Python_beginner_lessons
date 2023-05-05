'''
Accessing characters in a string
1) By using index
2) By using slice operator -- p[begin_index:end_index:step_value)
     -- forward direction -- default to begin 0 -- default to end is the length of the string -- default for step is incremented by one
     -- backward direction -- default to begin is decremented by one, default for end [-(string_length + 1)]
3) mathematical operators for string
4) Len() function -- finding the numbers of characters in a string
'''

print("using index")
a = 'Hello'
print(a[0])
print(a[4])

print("using slice operator")
s = "My Father is best teacher"
print(s[0:9:1])
print(s[1:7:2])
print(s[:])
print(s[::])
print(s[::-1])

print("mathematical operators for string")
print("Hello"+"World")
print("Hello" * 2)

print("len() function")
n = ('Hello')
print (len(n))

b = "My mother is a teacher"
m = len(b)
i = 0
print("Forward direction")
while i < m:
    print(b[i],end= " ")
    i +=1
print("\nBackward direction")
i = -1
while i >= -m:
    print(b[i],end=' ')
    i = i -1