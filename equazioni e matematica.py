Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import math
 
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
 
if(a == 0): # bx+c=0
    if(b != 0):
        x=-c/b
        print("x =", x)
    else:
        if(c == 0):
            print("Indeterminata")
        else:
            print("Impossibile")
else:
    delta=b*b-4*a*c
    if(delta > 0):
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif(delta == 0):
        x=-b/a
        print("x =", x)
    else:
        xr=-b/(2*a)
        xi=math.sqrt(-delta)/(2*a)
        x1=complex(xr,xi)
        x2=complex(xr,-xi)
        print("x1 =", x1)
        print("x2 =", x2)