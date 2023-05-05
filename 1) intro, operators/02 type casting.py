print("int casting")
print(int(12.33))
print(int(12))
print(12.33)
print(int(True))
print(int(False))
print(int("15"))
#can't convert complex numbers to int
#print(int(15+6j))

print("float casting")
print(float(12.33))
print(float(12))
print(float(True))
print(float(False))
print(float("15"))
#can't convert complex numbers to float
#print(int(15+6j))

print("complex casting")
print(complex(12.33))
print(complex(12))
print(complex(True))
print(complex(False))
print(complex("15"))
print(complex(50,-2))  #complex(p,q) q -- imaginary part

print("boolean casting")
print(bool(0))
print(bool(1))
print(bool(15))
print(bool(0.0))
print(bool(15-6j))
print(bool(0-6j))
print(bool(0-0j))
print(bool("True"))
print(bool("False"))
print(bool(""))

print("string casting")
print(str(12.33))
print(str(12))
print(str(15+6j))
print(str(True))
print(str(False))
print(str("15"))