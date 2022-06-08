import math
import numpy as np
from math import factorial

# Tangent method or Newton 's method
# log(x)+((x+1)**3) = 0
# derivative: (1/x)+(3*((x+1)**(2)))
# take some initial x. let it be 0.5

def equation_func(x):
    return np.log(x)+((x+1)**3)

def equation_proizvfunc(x):
    return (1/x)+(3*((x+1)**(2)))

def solve_equation(x, presition): #,kolvoiter):
    """
    for n in range(0,kolvoiter):
        if abs(equation_func(x)) < presition:
            return x
        x = x - equation_func(x)/equation_proizvfunc(x)
"""
    if abs(equation_func(x)-equation_func(equation_func(x))) < presition:
       return x
    else:
        solve_equation(x-equation_func(x)/equation_proizvfunc(x), presition)

var=len('Жирнова Полина Михайловна')%5
print("\nВариант", var)
print("\nФункция: ln x + (x+1)^3 = 0")

x = 0.5
presition = float(input("\nВведите погрешность: "))
print("x = ", solve_equation(x,presition))#,100))
