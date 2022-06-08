import math

a = 2.5
b = 2.6

def f(x):
    return x + (2 / (a + b)) * (2 * math.sin(x) - math.atan(x))

def rasch(x, e):
    if abs(f(x) - x) > e:
        return rasch(f(x), e)
    else:
        return x

print("\nФункция: 2 * sinX - arctgX = 0")
accuracy = float(input("Введите погрешность\n"))
print("x = ", rasch((a + b) / 2, accuracy))
