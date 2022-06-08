import math


def func(x):
    return math.sqrt(math.log(x+1))


def calc(e, x):
    if abs(x - func(x)) > e:
        return calc(e, func(x))
    else:
        return func(x)


print("Вариант задания - ", len("Лебедева Дарья Вячеславовна") % 5)
print("\nФункция: x^2 = ln(x + 1) ---> x = ln(x + 1)^(1 / 2)")
epsilon = float(input("Введите погрешность: "))
print("x = ", calc(epsilon, 1))
