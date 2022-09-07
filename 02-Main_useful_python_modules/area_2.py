#!/opt/local/bin/python 

def square(x):
    '''
    Calculate the area for a square with of width = x
    '''
    return x**2

def circle(r):
    '''
    Calculates the area of a circle of radius r
    '''
    pi = 3.14159
    return pi * r**2

print('The square of 4 is ', square(4))
