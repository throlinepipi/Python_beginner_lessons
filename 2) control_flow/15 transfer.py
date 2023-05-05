''' break
  continue -- skip the on-going iteration and continues with the next iteration
    pass'''

l = [15,18,25,45]
for i in l:
    if i > 18:
        print("Hello world")
        break
    print(i)

for j in range(8):
    if j == 4:
        print("Hello world")
        break
    print(j)

m = [15,17,25,45,65,9,12]
for a in m:
    if a > 18:
        continue
    print(a)

n = [11,25,5,0,30]
for n1 in n:
    if n1 == 0:
        continue
    print("Hello",n1)

for c in range(8):
    if i%2 == 0:
        print(c)
    else:
        pass