import math

# Метод простых итераций
# x^2=ln(x+1)
# преобразуем к x= ln(x+1)^(1/2)
x = 1
def func(x):
    return math.sqrt(math.log(x+1))

def eps(a,b):
    return abs(a - b)

def calculate(epsilon, x):
    if eps(x, func(x)) > epsilon:
        return calculate(epsilon, func(x))
    else:
        return x

print("\nФункция: x^2-ln(x+1)=0")
epsilon = float(input("Введите погрешность: "))
print("x = ", calculate(epsilon, x))
