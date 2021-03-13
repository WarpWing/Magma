import math 


def dash(): 
    print('-' * 36)



def hypocalc():
    #a, b = input("Please state your A and B values spaced apart. A example of a valid input would be (1 2): ").split
    a = 3
    b = 5
    c = a ** 2 + b ** 2 
    print(c)



dash()
print('Welcome to Magma. Please press a number on the list given for the corresponding operation')
print('1. Hypotensue Calculator')
dash()
input = input('What would you like to do: ')

if input == '1':
    hypocalc()

else:
    exit()

