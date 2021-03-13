import numpy as np

def dash(): 
    print('-' * 36)



def hypocalc():
    a = int(input('What is the value of A?: '))
    b = int(input('What is the value of B?: '))
    c = a ** 2 + b ** 2 
    print(c)
    
    


dash()
print('Welcome to Magma. Please press a number on the list given for the corresponding operation')
print('1. Hypotensue Calculator')
dash()
x = input('What would you like to do: ')

if x == "1":
    hypocalc()

else:
    exit()

