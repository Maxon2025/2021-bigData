import math
import numpy as np
from math import factorial

#вариант 2 (len('Шишмакова Татьяна Вадимовна') % 5)
#функция: x^2=ln(x+1). Методом простых итераций
# transform to x = np.sqrt(np.log(x+1))
# take some initial x0. let it be 2
x = 2
def equation_func(x):
    return np.sqrt(np.log(x+1))

def epsilon(x):
    return abs(equation_func(x) - equation_func(equation_func(x)))

def solve_equation(x, presition):
    if epsilon(x) > presition:
        return solve_equation(equation_func(x), presition)
    else:
        return x

print("\nФункция: x^2-ln(x+1)=0")
presition = float(input("Введите погрешность: "))
print("x = ", solve_equation(x, presition))
