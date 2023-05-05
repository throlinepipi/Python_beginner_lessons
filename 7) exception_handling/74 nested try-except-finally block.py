'''
The risky code needs to be taken in the outer try block and the more risky code needs to be  taken in the inner try block.
If in the inner try block, if an exception occurs then, the inner except block will manage the exception.
If it is unable to manage the exception then the outer except block will manage the exception.

Syntax
try:
        ______
        try:
                ______
        except:
                ______
except:
        ______

control flow of nested try-except-finally:
try:
        declaration-a
        declaration-b
        declaration-c
        try:
                declaration-d
                declaration-e
                declaration-f
except P:
            declaration-g
finally:
            declaration-h
            declaration-i
except Q:
            declaration-j
finally:
            declaration-k
            declaration-l

Case 1: When there is no exception, then a, b, c, d, e, f, h, i, k, l will terminate normally.
Case 2: When an exception occurs at declaration-b and its associated except block gets matched then a, j, k, l will terminate normally.
Case 3: When exception occurs at declaration-b and its associated except block didn’t match, then a, k will terminate abnormally.
Case 4: When exception occurs at declaration-e and the inner except block gets matched then a, b, c, d, g, h, i, k, l, will terminate normally.
Case 5: When an exception occurs at declaration-e and the inner except block didn’t match but the outer except block gets matched then a, b, c, d, h, j, k, l will terminate normally.
Case 6: When an exception occurs at declaration-e and the inner and the outer except blocks didn’t match then a, b, c, d, h, k will terminate abnormally.
Case 7: When an exception occurs at declaration-g and its associated except block gets matched then, a, b, c,……, h, j, k, l will terminate normally.
Case 8: When an exception occurs at declaration-g and its associated except block didn’t match then, a, b, c, d, e, f, g, h, k will terminate abnormally.
Case 9: When an exception occurs at declaration-h and its associated except block gets matched then a, b, c, ….., j, k, l will terminate normally.
Case 10: When exception occurs at declaration-h and its associated except block didn’t match then a, b, c, ….., k will terminate abnormally.
Case 11: When an exception occurs at declaration-i and its associated except block gets matched then a, b, c, ….., h, j, k, l will terminate normally.
Case 12: When an exception occurs at declaration-i and its associated except block didn’t match then a, b, c, …… h, k will terminate abnormally.
Case 13: When exception occurs at declaration-j then it will terminate abnormally but prior to abnormal termination, the finally block will be processed.
Case 14: When an exception occurs at declaration-k or declaration-l then it will terminate abnormally.
'''

try:
    print("Outer try block")
    try:
        print("Inner try block")
        print(10/"0") #print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("Outer except block")
finally:
    print("Outer finally block")