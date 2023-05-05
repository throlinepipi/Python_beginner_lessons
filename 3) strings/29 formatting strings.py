'''
replacement operators = {}
format method = format()

: f  --  fixed point number (float); default precision is 6
: d -- decimal integer
: b -- binary format
: o -- octal format
: X -- Hexa-decimal format in upper case
: x- - Hexa-decimal format in lower case

{:+d}
{:+f}

:< = left
:> = right
:^ = center
:= forced (+) (-) to the left most position

p.format(string)
'''

#Formatting (Default, Positional, Keyword arguments)
name = 'vijay'
empid = 20201
exp = 4
print("{} empid {} exp {}" . format(name, empid, exp))
print("{x} empid {y} exp {z}" . format(x=name, y=empid, z=exp))
print("{0} empid {1} exp {2}" . format(name, empid, exp))

#Formatting of  Numbers
print("Output: {}".format(133))
print("Output: {:d}".format(133))
print("Output: {:5d}".format(133))
print("Output: {:05d}".format(133))
print("Output: {:b}".format(133))
print("Output: {:f}".format(133.34565342532))
print("Output: {:.2f}".format(133.3456))
print("Output: {:.6f}".format(133.3456))

#Formatting of Signed Numbers
print("signed number: {:+d}".format(133))
print("signed number: {:+d}".format(-133))
print("signed number: {:+f}".format(133.44))
print("signed number: {:+f}".format(-133.44))

#Number formatting with Alignment
print("{:05d}".format(18))
print("{:5d}".format(18))
print("{:<5d}".format(18))
print("{:<05d}".format(18))
print("{:>05d}".format(18))
print("{:^05d}".format(18))
print("{:5d}".format(-18))
print("{:=5d}".format(-18))

#String formatting with format()
print("{:04}".format("man"))
print("{:>6}".format("man"))
print("{:*^7}".format("man"))

#Truncating String Using format()
print("{:.7}".format("vijayyeashekjrfha"))
print("{:06.4}".format("vijayyeashekjrfha"))

#Formatting Dictionary Members Using format()
dog =  {"color": "yellow", "breed": "GR", "age": 2}
print("It has {x[color]} color and it is {x[age]} years old.".format(x=dog))
print("It has {color} color and it is {age} years old.".format(**dog))

UK = {"continent": "Europe", "color": "White people"}
Kenya = {"continent": "Africa", "color": "Colored people"}
print (("Elizabeth is a late queen of UK which continent is {a[continent]} with {a[color]}. Kenya has {b[color]} and it is in {b[continent]}").format(a=UK, b=Kenya))

#Formatting Class Members Using format()
class Human:
    ids = 2021
    name = "sapiens"
print ("They are {c.name} Id: {c.ids}".format(c=Human))

#Dynamic formatting using format()

#Dynamic Float formatting using format()

#Formatting Date Values
import datetime
d = datetime.datetime.now()
print("Date and Time Formate: {:%d/%m/%Y     %H:%M:%S}".format(d))

#Formatting Complex Numbers
complexNumber = 1+2j
print("Real:{0.real}  Imaginary:{0.imag}".format(complexNumber))