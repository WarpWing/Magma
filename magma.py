import numpy as np
import math # Importing both math and numpy for now.

def dash(): 
    print('-' * 36)



def hypocalc(a,b):
    c = a ** 2 + b ** 2
    d = math.sqrt(c) 
    if type(d) is float: #Float is a number with decimals as opposed to Integer which is a whole number.
        print(f"{c} does not simply. This is the decimal return. Please make sure to meet roundup requirements.")
    else: 
        print(f"{c} does simply and returns {d} as it's square root")
    #Note: Does not do automatic Radical Conversion. Should add that soon.

def midpoint(x1, x2, y1, y2):
    xout = (x1 + x2) / 2 
    yout = (y1 + y2) / 2
    print(f"The midpoint would be ({xout},{yout})")

    
    


dash()
print('Welcome to Magma. Please press a number on the list given for the corresponding operation')
print('1. Hypotensue Calculator')
print('2. Midpoint Calculator from x1,y1 and x2,y2')
dash()
x = input('What would you like to do: ')


if x == "1":
    a = int(input('What is the value of A?: '))
    b = int(input('What is the value of B?: '))
    hypocalc(a,b)
elif x == "2":
    x1 = int(input('What is the value of x1?: '))
    y1 = int(input('What is the value of y1?: '))
    x2 = int(input('What is the value of x2: '))
    y2 = int(input('What is the value of y2?: '))
    midpoint(x1, x2, y1, y2)
else:
    exit()

