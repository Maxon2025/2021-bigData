import math

def f(x):
    return math.log(x) + (x+1)**3
    
def der(x):
    return 1/x + 3*(x+1)**2
    
def tangent(x):
    return x - f(x)/der(x)

def eps(a, b):
    return abs(b - a)

def solve(x, e):
    if eps(x, tangent(x)) < e: 
        return x
    else:
        return solve(tangent(x), e)

presition = float(input('e?\n'))
print('x = ', solve(0.01, presition))
