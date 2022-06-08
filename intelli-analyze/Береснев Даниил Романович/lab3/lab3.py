import math


def x_next(x, h):
    return x - h


def f(x):
    return math.log(x) + math.pow((x + 1), 3)


def f1(x):
    return 3 * math.pow((x + 1), 2) + 1/x


def method(x, e):
    if (abs(f(x)/f1(x)) > e):
        return method(x_next(x, f(x)/f1(x)), e)
    else:
        return x


x = 1

print("ln(x) + (x + 1)^3 = 0")
print("начальное приближение = ", x)

e = float(input("введите точность = ").replace(",", "."))

print("x =", method(x, e))
