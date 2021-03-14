import numpy as np
import math # Importing both math and numpy for now.

def dash(): 
    print('-' * 36)



def hypocalc():
    a = int(input('What is the value of A?: '))
    b = int(input('What is the value of B?: '))
    c = a ** 2 + b ** 2
    d = math.sqrt(c) 
    if type(d) is float:
        print(c)
    else: 
        print(d)
    
    


dash()
print('Welcome to Magma. Please press a number on the list given for the corresponding operation')
print('1. Hypotensue Calculator')
dash()
x = input('What would you like to do: ')

if x == "1":
    hypocalc()

else:
    exit()

