print("Hw 1")
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a > b:
    print(b)
elif b > a:
    print(a)


print("Hw 2")
s = int(input("Enter first number:"))
t = int(input("Enter second number:"))
w = int(input("Enter third number:"))
if s > t > w:
    print(s)
elif s > w > t:
    print(s)

elif t > s > w:
    print(t)
elif t > w > s:
    print(t)

elif w > s > t:
    print(w)
elif w > t > s:
    print(w)



print ("Hw 3")
x = int(input("Enter number from 1 to 10:: "))
if x >= 1 and x <= 10:
    print("Right")
else:
    print("The number is not within 1 to 10")



print ("Hw 4")
y = 'ym'
while y != 'YMTK':
  y = input("Enter a name 'YMTK':")




print ("HW 5")
l = [1,2,3]
for i in l:
    if i < 4:
        print("Vimal")
        continue