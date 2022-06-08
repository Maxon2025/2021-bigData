import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.4, 10, 1000)

# Метод хорд
# lg(1 + 2x) = 2 - x
# реобразуем к 2 - x - lg(1 + 2x) = 0

a = 1
b = 2


def equation_func(x):
    return np.log10(1 + 2 * x) - 2 + x


plt.subplot()
plt.plot(x, equation_func(x))
plt.show()


def func_x(a, b):
    return a - equation_func(a) * (b - a)/(equation_func(b) - equation_func(a))


def epsilon(a, b):
    return abs(equation_func(b) - equation_func(a))


def solve_equation(a, b, presition):
    if epsilon(a, b) > presition:
        if equation_func(a) * equation_func(func_x(a, b)) <= 0:
            return solve_equation(a, func_x(a, b), presition)
        else:
            return solve_equation(func_x(a, b), b, presition)
    else:
        return a


print("\nEquation: lg(1 + 2x) = 2 - x")
presition = float(input("Type what presition do you need?\n"))
print("x = ", solve_equation(a, b, presition))
