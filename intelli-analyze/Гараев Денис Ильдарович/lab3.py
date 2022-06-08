import math

def f(x):
    return math.log10(1+2*x)-2+x

def appr(a, b):
    return a - (f(a)*(b-a))/(f(b)-f(a))
    
def solve(a, b, e):
    if (abs(b - a) < e):
        return b
    else:
        return solve(b, appr(a, b), e)
        
e = float(input('e?'))
a = 0
b = 2
print('x = ', solve(a,b,e))