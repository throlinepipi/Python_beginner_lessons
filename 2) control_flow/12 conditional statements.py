#if  -- if the given condition is True
#if-else
#if-elif
#if-elif-else
""" if condition 1
            Action 1
        elif condition 2
             Action 2
        elif condition 3
             Action 3
        else
              default action """

n1 = int(input("Enter a first number::" ))
n2 = int(input("Enter a second number::" ))
o = int(input("Enter 1 to make addition::"))
if o == 1:
    print(n1+n2)
elif o == 2:
    print(n1-n2)
elif o == 3:
    print(n1*n2)
else:
    print(n1/n2)