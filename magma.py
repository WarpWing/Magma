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

def endpointmid(m1,m2,x1,y1):
    x2 = m1 * 2 - x1
    y2 = m2 * 2 - y1
    print(f"The missing endpoint would be ({x2},{y2})")
def slope(x1, x2, y1, y2):
    Ydiff = y2 - y1 
    Xdiff = x2 - x1
    slope - Ydiff / Xdiff
    print(f"The slope would be {Ydiff} / {Xdiff} or {slope}")

dash()
print('Welcome to Magma by Ty Chermsirivatana. Please press a number on the list given for the corresponding operation')
print('1. Hypotensue Calculator')
print('2. Midpoint Calculator from x1,y1 and x2,y2')
print('3. Endpoint Calculator from Midpoint and x1,y1')
print('4. Slope Calculator from Rise over Run (Difference in Y over Difference in X)')
dash()
x = input('What would you like to do: ')


if x == "1":
    dash()
    a = int(input('What is the value of A?: '))
    b = int(input('What is the value of B?: '))
    dash()
    hypocalc(a,b)
elif x == "2":
    dash()
    x1 = int(input('What is the value of x1?: '))
    y1 = int(input('What is the value of y1?: '))
    x2 = int(input('What is the value of x2: '))
    y2 = int(input('What is the value of y2?: '))
    dash()
    midpoint(x1, x2, y1, y2)
elif x == "3":
    dash()
    m1 = int(input('What is the value of m1?: '))
    m2 = int(input('What is the value of m2?: '))
    x1 = int(input('What is the value of x1: '))
    y1 = int(input('What is the value of y1?: '))
    dash()
    endpointmid(m1,m2,x1,y1)
elif x == "4":
    x1 = int(input('What is the value of x1?: '))
    x2 = int(input('What is the value of x2: '))
    y1 = int(input('What is the value of y1?: '))
    y2 = int(input('What is the value of y2?: '))
    slope(x1, x2, y1, y2)
else:
    exit()

