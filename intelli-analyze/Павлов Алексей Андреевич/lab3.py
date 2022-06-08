import math


def func(x):
    return x + (2 / (a + b)) * (2 * math.sin(x) - math.atan(x))


def calculate(x, e):
    if abs(func(x) - x) > e:
        return calculate(func(x), e)
    else:
        return func(x)


print("\nEquation: 2 * sinX - arctgX = 0")
a = 2.5
b = 2.6
accuracy = float(input("Accuracy of the equation?\n"))

print("x = ", calculate((a + b) / 2, accuracy))
